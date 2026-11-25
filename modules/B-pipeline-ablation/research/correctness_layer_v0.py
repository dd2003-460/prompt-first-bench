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
    """返回 [(name, text), ...]：T8b 6 条 + S5 1 条（设计 §4 归一化）。"""
    d = json.load(open(T8B_PATH))
    out = []
    for i, a in enumerate(d["arm_a"]):
        out.append((f"arm_a[{i}]", a.get("content", "") + "\n" + a.get("reasoning", "")))
    for i, b in enumerate(d["arm_b"]):
        parts = [b.get("final_content", "") or ""]
        st = b.get("stages", {})
        vals = st.values() if isinstance(st, dict) else st
        for v in vals:
            c = v.get("content", "") if isinstance(v, dict) else (v if isinstance(v, str) else "")
            parts.append(c or "")
        out.append((f"arm_b[{i}]", "\n".join(parts)))
    s5 = json.load(open(S5_PATH))
    out.append(("S5", "\n".join(n.get("claim", "") for n in s5["nodes"])))
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
    """R_low: 配置被评估过(E1>0)时, 强推荐行是否含 4×3090。被选中→0, 垫底→1; 未评估→0.5。"""
    if e1_rows == 0:
        return 0.5, {"strong_rec_lines": 0, "note": "E1=0, R 未定义, 中性 0.5"}
    rec_lines = [ln for ln in text.split("\n") if STRONG_REC.search(ln)]
    picked = any(CFG4.search(ln) for ln in rec_lines)
    r_low = 0.0 if picked else 1.0
    return r_low, {"strong_rec_lines": len(rec_lines), "winner_in_strong_rec": picked}


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

def judge_text(text):
    c, c_d = axis_c(text)
    e, e_d = axis_e(text)
    r, r_d = axis_r(text, e_d["e1_rows"])
    s, s_d = axis_s(text)
    n, n_d = axis_n(text)
    corr = W_C * c + W_E * e + W_S * s + W_N * n
    p_a1 = 1.0 - c
    p_a3 = e_d["e1"] * r
    if p_a1 >= TH_A1 and p_a3 >= TH_A3:
        verdict = "A1+A3"
    elif p_a1 >= TH_A1:
        verdict = "A1"
    elif p_a3 >= TH_A3:
        verdict = "A3"
    else:
        verdict = "indeterminate"
    return {"corr": round(corr, 3), "C": round(c, 3), "E": round(e, 3),
            "R_low": round(r, 3), "S": round(s, 3), "N": round(n, 3),
            "P_A1": round(p_a1, 3), "P_A3": round(p_a3, 3), "verdict": verdict,
            "detail": {"C": c_d, "E": e_d, "R": r_d, "S": s_d, "N": n_d}}


# ---------------- cov 对照轴（judge_v1 口径, 可选 bge-m3） ----------------
COS_THRESHOLD = 0.70  # 同 judge_v1.py 标定值（frozen, 只读引用）
_cov_model = None
_cov_gold = None

def cov_score(text):
    """judge_v1 口径: 句子级 bge-m3 top-1 cosine vs 36 gold units, >=0.70 计命中。
    无 bge-m3 时返回 None（dry-run 表标 NA）。"""
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
    chunks = [text[i:i + 512] for i in range(0, len(text), 512)]
    emb = _cov_model.encode(chunks, normalize_embeddings=True)
    sim = emb @ gold_emb.T
    top1 = sim.argmax(axis=1)
    top1_sim = sim[np.arange(len(emb)), top1]
    matched = set(int(j) for j in top1[top1_sim >= COS_THRESHOLD])
    return round(len(matched) / len(units), 3)


# ---------------- main ----------------
GT = {"arm_a[0]": "A1", "arm_a[2]": "A3"}  # salvage 已验证的 ground truth

def main():
    samples = load_samples()
    rows = []
    for name, text in samples:
        r = judge_text(text)
        r["sample"] = name
        r["cov"] = cov_score(text)
        r["gt"] = GT.get(name)
        rows.append(r)
    # 判别准确率（只对已知类型的样本）
    known = [r for r in rows if r["gt"]]
    correct = [r for r in known if r["verdict"] == r["gt"]
               or (r["gt"] in r["verdict"])]
    acc = len(correct) / len(known) if known else None
    print(f"{'sample':12s} {'cov':>5s} {'CORR':>6s} {'C':>5s} {'E':>5s} {'R':>5s} "
          f"{'S':>5s} {'N':>5s} {'P_A1':>5s} {'P_A3':>5s}  verdict  gt")
    for r in rows:
        cov = f"{r['cov']:.3f}" if r["cov"] is not None else "NA"
        print(f"{r['sample']:12s} {cov:>5s} {r['corr']:>6.3f} {r['C']:>5.3f} "
              f"{r['E']:>5.3f} {r['R_low']:>5.3f} {r['S']:>5.3f} {r['N']:>5.3f} "
              f"{r['P_A1']:>5.3f} {r['P_A3']:>5.3f}  {r['verdict']:<12s} {r['gt'] or '-'}")
    print(f"\n判别准确率 (已知 {len(known)} 条: "
          + ", ".join(f"{r['sample']}={r['gt']}→{r['verdict']}" for r in known)
          + f") = {acc:.0%}" if acc is not None else "\n无已知样本")
    json.dump({"weights": {"C": W_C, "E": W_E, "S": W_S, "N": W_N},
               "thresholds": {"A1": TH_A1, "A3": TH_A3},
               "accuracy_known": acc, "rows": rows},
              open(OUT_JSON, "w"), ensure_ascii=False, indent=1)
    print(f"\nJSON → {OUT_JSON}")

if __name__ == "__main__":
    main()
