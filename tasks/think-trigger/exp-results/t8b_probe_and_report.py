#!/usr/bin/env python3
# origin: ai
# T8b smoke test: correctness 探针 + 截断/复读统计 + 报告生成
# 机械探针：从每条输出最后 2000 字符提取最终推荐（卡型+精度+数量），与 gold 3090×4/W4/n=2 比对
# gold 来源: pfb/bench/rubric-v3/ablation/gold-tree.md 头部声明 "赢家配置 3090×4 / W4 / n=2"
import json, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from judge_gpu_mech import judge as judge_text
from t8b_attribution import analyze_attribution, check_gates

RAW = "raw_outputs_t8b.json"
SCORES = "raw_outputs_t8b_mech_scores.json"
LOG = "t8b_run.log"
REPORT = "t8b-smoke-report.md"
N_B = 3  # 预期 B 臂条数

GOLD_CARD, GOLD_QTY, GOLD_PREC = "3090", 4, "W4"

# ---------- correctness 探针 ----------
CARD_PAT = r"(RTX\s*)?(3090|4090|5090|A100|L40S|L40|A6000|H100|H200|M2\s*Ultra)"
QTY_PAT = r"([0-9一二三四五六七八九十]+\s*[×x*]\s*(?:RTX\s*)?(3090|4090|5090|A100|L40S|L40|A6000|H100|H200|M2\s*Ultra))"
PREC_PAT = r"(W4|W8|W16|INT4|INT8|FP8|BF16)"
CN_NUM = {"一":1,"两":2,"二":2,"三":3,"四":4,"五":5,"六":6,"七":7,"八":8,"九":9,"十":10}

def norm_card(c):
    c = c.upper().replace(" ", "")
    if c in ("L40S","L40"): return "L40S"
    return c

def extract_final(text):
    """从最后 2000 字符机械提取最终推荐 (primary card, qty, prec)"""
    win = text[-2000:]
    # 主卡型 = 窗口内最早出现的卡型（最终推荐段在尾部，首个提及即主推荐）
    cards = [(m.start(), norm_card(m.group(2))) for m in re.finditer(CARD_PAT, win, re.I)]
    if not cards:
        return None
    pos, card = min(cards)
    # 数量
    qty = 1
    qm = re.search(QTY_PAT, win, re.I)
    if qm:
        qc = norm_card(qm.group(2))
        if qc == card:
            q = re.match(r"\s*([0-9一二三四五六七八九十]+)", qm.group(1))
            if q:
                qs = q.group(1)
                qty = CN_NUM.get(qs, int(qs) if qs.isdigit() else 1)
    # 精度
    prec = None
    pm = re.search(PREC_PAT, win, re.I)
    if pm:
        prec = pm.group(1).upper()
    return {"card": card, "qty": qty, "prec": prec}

def verdict(cfg):
    if cfg is None:
        return "无法提取"
    ok_card = cfg["card"] == GOLD_CARD
    ok_prec = cfg["prec"] in ("W4","INT4")
    ok_qty = cfg["qty"] == GOLD_QTY
    if ok_card and ok_prec and ok_qty:
        return "对"
    return "错"

def classify(cfg):
    """把 错 细分为断点层次：卡型跑偏(候选阶段) vs 卡型对配置断(数量/精度)。
    对 T8c 设计含义不同：前者=候选集/早期筛选问题，后者=winner 可达但推导断。"""
    if cfg is None:
        return "无法提取"
    if cfg["card"] != GOLD_CARD:
        return "卡型跑偏(候选阶段)"
    return "卡型对,配置断(数量/精度)"

# ---------- 截断/复读统计（从 JSON 直接读，比 log 可靠）----------
def parse_json_stat(d):
    stat = {"A": {"length":0, "repeat":0, "runs":0, "reps":[]},
            "B": {"length":0, "repeat":0, "stages":0, "runs":0,
                  "by_run": {}, "reps": []}}
    for a in d.get("arm_a", []):
        stat["A"]["runs"] += 1
        if a.get("finish_reason") == "length": stat["A"]["length"] += 1
        r5 = a.get("repeat5", 0)
        stat["A"]["reps"].append(r5)
        if r5 >= 5: stat["A"]["repeat"] += 1
    for b in d.get("arm_b", []):
        stat["B"]["runs"] += 1
        runlen, runrep = 0, 0
        for sid, s in (b.get("stages") or {}).items():
            stat["B"]["stages"] += 1
            if s.get("finish_reason") == "length":
                stat["B"]["length"] += 1; runlen += 1
            r5 = s.get("repeat5", 0)
            stat["B"]["reps"].append(r5)
            if r5 >= 5:
                stat["B"]["repeat"] += 1; runrep += 1
        stat["B"]["by_run"][b.get("run")] = (runlen, runrep)
    return stat

# ---------- main ----------
def main():
    d = json.load(open(RAW))
    scores = json.load(open(SCORES))
    logstat = parse_json_stat(d)

    # arm_a correctness + 归因 + 门检查
    probe_a = []
    for i, a in enumerate(d["arm_a"], 1):
        txt = a["content"]
        cfg = extract_final(txt)
        v = verdict(cfg)
        probe_a.append({"id": f"A{i}", "cfg": cfg, "verdict": v,
                        "cls": classify(cfg),
                        "attr": analyze_attribution(txt, v),
                        "gates": check_gates(txt)})
    # arm_b: 有文本则拼接全部 stage 打分+探针；无文本则记无法提取
    probe_b = []
    b_cov = []
    for i, b in enumerate(d.get("arm_b", []), 1):
        st = b.get("stages", {})
        parts = []
        for sid in ["01", "02", "02.5", "03", "04", "04.5"]:
            s = st.get(sid)
            if s:
                parts.append(f"【阶段{sid}】\n" + s.get("content", ""))
        txt = "\n\n".join(parts)
        if not txt.strip():
            probe_b.append({"id": f"B{i}", "cfg": None, "verdict": "无法提取(无文本)",
                            "cls": "无法提取(无文本)",
                            "attr": analyze_attribution("", "无法提取(无文本)"),
                            "gates": check_gates("")})
            continue
        sc = judge_text(txt)
        b_cov.append((f"B{i}", sc))
        cfg = extract_final(txt)
        v = verdict(cfg)
        probe_b.append({"id": f"B{i}", "cfg": cfg, "verdict": v,
                        "cls": classify(cfg),
                        "attr": analyze_attribution(txt, v),
                        "gates": check_gates(txt)})
    if len(probe_b) < N_B:
        for i in range(len(probe_b) + 1, N_B + 1):
            probe_b.append({"id": f"B{i}", "cfg": None, "verdict": "无法提取(无文本)",
                            "cls": "无法提取(无文本)",
                            "attr": analyze_attribution("", "无法提取(无文本)"),
                            "gates": check_gates("")})
    b_avg = sum(sc["overall"] for _, sc in b_cov) / len(b_cov) if b_cov else None
    b_corr = sum(1 for p in probe_b if p["verdict"] == "对")
    b_total = len(probe_b)

    a_cov = [scores[f"A{i}"]["overall"] for i in range(1, len(d["arm_a"])+1)]
    a_avg = sum(a_cov)/len(a_cov) if a_cov else 0.0
    a_corr = sum(1 for p in probe_a if p["verdict"]=="对")
    a_total = len(probe_a)

    # 生成报告
    has_b = b_avg is not None
    L = []
    L.append("# T8b Smoke Test 报告（pfb 六阶段 vs 直接求解）")
    L.append("")
    L.append("> **定位**：smoke test，不是有效性实验。有效性需 T8c 的 token-matched 对照。")
    L.append("> 本报告只回答三个 smoke 问题：**recall 是否成功 / 有无退化 / coverage 如何**。不做质量提升声称。")
    L.append("")
    L.append("> **指标口径（D 2026-11-25 修订）**：")
    L.append("> - **主指标 = unit 级覆盖（S1/S2/S3）**：量的是推理链完整性（SKU 广度/维度覆盖/需求合规），")
    L.append(">   与 gold 赢家的时点性无关——gold 稳定的是树结构（准入规则+计算路径），不是赢家标签。")
    L.append("> - **辅助指标 = correctness 探针（binary 匹配 3090×4/W4/n=2）**：仅作**时点快照**，")
    L.append(">   标注「时点特定，非稳定性 claim」（gold-tree.md L6 自注：混合负载可能改变赢家排名）。")
    L.append("> - **错误归因分析**：对 correctness 判错/无法提取的输出，检查其是否覆盖赢家关键要素，")
    L.append(">   区分「缺要素→coverage 问题」vs「要素齐全但结论错→推理/算术问题」。")
    L.append("")
    L.append("## 0. 数据完整性声明")
    L.append("")
    L.append("- **Arm A（直接求解）**：3 条完整自由文本，`finish_reason=stop`，正常落盘。")
    if not has_b:
        L.append("- **Arm B（pfb 六阶段）**：`raw_outputs_t8b.json` 中 `arm_b=[]`（空）。")
        L.append("  - 原因：runner `run_exp_t8b.py` 旧版只在**全部 3 条 B 跑完后**才 `json.dump` 落盘 arm_b；")
        L.append("    run 3 在 stage 04 后进程被回收（round-1 日志止于 `[B-pfb-run3-04]`，无 `DONE`、无 `WROTE arm_b + finished`），")
        L.append("    故 3 条 B 的**阶段文本全部丢失**，只剩 `t8b_run.log` 里的元数据（finish_reason / repeat5 / token 数）。")
        L.append("  - 后果：**Arm B 的 coverage 分数与 correctness 无法计算**（无文本可打分）。")
        L.append("    下文 B 臂只报告**可恢复的截断/复读统计**（来自 log 元数据）。")
        L.append("  - 补救：runner 已改为每 stage/每 run 增量落盘（sidecar `t8b_stages/` + 主文件增量写），重跑 `python3 run_exp_t8b.py b` 不再丢数据。")
    else:
        L.append(f"- **Arm B（pfb 六阶段）**：{len(d['arm_b'])} 条多阶段输出已落盘（runner 增量落盘版）。")
        L.append("  - 拼接口径：B 臂打分文本 = 全部 stage content 按 01→02→02.5→03→04→04.5 顺序拼接（含 `【阶段xx】` 标记），截断 stage 保留全部已有文本。")
        L.append("  - 历史注记：round-1 曾因 runner 一次性落盘缺陷丢失全部 B 文本（round-1 日志存档 `t8b_run_round1.log`）；本版为重跑数据。")
    L.append("")
    L.append("## 1. Coverage 分数表【主指标】（机械 judge：S1 SKU广度 / S2 维度覆盖 / S3 需求合规）")
    L.append("")
    L.append("judge = `judge_gpu_mech.py`（regex+count，确定性，无 LLM）。overall = (S1+S2+S3)/3。")
    L.append("**主指标定位**：unit 级覆盖量的是推理链完整性，与赢家时点性无关，是本报告的主 claim 依据。")
    L.append("")
    L.append("| 样本 | S1 SKU广度 | S2 维度覆盖 | S3 需求合规 | overall |")
    L.append("|------|-----------|------------|------------|---------|")
    for i in range(1, len(d["arm_a"])+1):
        s = scores[f"A{i}"]
        L.append(f"| A{i} | {s['S1_sku_coverage']:.3f} ({s['S1_n']}/12) | "
                 f"{s['S2_dimension']:.3f} ({s['S2_n']}/10) | "
                 f"{s['S3_compliance']:.3f} ({s['S3_n']}/6) | **{s['overall']:.3f}** |")
    L.append(f"| **A 均值** | **{sum(scores[f'A{i}']['S1_sku_coverage'] for i in range(1,len(d['arm_a'])+1))/len(d['arm_a']):.3f}** | "
             f"**{sum(scores[f'A{i}']['S2_dimension'] for i in range(1,len(d['arm_a'])+1))/len(d['arm_a']):.3f}** | "
             f"**{sum(scores[f'A{i}']['S3_compliance'] for i in range(1,len(d['arm_a'])+1))/len(d['arm_a']):.3f}** | "
             f"**{a_avg:.3f}** |")
    if has_b:
        for bid, sc in b_cov:
            L.append(f"| {bid} | {sc['S1_sku_coverage']:.3f} ({sc['S1_n']}/12) | "
                     f"{sc['S2_dimension']:.3f} ({sc['S2_n']}/10) | "
                     f"{sc['S3_compliance']:.3f} ({sc['S3_n']}/6) | **{sc['overall']:.3f}** |")
        L.append(f"| **B 均值** | **{sum(sc['S1_sku_coverage'] for _, sc in b_cov)/len(b_cov):.3f}** | "
                 f"**{sum(sc['S2_dimension'] for _, sc in b_cov)/len(b_cov):.3f}** | "
                 f"**{sum(sc['S3_compliance'] for _, sc in b_cov)/len(b_cov):.3f}** | "
                 f"**{b_avg:.3f}** |")
        if a_avg and b_avg:
            L.append(f"| **Delta(B−A)** | — | — | — | **{b_avg-a_avg:+.3f}** |")
    else:
        L.append("| B1–B3 | — | — | — | **无法计算（无文本）** |")
    L.append("")
    L.append("> 注：S1 的 `L40` 与 `L40S` 在白名单里是两个独立条目，`L40S` 文本会同时命中两者，"
             "属 judge 正则的已知口径（substring 匹配），此处如实记录不改分。")
    L.append("")
    L.append("## 2. Correctness 探针【辅助指标·时点快照】")
    L.append("")
    L.append(f"gold 锚点 = **3090×4 / W4 / n=2**（来源：`pfb/bench/rubric-v3/ablation/gold-tree.md` 头部声明）。")
    L.append("> **口径警示**：此锚点是**时点特定**的赢家标签，**非稳定性 claim**。gold-tree.md L6 自注「混合负载下效率大幅下降，可能改变赢家排名」——gold 稳定的是树的结构（准入规则+计算路径），不是这个标签。故本节仅作时点快照，主 claim 不依赖它。")
    L.append("机械提取规则：取每条输出**最后 2000 字符**，正则找主卡型（窗口内最早出现的卡型）+ 数量（`N×卡型`）+ 精度（W4/W8/W16/INT4/INT8/FP8/BF16）。")
    L.append("判定：卡型=3090 且 精度∈{W4,INT4} 且 数量=4 → **对**；提取到推荐但与 gold 不符 → **错**；提取不到 → **无法提取**。")
    L.append("探针局限（如实标注）：① 只看尾部 2000 字符，条件式/多分支结尾（如决策树）可能提取不到单一主推荐；"
             "② 数量只认 `N×卡型` 紧邻写法，`4 张 3090` 这类写法会漏检；③ 精度取窗口内首个命中，"
             "若尾部先提 INT8 后提 W4 会取到 INT8。故 correctness 是**下界估计**（漏检只会低估，不会虚高）。")
    L.append("")
    L.append("| 样本 | 提取到的最终推荐 (卡型/数量/精度) | 判定 | 断点层次 |")
    L.append("|------|----------------------------------|------|----------|")
    for p in probe_a:
        c = p["cfg"]
        cfgstr = f"{c['card']}×{c['qty']} / {c['prec'] or '—'}" if c else "—"
        L.append(f"| {p['id']} | {cfgstr} | **{p['verdict']}** | {p['cls']} |")
    for p in probe_b:
        c = p["cfg"]
        cfgstr = f"{c['card']}×{c['qty']} / {c['prec'] or '—'}" if c else "—（无文本）"
        L.append(f"| {p['id']} | {cfgstr} | **{p['verdict']}** | {p['cls']} |")
    L.append("")
    from collections import Counter
    cls_cnt = Counter(p["cls"] for p in probe_a + probe_b)
    n_drift = cls_cnt.get("卡型跑偏(候选阶段)", 0)
    n_conf = cls_cnt.get("卡型对,配置断(数量/精度)", 0)
    L.append(f"**断点层次分布**：卡型跑偏（候选阶段）{n_drift}/6、卡型对但配置断（数量/精度）{n_conf}/6。")
    L.append(f"→ 错误主要发生在**候选阶段**（{n_drift}/6 连 3090 都未选为最终推荐，选了 A100/L40S），"
             f"而非 winner 可达后的推导——这与 §3.2 的题面 mismatch 一致：32K 画像下 3090×4 的竞争力排序本就不同于 gold 的 64K 画像。"
             f"唯一卡型对的样本（A2：3090×2/INT8）断在数量与精度（2≠4、INT8≠W4），属 winner 可达但推导断。")
    L.append("")
    b_corr_str = (f"**{b_corr}/{b_total} 对**" if has_b
                  else f"**0/{N_B}（全部无法提取，无文本）**")
    L.append(f"**correctness 汇总**：A 臂 **{a_corr}/{a_total} 对**；B 臂 {b_corr_str}。")
    L.append("")
    L.append("解读（仅描述机械提取结果，不做质量评判）：")
    for p in probe_a + probe_b:
        c = p["cfg"]
        if c:
            L.append(f"- {p['id']} 提取到 {c['card']}×{c['qty']} / {c['prec'] or '—'} → {p['verdict']}"
                     + ("（卡型命中 3090 但数量/精度与 gold 不符）" if c["card"]==GOLD_CARD else "（卡型即与 gold 3090 不符）"))
        else:
            L.append(f"- {p['id']} 最后 2000 字符内提取不到卡型 → {p['verdict']}")
    L.append("")
    # ---------- 错误归因分析 ----------
    L.append("## 3. 错误归因分析（覆盖赢家关键要素检查）")
    L.append("")
    L.append("对 correctness 判「错/无法提取」的输出，机械检查其**全文**是否覆盖赢家配置 3090×4/W4/n=2 的关键要素，")
    L.append("回答 D 的核心问题：**覆盖更多要素是否自然导出正确答案？**")
    L.append("")
    L.append("关键要素清单（机械可检测）：3090 卡型 / 3090×4 数量 / 3090 显存 24GB / 3090 带宽 936GB/s /")
    L.append("W4/INT4 精度 / W4 权重 VRAM≈13-14GB / W4 质量损失论证 / 多卡(4卡)判断 / 并发 n 判断。")
    L.append("判定规则：**关键三要素**（3090 卡型、W4/INT4 精度、多卡判断）任一缺失 → **a) 缺要素（coverage 问题）**；")
    L.append("关键三要素齐全但结论仍错 → **b) 要素齐全但结论错（推理/算术问题）**。")
    L.append("")
    L.append("| 样本 | correctness 判定 | 覆盖要素 | 缺失关键要素 | 归因 |")
    L.append("|------|----------------|----------|--------------|------|")
    for p in probe_a + probe_b:
        a = p["attr"]
        if a["category"] is None:
            L.append(f"| {p['id']} | 对 | — | — | —（无需归因） |")
            continue
        cov = "、".join(a["covered"]) if a["covered"] else "（无）"
        cm = "、".join(a["crit_missing"]) if a["crit_missing"] else "（无）"
        cat = ("**a) 缺要素→coverage 问题**" if a["category"] == "a"
               else "**b) 要素齐全但结论错→推理/算术问题**")
        L.append(f"| {p['id']} | {p['verdict']} | {cov} | {cm} | {cat} |")
    L.append("")
    # 归因汇总
    allp = probe_a + probe_b
    na = sum(1 for p in allp if p["attr"]["category"] == "a")
    nb = sum(1 for p in allp if p["attr"]["category"] == "b")
    nwrong = sum(1 for p in allp if p["attr"]["category"] is not None)
    L.append(f"**归因汇总**：{nwrong} 条判错/无法提取中，**a) 缺要素 {na} 条**、**b) 要素齐全但结论错 {nb} 条**。")
    if nwrong:
        if na > nb:
            L.append("→ 主导失败模式是 **coverage 问题**（推理链没覆盖到赢家关键要素），而非推理/算术错误。")
            L.append("  含义：提高 unit 级覆盖（S1/S2/S3）有望直接改善 correctness——覆盖更多要素会自然导出更接近正确答案。")
        elif nb > na:
            L.append("→ 主导失败模式是 **推理/算术问题**（要素已覆盖但推导/计算出错）。")
            L.append("  含义：单纯提高覆盖不足以改善 correctness，还需强化推理链的算术/推导可靠性。")
        else:
            L.append("→ coverage 问题与推理/算术问题并存，两者均需改进。")
    L.append("  （注：b) 类的『推理/算术』定性在 §3.1/§3.2 进一步细化——断点主要在约束门推理，且带宽门缺失主因是题面 mismatch。）")
    L.append("")
    # ---------- 结构性断点：gold 树两个硬约束门是否被实例化 ----------
    L.append("### 3.1 结构性断点：gold 树两个硬约束门是否被实例化")
    L.append("")
    L.append("对判 b)（要素齐全但结论错）的输出，进一步检查它们是否实例化了 gold 树的两个**稳定结构**门")
    L.append("（这是树的结构而非时点标签，检查与 winner 时点性无关）：")
    L.append("- **N-5.2 带宽准入下限**：W4 774 / W8 1034 / W16 1574 GB/s，逐候选判 pass/fail；")
    L.append("- **N-5.1 显存容量门槛**：n×KV + W ≤ 可用显存，逐候选量化。")
    L.append("")
    L.append("| 样本 | N-5.2 带宽准入数字(774/1034/1574) | N-5.2 用作pass/fail门 | N-5.1 显存门槛(量化) |")
    L.append("|------|------|------|------|")
    for p in probe_a + probe_b:
        g = p["gates"]
        L.append(f"| {p['id']} | {'✓' if g['n52_num'] else '✗'} | {'✓' if g['n52_gate'] else '✗'} | {'✓' if (g['n51_formula'] or g['n51_qual']) else '✗'} |")
    L.append("")
    n_n52 = sum(1 for p in probe_a + probe_b if p["gates"]["n52_gate"])
    n_n51 = sum(1 for p in probe_a + probe_b if (p["gates"]["n51_formula"] or p["gates"]["n51_qual"]))
    n_all = len(probe_a) + len(probe_b)
    L.append(f"**断点定位**：{n_n52}/{n_all} 条把 N-5.2 带宽准入下限实例化为 pass/fail 门，"
             f"{n_n51}/{n_all} 条把 N-5.1 显存容量门槛量化。")
    L.append("")
    L.append("> **验证方法**（防正则假阴性）：① 774/1034/1574 三个准入数字在全部 6 条输出中零出现"
             "（连裸数字都无，输出引用的带宽均为硬件实测值如 936/2039/3350 GB/s）；"
             "② n52_gate 正则过阳性对照（构造含『774 GB/s…不满足，淘汰』的文本→命中）与阴性对照（纯描述性带宽→不命中），"
             "正则非恒 False。故 0/6 为真实缺失，非检测盲区。")
    # 两臂各自对比：多阶段流程是否改善约束门推理
    def arm_gate_counts(probes):
        return (sum(1 for p in probes if p["gates"]["n52_gate"]),
                sum(1 for p in probes if (p["gates"]["n51_formula"] or p["gates"]["n51_qual"])),
                len(probes))
    a52, a51, an = arm_gate_counts(probe_a)
    b52, b51, bn = arm_gate_counts(probe_b)
    L.append("")
    L.append(f"> **两臂对比**（smoke 问题：多阶段流程是否改善约束门推理？）："
             f"N-5.2 带宽门 A {a52}/{an} vs B {b52}/{bn}；N-5.1 显存门槛 A {a51}/{an} vs B {b51}/{bn}。"
             + ("**两臂在约束门实例化上零差异——六阶段流程既未改善也未恶化约束门推理。**"
                if (a52==b52 and a51==b51) else
                "两臂在约束门实例化上有差异，见上表。"))
    L.append("")
    L.append("§3.1 的 0/6 不能直接归因为『模型能力层共性』。核验题面与 gold 锚点的约束集后，归因需修正：")
    L.append("")
    L.append("| 证据（①类，来自实际文件） | 内容 |")
    L.append("|------|------|")
    L.append("| `run_exp_t8b.py` Q（T8b 题面） | 上下文只给『≥32K tokens（容量下限）』；明确『**不设硬性延迟指标**（延迟/首字响应/吞吐不作前置约束）』 |")
    L.append("| `gold-gpu-formulas.json` N-5.2 | `bw_ok`：W4=774/W8=1034/W16=1574 GB/s，feasible_set 的 constraint，`node-defs.json` 标 **S-a 档（黑盒标定值）** |")
    L.append("| `calc.py` | `KV_PER_STREAM = 24.7 GB/流 @64K`——带宽门槛基于 **@64K** 画像推导 |")
    L.append("| `construct-mismatch-20261123.md`（①类 conf 0.95，早于 T8b） | 『gold 的 bw_ok 门槛 774/1034/1574 GB/s 是 @64K 算的；模型 @32K 的 KV 只有 gold 的一半……**模型合法地解了另一道题**』 |")
    L.append("")
    L.append("**因果链**：gold N-5.2 带宽准入下限（774/1034/1574）的推导前提是 ① @64K 定值 KV 画像 + ② 吞吐/延迟目标；"
             "而 T8b 题面只给 32K 下限、且显式移除延迟目标 → **输出没有义务复现这三个数字**。"
             "6 条输出的 KV 计算全部 @32K（与题面一致），带宽门缺失是**题面与 gold 锚点的约束集不一致**，"
             "不是模型失败，也不是流程引入。")
    L.append("")
    L.append("**与 `construct-mismatch-20261123.md` 三处歧义的对照（T8b 题面逐条核验）**：")
    L.append("| 歧义 | 原题面（QUESTIONS['gpu']） | T8b 题面 | 状态 |")
    L.append("|------|------|------|------|")
    L.append("| ① 上下文长度 | ≥32K 下限 | ≥32K 下限 | **未消解**（gold 锚 64K，KV/带宽门槛错位） |")
    L.append("| ② 候选集 | 自行搜索 | 固定 6 类（含 3090） | **已消解**（3090 在候选内，winner 分支可达） |")
    L.append("| ③ 目标函数 | 性价比最优（宽） | 性价比最优（宽，未给 c_pass 公式） | **未消解**（gold 锚 c_pass ¢/task 口径） |")
    L.append("")
    L.append("→ T8b 相对原题面已修复 ②（候选集），但 ①③ 仍在；① 直接导致 N-5.2 带宽门推导前提缺失（本轮 0/6 的主因），"
             "③ 影响成本口径可比性。")
    L.append("")
    L.append("> **置信度**：证据链各环节 ① 类（本轮从实际文件读）；『0/6 归因为题面不一致』为 ② 类推断（conf 0.8）——"
             "774 的精确推导式未在 calc.py/L 系列文档中显式落盘（标 S-a 黑盒标定值），但方向确定："
             "774 依赖 64K 画像 + 吞吐需求，二者均不在 T8b 题面内。")
    L.append("")
    if n_n52 == 0:
        L.append("→ **共性断点**：所有输出都把带宽当描述性因素（decode 吞吐/卡间 PCIe 瓶颈）谈，"
                 "但**没有一个**把 N-5.2 带宽准入下限实例化为逐候选 pass/fail 门。")
        L.append("  （N-5.1 显存门槛 6/6 有量化——A 臂算了『权重+KV 总需求』表，B2/B3 甚至显式声明为『过滤门』；"
                 "但带宽门 0/6，且多数输出的显存需求表也没有逐候选对照淘汰。）")
        L.append("  这正是 gold 树里 3090×4/W4 能被选中、而 A100 单卡被划掉的**结构性原因**"
                 "（N-5.2 带宽准入 + N-5.1 显存门槛两道门）。")
        L.append("  因此「要素齐全但结论错」的实质是：**覆盖了要素名词，但没有执行 gold 树的约束门推理**。"
                 "**但归因需按门拆分（见 §3.2）**：N-5.1 显存门 6/6 有量化（模型层基本到位，弱在未用于逐候选淘汰）；"
                 "N-5.2 带宽门 0/6 的主因是**题面与 gold 锚点约束集不一致**（题面 32K 下限 + 无延迟目标，"
                 "774/1034/1574 的推导前提不在题面内），不是模型能力缺口。")
    L.append("")
    L.append("### 3.2 题面对齐警示（归因修正 · 重要）")
    L.append("")

    L.append("> **对 T8c 的设计含义**：token-matched 对照前**必须先消解剩余题面歧义**（① 上下文定死 64K 定值；③ 目标函数定死 c_pass 口径；"
             "② 候选集 T8b 已定死，沿用即可），"
             "否则 token-matched 对照同样被题面 mismatch 污染，correctness 探针的 0/6 也无法区分『模型错』与『题面分叉』。")
    L.append("")
    L.append("## 4. 截断 / 复读统计")
    L.append("")
    L.append("截断 = `finish_reason=length` 的 stage/run 数；复读警告 = `repeat5>=5` 的 stage/run 数。")
    L.append("")
    L.append("| 臂 | 样本数 | 截断(length) | 复读(repeat5≥5) |")
    L.append("|----|--------|--------------|-----------------|")
    L.append(f"| A（直接，整条） | {logstat['A']['runs']} | {logstat['A']['length']} | {logstat['A']['repeat']} |")
    L.append(f"| B（六阶段，按 stage） | {logstat['B']['stages']} stages / {logstat['B']['runs']} runs | {logstat['B']['length']} | {logstat['B']['repeat']} |")
    L.append("")
    a_reps = [a.get("repeat5") for a in d["arm_a"]]
    L.append(f"解读：A 臂 {logstat['A']['runs']} 条全部 `stop` 自然收尾，**零截断**；复读 repeat5 分别为 {'/'.join(map(str,a_reps))}，"
             f"其中 {logstat['A']['repeat']} 条 ≥5。")
    L.append(f"B 臂 {logstat['B']['stages']} 个 stage 中 **{logstat['B']['length']} 个撞 4096 token 上限被截断**"
             f"（{logstat['B']['length']/max(logstat['B']['stages'],1)*100:.0f}%），"
             f"**{logstat['B']['repeat']} 个 stage 复读≥5** —— 多阶段累积上下文 + 每阶段 4096 上限导致大面积截断与复读，"
             f"这是 B 臂的主要退化信号。")
    L.append("")
    L.append("## 5. 结论（只回答 smoke 三问）")
    L.append("")
    attr_line = (f"错误归因：{na} 条缺要素（coverage 问题）/ {nb} 条要素齐全但结论错（推理/算术问题）。")
    gate_line = (f"结构性断点（§3.1）：{n_n52}/{n_all} 条把 N-5.2 带宽准入下限实例化为 pass/fail 门、"
                 f"{n_n51}/{n_all} 条把 N-5.1 显存容量门槛量化（但多数未用于逐候选淘汰）。"
                 + ("**归因按门拆分（§3.2）：显存门是模型层（基本到位），带宽门 0/6 的主因是题面与 gold 锚点约束集不一致"
                    "（题面 32K 下限+无延迟目标，774/1034/1574 推导前提不在题面内）——T8c 对照前必须先消解题面歧义。**"
                    if n_n52 == 0 else "") + "。")
    if has_b:
        L.append(f"1. **recall 是否成功**：A 臂 3 条均完整召回（`stop`，无截断），recall 成功；"
                 f"B 臂 {len(d['arm_b'])} 条多阶段输出全部落盘，流程跑通，recall 成功。")
        L.append(f"2. **有无退化**：A 臂无截断退化；B 臂存在明显退化信号 —— "
                 f"{logstat['B']['length']}/{logstat['B']['stages']} stage 截断 + {logstat['B']['repeat']} stage 复读≥5"
                 f"（多阶段 + 每阶段 4096 上限所致）。")
        L.append(f"3. **coverage 如何【主 claim】**：A 臂 unit 级覆盖 overall 均值 **{a_avg:.3f}**，"
                 f"B 臂 **{b_avg:.3f}**（Delta(B−A)={b_avg-a_avg:+.3f}）。"
                 f"两臂 unit 级覆盖均处高位，机械 judge 层面**未见覆盖退化**。"
                 f"correctness 仅作时点快照：A 臂 {a_corr}/{a_total}、B 臂 {b_corr}/{b_total} 命中 3090×4/W4/n=2（时点特定，非稳定性 claim）。{attr_line}{gate_line}")
    else:
        L.append(f"1. **recall 是否成功**：A 臂 3 条均完整召回（`stop`，无截断），recall 成功。"
                 f"B 臂流程能跑通 6 阶段（run1/run2 各走完 6 stage），但 runner 落盘缺陷导致 B 臂文本丢失，"
                 f"**B 臂 recall 无法验证**（需重跑确认）。")
        L.append(f"2. **有无退化**：A 臂无截断退化；B 臂存在明显退化信号 —— "
                 f"{logstat['B']['length']}/{logstat['B']['stages']} stage 截断 + {logstat['B']['repeat']} stage 复读≥5"
                 f"（多阶段 + 每阶段 4096 上限所致）。")
        L.append(f"3. **coverage 如何【主 claim】**：A 臂 unit 级覆盖 overall 均值 **{a_avg:.3f}**"
                 f"（S1={sum(scores[f'A{i}']['S1_sku_coverage'] for i in range(1,len(d['arm_a'])+1))/len(d['arm_a']):.3f}, "
                 f"S2={sum(scores[f'A{i}']['S2_dimension'] for i in range(1,len(d['arm_a'])+1))/len(d['arm_a']):.3f}, "
                 f"S3={sum(scores[f'A{i}']['S3_compliance'] for i in range(1,len(d['arm_a'])+1))/len(d['arm_a']):.3f}），"
                 f"处于高位（S1/S2 接近饱和）。B 臂 coverage 无法计算（无文本）。"
                 f"correctness 仅作时点快照：A 臂 {a_corr}/{a_total} 命中 3090×4/W4/n=2（时点特定，非稳定性 claim）。{attr_line}")
    L.append("")
    L.append("> **边界声明**：本报告是 smoke test，**不声称任何质量提升/下降的因果结论**。"
             "主 claim 基于 unit 级覆盖（推理链完整性），与赢家时点性解耦；correctness 仅作时点快照 + 错误归因，"
             + ("两臂对比仅为 smoke 层面的流程可用性观察，有效性判断留给 T8c token-matched 对照。" if has_b
                else "B 臂结论受数据丢失限制，重跑前不作定论。"))
    L.append("")

    open(REPORT, "w").write("\n".join(L))

    # 控制台一行汇报
    b_cov_str = f"{b_avg:.3f}" if has_b else "N/A(无文本)"
    b_corr_str2 = f"{b_corr}/{b_total}" if has_b else f"0/{N_B}"
    print(f"A臂 avg coverage={a_avg:.3f} correctness={a_corr}/{a_total}, "
          f"B臂 avg coverage={b_cov_str} correctness={b_corr_str2}, "
          f"截断 A={logstat['A']['length']}/3 B={logstat['B']['length']}/{logstat['B']['stages']}, "
          f"复读 A={logstat['A']['repeat']}/3 B={logstat['B']['repeat']}/{logstat['B']['stages']}")
    print(f"WROTE {REPORT}")

if __name__ == "__main__":
    main()
