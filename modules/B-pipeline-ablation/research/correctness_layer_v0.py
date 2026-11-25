#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
correctness_layer_v0.py — pfb judge correctness 层原型（机械 + 连续，无 LLM）

# origin: ai (2026-11-25)
# 设计: research/correctness-layer-design.md（同目录）
# 目的: 修复 coverage 陷阱 — 机械区分 A1(候选构建断点) vs A3(排序/权重断点)
# 输入: T8b 6 条 (raw_outputs_t8b.json) + S5 run (runs-s5-sm-gpu.json)
# 输出: 分数表 stdout + correctness-layer-dryrun-20261125.json
# 复用: gold-gpu-units.json (36 单元, cov 对照轴); calc.py gold 数值锚
# 不修改 judge_v1.py (frozen f6072397f)

轴: C 候选构建 / E 评估完整性 / R 排序结局 / S 结构签名 / N 数值容差
判别: P_A1 = 1-C ; P_A3 = E1*R_low ; 阈值见设计 §3
"""
import json, re, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
PFB = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
T8B_PATH = os.path.join(PFB, "tasks/think-trigger/exp-results/raw_outputs_t8b.json")
S5_PATH = os.path.join(PFB, "experiments/stage-ablation/runs-s5-sm-gpu.json")
UNITS_PATH = os.path.join(PFB, "modules/B-pipeline-ablation/gold-gpu-units.json")
OUT_JSON = os.path.join(HERE, "correctness-layer-dryrun-20261125.json")

NEG_WIN = 40          # 否定语境窗口（±字符）
NEG_PAT = re.compile(r"遗漏|未覆盖|缺失|缺少|未纳入|没考虑|漏掉|没提|不考虑|排除")
# winner 配置 4×3090 正则族（设计 §2 C2）
CFG4 = re.compile(
    r"4\s*[×xX✕*]\s*(?:RTX\s*)?3090"
    r"|(?:RTX\s*)?3090\s*[×xX✕*]\s*4(?!\d)"
    r"|[4四]\s*(?:张|卡|块)\s*(?:RTX\s*)?3090"
    r"|(?:RTX\s*)?3090\s+[4四]\s*(?:张|卡|块)")
STRONG_REC = re.compile(r"主推荐|首选|最终推荐|最终方案|推荐方案|最佳方案|最优方案|综合推荐|最终结论|推荐：|推荐:")
# v1 弱推荐语义兜底: 无 STRONG_REC 行时, 含 CFG4 的弱推荐行命中 winner → R_low=0
#   防假阳性: winner 被评估+推荐但推荐语句无关键词(如"建议优先部署 4×RTX 3090")→ 误判 A3
WEAK_REC = re.compile(r"建议|优先|推荐|部署|选用|采纳")
# 否定守卫: 覆盖"不X"(v1) + "未X"(v1.1) 两族否定, 防弱兜底把"否定 winner"误读为"推荐 winner"
#   v1.1 补: "未采用 4×3090, 建议优先部署 2×4090" 这类行(否定 winner+推荐他项)
#   若 NEG_REC 漏掉"未采用"→ 整行被误判为推荐 winner → 假 indeterminate(应 A3)
NEG_REC = re.compile(r"不建议|不推荐|不采纳|不可行|淘汰|放弃|排除|否决"
                     r"|未采用|未选择|未采纳|未部署|未选用|未推荐")
EVAL_NUM = re.compile(r"t/s|tok/s|tokens?/s|TCO|成本|\$|元|/GB|分\b|\d+\s*W\b")
# gold 数值锚（name, gold值, 数字正则, 语境正则, 语境窗口）← calc.py / gold-tree N-5.2
# 语境要求防误报: "24 GB"(显存) 不误触 KV 锚; 1008 GB/s(4090) 不误触 936 锚(936 用精确值)
NUM_ANCHORS = [
    ("bw936",   936.0,  re.compile(r"(936)\s*(?:GB/s|Gbps)"), None, 0),
    ("w4_14gb", 14.0,   re.compile(r"(\d{1,2}(?:\.\d+)?)\s*GB"), re.compile(r"W4|INT4|NVFP4|4\s*bit|4-bit"), 30),
    ("w8_27gb", 27.0,   re.compile(r"(\d{1,2}(?:\.\d+)?)\s*GB"), re.compile(r"W8|INT8|FP8|BF16|8\s*bit|8-bit"), 30),
    ("kv24_7",  24.7,   re.compile(r"(\d{1,2}(?:\.\d+)?)\s*GB"), re.compile(r"KV|kv|cache|缓存"), 30),
    ("pf594",   594.0,  re.compile(r"(594)\s*(?:T|TFLOP)"), None, 0),
    ("cp0679",  0.679,  re.compile(r"0\.(\d{1,4})"), re.compile(r"c_pass|¢|cent|/task|每任务|成本"), 30),
    ("bwgate",  774.0,  re.compile(r"(774|1034|1574)\s*(?:GB/s|Gbps)"), None, 0),
]
NUM_TOL = 0.10


def load_samples():
    """返回 [(name, text, nodes), ...]：T8b 6 条 + S5 1 条（设计 §4 归一化）。
    对称抽取：arm_a 与 arm_b 都取 content+reasoning（含 final_*），
    早期版本 arm_b 只取 content 造成不对称（3090 计数减半, arm_b A1 判定失真）。
    nodes = 用于 cov 的节点列表（judge_v1 口径按节点 claim 编码）：
    S5 = 真实节点 claim；T8b 自由文本无节点，用非空行作节点近似。"""
    d = json.load(open(T8B_PATH))
    out = []
    for i, a in enumerate(d["arm_a"]):
        text = a.get("content", "") + "\n" + a.get("reasoning", "")
        out.append((f"arm_a[{i}]", text, [ln.strip() for ln in text.split("\n") if ln.strip()]))
    for i, b in enumerate(d["arm_b"]):
        parts = [b.get("final_content", "") or "", b.get("final_reasoning", "") or ""]
        st = b.get("stages", {})
        vals = st.values() if isinstance(st, dict) else st
        for v in vals:
            if isinstance(v, dict):
                parts.append(v.get("content", "") or "")
                parts.append(v.get("reasoning", "") or "")
            else:
                parts.append(v if isinstance(v, str) else "")
        text = "\n".join(parts)
        out.append((f"arm_b[{i}]", text, [ln.strip() for ln in text.split("\n") if ln.strip()]))
    s5 = json.load(open(S5_PATH))
    s5_nodes = [n.get("claim", "") for n in s5["nodes"]]
    out.append(("S5", "\n".join(s5_nodes), s5_nodes))
    return out


def neg_mask(text, pat):
    """返回 text 中 pat 每个匹配的 (start, is_neg)；is_neg = ±NEG_WIN 内有否定词。"""
    res = []
    for m in pat.finditer(text):
        lo, hi = max(0, m.start() - NEG_WIN), min(len(text), m.end() + NEG_WIN)
        res.append((m.start(), bool(NEG_PAT.search(text[lo:hi]))))
    return res


# ---------------- 轴 C: 候选构建对齐（A1 诊断轴） ----------------
def axis_c(text):
    """C = 0.5*C1e + 0.5*C2。C1e: 3090 有效提及(扣否定语境); C2: 4×3090 配置提及。"""
    masks = neg_mask(text, re.compile(r"3090"))
    neg = sum(1 for _, n in masks if n)
    eff = max(len(masks) - neg, 0)
    c1e = min(eff / 4.0, 1.0)
    c2 = min(len(CFG4.findall(text)) / 2.0, 1.0)
    return 0.5 * c1e + 0.5 * c2, {"c1_total": len(masks), "c1_neg": neg,
                                  "c1e": round(c1e, 3), "c2": round(c2, 3),
                                  "cfg4_hits": len(CFG4.findall(text))}


# ---------------- 轴 E: 评估完整性（A3 诊断轴） ----------------
def axis_e(text):
    """E = 0.5*E1 + 0.5*E2。E1: 4×3090 配置评估行; E2: 3090 规格行(非否定)。"""
    lines = text.split("\n")
    e1_rows = sum(1 for ln in lines if CFG4.search(ln) and EVAL_NUM.search(ln))
    e1 = min(e1_rows / 2.0, 1.0)
    e2_rows = 0
    for ln in lines:
        if "3090" not in ln:
            continue
        i = text.find(ln)
        ctx = text[max(0, i - NEG_WIN):i + len(ln) + NEG_WIN]
        if NEG_PAT.search(ctx):
            continue
        if re.search(r"GB/s", ln) and re.search(r"GB|\$|元", ln):
            e2_rows += 1
    e2 = min(e2_rows / 2.0, 1.0)
    return 0.5 * e1 + 0.5 * e2, {"e1": round(e1, 3), "e1_rows": e1_rows,
                                 "e2": round(e2, 3), "e2_rows": e2_rows}


# ---------------- 轴 R: 排序结局 ----------------
def axis_r(text, e1_rows):
    """R_low: 配置被评估过(E1>0)时, 强推荐行是否含 4×3090。被选中→0, 垫底→1; 未评估→0.5。
    v1 兜底: 无任何强推荐行时(推荐表述无关键词), 扫含 CFG4 的弱推荐语义行,
    命中 winner(且非否定语境)→ R_low=0, 防假阳性误判 A3。
    有强推荐行但未含 winner → 保持 R_low=1(A3 信号, 不启用兜底)。"""
    if e1_rows == 0:
        return 0.5, {"strong_rec_lines": 0, "note": "E1=0, R 未定义, 中性 0.5"}
    rec_lines = [ln for ln in text.split("\n") if STRONG_REC.search(ln)]
    if rec_lines:
        picked = any(CFG4.search(ln) for ln in rec_lines)
        return (0.0 if picked else 1.0), {"strong_rec_lines": len(rec_lines),
                                          "winner_in_strong_rec": picked, "weak_fallback": False}
    # 兜底: 无强推荐行 → 弱推荐语义扫描(否定守卫)
    weak_hits = [ln for ln in text.split("\n")
                 if CFG4.search(ln) and WEAK_REC.search(ln) and not NEG_REC.search(ln)]
    picked = len(weak_hits) > 0
    return (0.0 if picked else 1.0), {"strong_rec_lines": 0, "winner_in_strong_rec": False,
                                      "weak_fallback": True, "weak_hit_lines": len(weak_hits)}


# ---------------- 轴 S: gold 树结构签名 ----------------
S_PATS = {
    "s_band": re.compile(r"\b(?:774|1034|1574)\b\s*(?:GB/s|Gbps)"),   # N-5.2 带宽准入
    "s_mem":  re.compile(r"(?:W|权重)\s*[+＋]\s*(?:KV|kv)[^。\n]{0,40}(?:≤|<=|不超过|小于等于|显存)"
                        r"|(?:≤|<=|不超过|小于等于)[^。\n]{0,40}(?:W|权重)\s*[+＋]\s*(?:KV|kv)"
                        r"|(?:KV|kv)[^。\n]{0,30}(?:≤|<=|不超过|小于等于)[^。\n]{0,30}(?:显存|GB)"),  # N-5.1
    "s_dec":  re.compile(r"(?:W|权重)[^。\n]{0,20}[+＋][^。\n]{0,20}(?:n|并发)[^。\n]{0,10}[×xX*][^。\n]{0,10}(?:KV|kv)"),  # N-3.2
    "s_obj":  re.compile(r"c_pass|每个通过任务|每任务成本|单位任务成本|单位成本"),  # N-0
}
def axis_s(text):
    hits = {k: len(p.findall(text)) for k, p in S_PATS.items()}
    scores = {k: min(n, 1.0) for k, n in hits.items()}
    return sum(scores.values()) / len(scores), {"hits": hits, "scores": {k: round(v, 3) for k, v in scores.items()}}


# ---------------- 轴 N: 数值容差 ----------------
def axis_n(text):
    """N = 命中且容差内(±10%)的 gold 锚数 / 7。bwgate 特例: 774/1034/1574 是同规则三档, 任一命中即算。"""
    got = {}
    for name, gold, num_re, ctx_re, win in NUM_ANCHORS:
        best = None
        for m in num_re.finditer(text):
            if ctx_re is not None:
                lo, hi = max(0, m.start() - win), min(len(text), m.end() + win)
                if not ctx_re.search(text[lo:hi]):
                    continue
            try:
                v = float(m.group(1))
            except (ValueError, IndexError):
                continue
            tol = 0.0 if name == "bwgate" else NUM_TOL
            if abs(v - gold) / gold <= tol:
                best = v
                break
        if best is not None:
            got[name] = best
    return len(got) / len(NUM_ANCHORS), {"anchors_hit": got, "n_hit": len(got),
                                         "n_total": len(NUM_ANCHORS)}


# ---------------- 合成 + 判别 ----------------
W_C, W_E, W_S, W_N = 0.35, 0.25, 0.20, 0.20
TH_A1, TH_A3 = 0.7, 0.5

def judge_text(text, th_a1=TH_A1, th_a3=TH_A3, c1e_th=0.5):
    c, c_d = axis_c(text)
    e, e_d = axis_e(text)
    r, r_d = axis_r(text, e_d["e1_rows"])
    s, s_d = axis_s(text)
    n, n_d = axis_n(text)
    corr = W_C * c + W_E * e + W_S * s + W_N * n
    p_a1 = 1.0 - c
    p_a3 = e_d["e1"] * r
    # A2 (候选集粒度断点, dry-run 新发现): winner 卡型充分出现(C1e≥c1e_th)
    # 但 winner 配置从未构造(C2<0.5)且从未评估(E1<0.5) → 非A1(卡型在)非A3(配置没评估)。
    # 与 A3 严格互斥(E1 条件相反); 与 A1 在 C2=0 且 C1e 接近 c1e_th 时有边界重叠,
    # 由判定优先级裁决(A1 先判, 卡型边缘出现时保守归 A1)。观测数据上三型完全分离。
    c2bp = c_d["c1e"] >= c1e_th and c_d["c2"] < 0.5 and e_d["e1"] < 0.5
    if p_a1 >= th_a1 and p_a3 >= th_a3:
        verdict = "A1+A3"
    elif p_a1 >= th_a1:
        verdict = "A1"
    elif p_a3 >= th_a3:
        verdict = "A3"
    elif c2bp:
        verdict = "A2"
    else:
        verdict = "indeterminate"
    return {"corr": round(corr, 3), "C": round(c, 3), "E": round(e, 3),
            "R_low": round(r, 3), "S": round(s, 3), "N": round(n, 3),
            "P_A1": round(p_a1, 3), "P_A3": round(p_a3, 3), "C2BP": c2bp,
            "verdict": verdict,
            "detail": {"C": c_d, "E": e_d, "R": r_d, "S": s_d, "N": n_d}}


# ---------------- cov 对照轴（judge_v1 口径, 可选 bge-m3） ----------------
COS_THRESHOLD = 0.70  # 同 judge_v1.py 标定值（frozen, 只读引用）
_cov_model = None
_cov_gold = None

def cov_score(nodes):
    """judge_v1 口径: 节点级 bge-m3 top-1 cosine vs 36 gold units, >=0.70 计命中
    (同 judge_v1.layer_coverage: 按节点 claim 编码, 非 512 字切片——切片口径会低估,
    实测 S5 切片 0.139 vs 节点级 0.389)。无 bge-m3 时返回 None（dry-run 表标 NA）。"""
    global _cov_model, _cov_gold
    if _cov_model is None:
        try:
            from sentence_transformers import SentenceTransformer
            import numpy as np
            _cov_model = SentenceTransformer("BAAI/bge-m3")
            units = json.load(open(UNITS_PATH))["units"]
            _cov_gold = (_cov_model.encode([u["text"] for u in units],
                                           normalize_embeddings=True), units)
        except Exception as ex:
            print(f"[cov] bge-m3 不可用 ({ex.__class__.__name__}), cov 列 = NA", file=sys.stderr)
            _cov_model = False
            return None
    if _cov_model is False:
        return None
    import numpy as np
    gold_emb, units = _cov_gold
    emb = _cov_model.encode(nodes, normalize_embeddings=True)
    sim = emb @ gold_emb.T
    top1 = sim.argmax(axis=1)
    top1_sim = sim[np.arange(len(emb)), top1]
    matched = set(int(j) for j in top1[top1_sim >= COS_THRESHOLD])
    return round(len(matched) / len(units), 3)


# ---------------- 扰动自测（判别规则的因果性，非 n=2 相关性） ----------------
def selftest():
    """11 断言: 基线 3(A1/A3/A2) + 变异 3 + 阳性对照 1 + A2 因果 1
    + FP 边界已修 1(V7) + 否定守卫 2(V8 不X族 / V9 未X族)。
    全过 = 三型判别由探针因果驱动, 非对样本过拟合, 且不'全判病'。
    V7 钉住 v0 假阳性已修(winner 评估+无关键词推荐→indeterminate, v1 兜底);
    V8/V9 钉住否定守卫两族(不X/未X)——winner 被评估但被否定→仍 A3, 兜底不误救。"""
    samples = {n: t for n, t, _ in load_samples()}
    a0, a2 = samples["arm_a[0]"], samples["arm_a[2]"]
    results = []
    # 基线
    r = judge_text(a0); results.append(("baseline arm_a[0]→A1", r["verdict"] == "A1", r["verdict"]))
    r = judge_text(a2); results.append(("baseline arm_a[2]→A3", r["verdict"] == "A3", r["verdict"]))
    # V1 R 轴因果: arm_a[2] 强推荐行改为推 4×3090 → 应脱离 A3
    v1 = a2.replace("主推荐: 方案 B (2×RTX 4090, INT4 AWQ)",
                    "主推荐: 方案 D (4×RTX 3090, INT4 AWQ)")
    assert v1 != a2, "V1 替换未命中(文本变了?), 需更新 pattern"
    r = judge_text(v1); results.append(("V1 winner进强推荐→非A3", r["verdict"] != "A3", r["verdict"]))
    # V2 C 轴因果: arm_a[2] 抹掉 3090 → 应翻成 A1
    r = judge_text(a2.replace("3090", "3080")); results.append(("V2 抹3090→A1",
                                                                 r["verdict"] == "A1", r["verdict"]))
    # V3 E 轴因果: arm_a[0] 注入 4×3090 候选+评估行(不加强推荐) → 应翻成 A3
    inj = ("\n| D | 4×RTX 3090 | 96 GB | INT4 | ✅ 可行 |\n"
           "| D | 4×RTX 3090 (二手) | 10-15 t/s | TCO $5,839 |\n")
    r = judge_text(a0 + inj); results.append(("V3 注入评估上下文→A3",
                                              r["verdict"] == "A3", r["verdict"]))
    # V4 阳性对照: winner 被完整评估且被强推荐 → 既非 A1 也非 A3 (防"全判病"假阳性)
    v4 = a2.replace("主推荐: 方案 B (2×RTX 4090, INT4 AWQ)",
                    "主推荐: 方案 D (4×RTX 3090, INT4 AWQ)")
    assert v4 != a2, "V4 替换未命中"
    r = judge_text(v4); results.append(("V4 阳性对照(winner评估+推荐)→非A1非A3",
                                        r["verdict"] == "indeterminate", r["verdict"]))
    # V5 A2 基线: arm_a[1] 卡型充分出现但 4×3090 从未构造/评估 → 候选集粒度断点
    a1 = samples["arm_a[1]"]
    r = judge_text(a1); results.append(("V5 基线 arm_a[1]→A2(候选集粒度断点)",
                                        r["verdict"] == "A2", r["verdict"]))
    # V6 A2 因果: arm_a[1] 抹掉 3090 → 卡型消失 → 应翻成 A1
    r = judge_text(a1.replace("3090", "3080")); results.append(("V6 A2抹3090→A1",
                                                                r["verdict"] == "A1", r["verdict"]))
    # V7 FP 边界(已修): winner 被完整评估(E1>0)且被推荐, 但推荐语句不含 STRONG_REC 关键词
    #   → v0 误判 A3(假阳性); v1 弱推荐语义兜底后应判 indeterminate(R_low=0)。
    #   此断言钉住修复: 若未来兜底逻辑退化, 此项会翻回 A3 报警。
    lines = [ln for ln in a2.split("\n") if not STRONG_REC.search(ln)]
    fp = "\n".join(lines) + "\n综上, 综合性价比来看, 建议优先部署 4×RTX 3090 方案。\n"
    r = judge_text(fp); results.append(("V7 FP边界已修(winner评估+无关键词推荐)→非A3[v1兜底生效]",
                                        r["verdict"] != "A3", r["verdict"]))
    # V8 否定守卫: winner 被评估但被否定("不推荐 4×RTX 3090")→ 兜底不应误救, 仍 A3
    neg = "\n".join(lines) + "\n综上, 4×RTX 3090 成本过高, 不推荐, 建议优先部署 2×RTX 4090 方案。\n"
    r = judge_text(neg); results.append(("V8 否定守卫(winner评估+被否定)→仍A3[兜底不误救]",
                                         r["verdict"] == "A3", r["verdict"]))
    # V9 否定守卫"未X"族(v1.1): winner 被评估但被"未采用"否定 → 兜底不应误救, 仍 A3
    #   回归哨兵: 若 NEG_REC 漏掉"未X"否定族, 此项会翻成 indeterminate 报警
    neg2 = "\n".join(lines) + "\n综上, 4×RTX 3090 功耗过高, 未采用, 建议优先部署 2×RTX 4090 方案。\n"
    r = judge_text(neg2); results.append(("V9 否定守卫未X族(winner评估+未采用)→仍A3[v1.1]",
                                          r["verdict"] == "A3", r["verdict"]))
    ok = all(p for _, p, _ in results)
    for name, p, got in results:
        print(f"  [{'PASS' if p else 'FAIL'}] {name} → {got}")
    print(f"selftest: {'ALL PASS' if ok else 'FAIL'} ({sum(p for _,p,_ in results)}/{len(results)})")
    return ok


# ---------------- 锚值一致性核验（回应硬要求#1: 复用现有 gold 基础设施, 无平行 gold 漂移） ----------------
def verify_anchors():
    """N 轴锚值硬编码在 NUM_ANCHORS, 源 = calc.py 参数表 + gold-gpu-units.json N-5.2。
    逐一比对源文件实际值 vs 脚本硬编码值, 全一致 = 复用忠实, 无平行 gold 漂移。"""
    import importlib.util
    calc_path = os.path.join(PFB, "bench/rubric-v3/tasks/T0-local-27b/reference/calc.py")
    spec = importlib.util.spec_from_file_location("calc_gold", calc_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"无法加载 calc.py: {calc_path}")
    calc = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(calc)
    src = {
        "bw936":  calc.HARDWARE["3090"]["bw"],
        "w4_14gb": calc.W_BYTES["W4"],
        "w8_27gb": calc.W_BYTES["W8"],
        "kv24_7":  calc.KV_PER_STREAM,
        "pf594":   calc.PREFILL_FLOPS / 1e12,
    }
    # cp0679 特殊: gold 锚 = L5§4 文档化点值 0.679 (calc.py docstring 验收锚),
    # calc.py 实算值依赖 tp_eff=0.81 标定 (实算 0.680713)。
    # 核验方式: 锚值须在 10% 容差内贴近实算值 (非严格相等, 因标定差 0.25%)。
    cp_computed = calc.c_pass("3090", 4, "W4", 2)[0]
    units = json.load(open(UNITS_PATH))["units"]
    n52 = next(u for u in units if u["unit_id"] == "N-5.2")
    m = re.search(r"W4\s+(\d+)\s*/\s*W8\s+(\d+)\s*/\s*W16\s+(\d+)", n52["raw"])
    src.update({"cp0679": cp_computed, "bwgate": float(m.group(1)) if m else None})
    my = {name: gold for name, gold, *_ in NUM_ANCHORS}
    rows, all_ok = [], True
    for name, mine in my.items():
        s = src.get(name)
        tol = NUM_TOL if name == "cp0679" else 1e-6
        ok = s is not None and abs(s - mine) / mine < tol
        all_ok = all_ok and ok
        rows.append((name, mine, s, ok))
    for name, mine, s, ok in rows:
        sv = f"{s:g}" if s is not None else "MISSING"
        note = ""
        if name == "cp0679":
            note = f"  (calc.py 实算={cp_computed:.4f}, 差 {abs(cp_computed-mine)/mine*100:.2f}%, 在 10% 容差内)"
        print(f"  [{'OK' if ok else 'DRIFT'}] {name:<9s} 脚本={mine:<8g} 源={sv}{note}")
    print(f"verify_anchors: {'ALL MATCH (复用忠实, 无平行 gold 漂移)' if all_ok else 'DRIFT FOUND (平行 gold 风险!)'}")
    return all_ok


# ---------------- 阈值敏感性分析（判分校准：阈值=判据档位，须核对扰动下是否稳健） ----------------
def sensitivity():
    """量化'三型判别对阈值扰动的稳健性'——回应 §3 标注的理论边界
    (A1/A2 在 C1e 接近 0.5 时的重叠点)。做法：对已知 3 条(gt)三维扫
    TH_A1 × TH_A3 × C1e_th，报告每条样本判定保持正确的阈值体素占比 +
    距默认阈值最近的翻转点。占比越高 = 判别越不靠阈值微调(非过拟合)。
    C1e_th 是 A1↔A2 的真正铰链(A2 要求 C1e≥c1e_th, A1 要求 C≤0.3)，重点扫它。"""
    samples = {n: t for n, t, _ in load_samples()}
    grid_a = [round(0.4 + 0.1 * i, 1) for i in range(7)]   # TH_A1 0.4..1.0
    grid_b = [round(0.4 + 0.1 * i, 1) for i in range(7)]   # TH_A3 0.4..1.0
    grid_c = [0.3, 0.4, 0.5, 0.6, 0.7]                     # C1e_th (A1↔A2 铰链)
    out = {}
    for name, gt in GT.items():
        text = samples[name]
        stable, flips = 0, []
        total = len(grid_a) * len(grid_b) * len(grid_c)
        for ta in grid_a:
            for tb in grid_b:
                for tc in grid_c:
                    r = judge_text(text, th_a1=ta, th_a3=tb, c1e_th=tc)
                    if r["verdict"] == gt or gt in r["verdict"]:
                        stable += 1
                    else:
                        flips.append((abs(ta - TH_A1) + abs(tb - TH_A3)
                                      + abs(tc - 0.5), ta, tb, tc, r["verdict"]))
        frac = stable / total
        nearest = min(flips) if flips else None
        out[name] = {"gt": gt, "stable_frac": round(frac, 3), "nearest_flip": nearest}
        print(f"  {name:<10s} gt={gt:<5s} 稳定占比={frac:.0%} ({stable}/{total}) "
              + (f"最近翻转@TH_A1={nearest[1]}/TH_A3={nearest[2]}/C1e_th={nearest[3]}→{nearest[4]}"
                 if nearest else "全网格稳定"))
    all_ok = all(o["stable_frac"] >= 0.5 for o in out.values())
    print(f"sensitivity: {'ROBUST (已知样本过半阈值体素稳定)' if all_ok else 'FRAGILE (窄稳定区, 阈值敏感)'}")
    return all_ok


# ---------------- main ----------------
GT = {"arm_a[0]": "A1", "arm_a[2]": "A3", "arm_a[1]": "A2"}
# arm_a[1]=A2 为推导型 ground truth: 独立探针已验证(3090 提及 12 次 + 4×3090 构造 0 次
# = A2 定义本身), 非 salvage 实锤, 报告中单独标注。

def main():
    samples = load_samples()
    rows = []
    for name, text, nodes in samples:
        r = judge_text(text)
        r["sample"] = name
        r["cov"] = cov_score(nodes)
        r["gt"] = GT.get(name)
        rows.append(r)
    # 判别准确率（只对已知类型的样本）
    known = [r for r in rows if r["gt"]]
    correct = [r for r in known if r["verdict"] == r["gt"]
               or (r["gt"] in r["verdict"])]
    acc = len(correct) / len(known) if known else None
    print(f"{'sample':12s} {'cov':>5s} {'CORR':>6s} {'C':>5s} {'E':>5s} {'R':>5s} "
          f"{'S':>5s} {'N':>5s} {'P_A1':>5s} {'P_A3':>5s} {'C2BP':>5s}  verdict  gt")
    for r in rows:
        cov = f"{r['cov']:.3f}" if r["cov"] is not None else "NA"
        c2bp = "1" if r["C2BP"] else "0"
        print(f"{r['sample']:12s} {cov:>5s} {r['corr']:6.3f} {r['C']:5.3f} "
              f"{r['E']:5.3f} {r['R_low']:5.3f} {r['S']:5.3f} {r['N']:5.3f} "
              f"{r['P_A1']:5.3f} {r['P_A3']:5.3f} {c2bp:>5s}  {r['verdict']:<12s} {r['gt'] or '-'}")
    print(f"\n判别准确率 (已知 {len(known)} 条: "
          + ", ".join(f"{r['sample']}={r['gt']}→{r['verdict']}" for r in known)
          + f") = {acc:.0%}" if acc is not None else "\n无已知样本")
    json.dump({"weights": {"C": W_C, "E": W_E, "S": W_S, "N": W_N},
               "thresholds": {"A1": TH_A1, "A3": TH_A3},
               "accuracy_known": acc, "rows": rows},
              open(OUT_JSON, "w"), ensure_ascii=False, indent=1)
    print(f"\nJSON → {OUT_JSON}")

if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--verify-anchors" in sys.argv:
        sys.exit(0 if verify_anchors() else 1)
    if "--sensitivity" in sys.argv:
        sys.exit(0 if sensitivity() else 1)
    main()
