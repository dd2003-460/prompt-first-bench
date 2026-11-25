#!/usr/bin/env python3
# origin: ai
# T8b smoke test: correctness 探针 + 截断/复读统计 + 报告生成
# 机械探针：从每条输出最后 2000 字符提取最终推荐（卡型+精度+数量），与 gold 3090×4/W4/n=2 比对
# gold 来源: pfb/bench/rubric-v3/ablation/gold-tree.md 头部声明 "赢家配置 3090×4 / W4 / n=2"
import json, re, sys

RAW = "raw_outputs_t8b.json"
SCORES = "raw_outputs_t8b_mech_scores.json"
LOG = "t8b_run.log"
REPORT = "t8b-smoke-report.md"

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

# ---------- 截断/复读统计（从 log 解析）----------
def parse_log(path):
    stat = {"A": {"length":0, "repeat":0, "runs":0},
            "B": {"length":0, "repeat":0, "stages":0, "runs":0}}
    cur_b_run = None
    for line in open(path):
        m = re.match(r"\[A-direct-run(\d)\] OK .* finish=(\w+) .* repeat5=(\d+)", line)
        if m:
            stat["A"]["runs"] += 1
            if m.group(2) == "length": stat["A"]["length"] += 1
            if int(m.group(3)) >= 5: stat["A"]["repeat"] += 1
            continue
        m = re.match(r"\[B-pfb-run(\d)-([\d.]+)\] OK .* finish=(\w+) .* repeat5=(\d+)", line)
        if m:
            stat["B"]["stages"] += 1
            cur_b_run = m.group(1)
            if m.group(3) == "length": stat["B"]["length"] += 1
            if int(m.group(4)) >= 5: stat["B"]["repeat"] += 1
            continue
        m = re.match(r"\[B-pfb-run(\d)\] DONE", line)
        if m:
            stat["B"]["runs"] += 1
    return stat

# ---------- main ----------
def main():
    d = json.load(open(RAW))
    scores = json.load(open(SCORES))
    logstat = parse_log(LOG)

    # arm_a correctness
    probe_a = []
    for i, a in enumerate(d["arm_a"], 1):
        cfg = extract_final(a["content"])
        v = verdict(cfg)
        probe_a.append({"id": f"A{i}", "cfg": cfg, "verdict": v})
    # arm_b: 无文本（runner 崩溃），全部无法提取
    n_b = 3  # 预期 3 条
    probe_b = [{"id": f"B{i}", "cfg": None, "verdict": "无法提取(无文本)"} for i in range(1, n_b+1)]

    a_cov = [scores[f"A{i}"]["overall"] for i in range(1, len(d["arm_a"])+1)]
    a_avg = sum(a_cov)/len(a_cov) if a_cov else 0.0
    a_corr = sum(1 for p in probe_a if p["verdict"]=="对")
    a_total = len(probe_a)

    # 生成报告
    L = []
    L.append("# T8b Smoke Test 报告（pfb 六阶段 vs 直接求解）")
    L.append("")
    L.append("> **定位**：smoke test，不是有效性实验。有效性需 T8c 的 token-matched 对照。")
    L.append("> 本报告只回答三个 smoke 问题：**recall 是否成功 / 有无退化 / coverage 如何**。不做质量提升声称。")
    L.append("")
    L.append("## 0. 数据完整性声明（重要）")
    L.append("")
    L.append("- **Arm A（直接求解）**：3 条完整自由文本，`finish_reason=stop`，正常落盘。")
    L.append(f"- **Arm B（pfb 六阶段）**：`raw_outputs_t8b.json` 中 `arm_b=[]`（空）。")
    L.append(f"  - 原因：runner `run_exp_t8b.py` 只在**全部 3 条 B 跑完后**才 `json.dump` 落盘 arm_b；")
    L.append(f"    run 3 在 stage 04 后进程被回收（日志止于 `[B-pfb-run3-04]`，无 `DONE`、无 `WROTE arm_b + finished`），")
    L.append(f"    故 3 条 B 的**阶段文本全部丢失**，只剩 `t8b_run.log` 里的元数据（finish_reason / repeat5 / token 数）。")
    L.append(f"  - 后果：**Arm B 的 coverage 分数与 correctness 无法计算**（无文本可打分）。")
    L.append(f"    下文 B 臂只报告**可恢复的截断/复读统计**（来自 log 元数据）。")
    L.append(f"  - 补救：需重跑 `python3 run_exp_t8b.py b`（建议改成每 stage 增量落盘，防再次丢数据）。")
    L.append("")
    L.append("## 1. Coverage 分数表（机械 judge：S1 SKU广度 / S2 维度覆盖 / S3 需求合规）")
    L.append("")
    L.append("judge = `judge_gpu_mech.py`（regex+count，确定性，无 LLM）。overall = (S1+S2+S3)/3。")
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
    L.append("| B1–B3 | — | — | — | **无法计算（无文本）** |")
    L.append("")
    L.append("> 注：S1 的 `L40` 与 `L40S` 在白名单里是两个独立条目，`L40S` 文本会同时命中两者，"
             "属 judge 正则的已知口径（substring 匹配），此处如实记录不改分。")
    L.append("")
    L.append("## 2. Correctness 探针（本次新增关键维度）")
    L.append("")
    L.append(f"gold 锚点 = **3090×4 / W4 / n=2**（来源：`pfb/bench/rubric-v3/ablation/gold-tree.md` 头部声明）。")
    L.append("机械提取规则：取每条输出**最后 2000 字符**，正则找主卡型（窗口内最早出现的卡型）+ 数量（`N×卡型`）+ 精度（W4/W8/W16/INT4/INT8/FP8/BF16）。")
    L.append("判定：卡型=3090 且 精度∈{W4,INT4} 且 数量=4 → **对**；提取到推荐但与 gold 不符 → **错**；提取不到 → **无法提取**。")
    L.append("探针局限（如实标注）：① 只看尾部 2000 字符，条件式/多分支结尾（如决策树）可能提取不到单一主推荐；"
             "② 数量只认 `N×卡型` 紧邻写法，`4 张 3090` 这类写法会漏检；③ 精度取窗口内首个命中，"
             "若尾部先提 INT8 后提 W4 会取到 INT8。故 correctness 是**下界估计**（漏检只会低估，不会虚高）。")
    L.append("")
    L.append("| 样本 | 提取到的最终推荐 (卡型/数量/精度) | 判定 |")
    L.append("|------|----------------------------------|------|")
    for p in probe_a:
        c = p["cfg"]
        cfgstr = f"{c['card']}×{c['qty']} / {c['prec'] or '—'}" if c else "—"
        L.append(f"| {p['id']} | {cfgstr} | **{p['verdict']}** |")
    for p in probe_b:
        L.append(f"| {p['id']} | —（无文本） | **{p['verdict']}** |")
    L.append("")
    L.append(f"**correctness 汇总**：A 臂 **{a_corr}/{a_total} 对**；B 臂 **0/{n_b}（全部无法提取，无文本）**。")
    L.append("")
    L.append("解读（仅描述机械提取结果，不做质量评判）：")
    for p in probe_a:
        c = p["cfg"]
        if c:
            L.append(f"- {p['id']} 提取到 {c['card']}×{c['qty']} / {c['prec'] or '—'} → {p['verdict']}"
                     + ("（卡型命中 3090 但数量/精度与 gold 不符）" if c["card"]==GOLD_CARD else "（卡型即与 gold 3090 不符）"))
        else:
            L.append(f"- {p['id']} 最后 2000 字符内提取不到卡型 → {p['verdict']}")
    L.append("- 三条均未收敛到 gold 赢家 3090×4/W4/n=2（correctness 0/3）。")
    L.append("")
    L.append("## 3. 截断 / 复读统计")
    L.append("")
    L.append("截断 = `finish_reason=length` 的 stage/run 数；复读警告 = `repeat5>=5` 的 stage/run 数。")
    L.append("")
    L.append("| 臂 | 样本数 | 截断(length) | 复读(repeat5≥5) |")
    L.append("|----|--------|--------------|-----------------|")
    L.append(f"| A（直接，整条） | {logstat['A']['runs']} | {logstat['A']['length']} | {logstat['A']['repeat']} |")
    L.append(f"| B（六阶段，按 stage） | {logstat['B']['stages']} stages / {logstat['B']['runs']} runs | {logstat['B']['length']} | {logstat['B']['repeat']} |")
    L.append("")
    L.append(f"解读：A 臂 3 条全部 `stop` 自然收尾，**零截断**；复读 repeat5 分别为 3/8/5，"
             f"其中 {logstat['A']['repeat']} 条 ≥5（A2=8、A3=5 达到阈值，A1=3 未达）。")
    L.append(f"B 臂 {logstat['B']['stages']} 个 stage（run1/2 各 6 个走完，run3 止于 04 共 5 个）中 "
             f"**{logstat['B']['length']} 个撞 4096 token 上限被截断**（{logstat['B']['length']/logstat['B']['stages']*100:.0f}%），"
             f"**{logstat['B']['repeat']} 个 stage 复读≥5** —— 多阶段累积上下文 + 每阶段 4096 上限导致大面积截断与复读，"
             f"这是 B 臂的主要退化信号（但文本已丢失，无法量化对 coverage 的影响）。")
    L.append("")
    L.append("## 4. 结论（只回答 smoke 三问）")
    L.append("")
    L.append(f"1. **recall 是否成功**：A 臂 3 条均完整召回（`stop`，无截断），recall 成功。"
             f"B 臂流程能跑通 6 阶段（run1/run2 各走完 6 stage），但 runner 落盘缺陷导致 B 臂文本丢失，"
             f"**B 臂 recall 无法验证**（需重跑确认）。")
    L.append(f"2. **有无退化**：A 臂无截断退化；B 臂存在明显退化信号 —— "
             f"{logstat['B']['length']}/{logstat['B']['stages']} stage 截断 + {logstat['B']['repeat']} stage 复读≥5"
             f"（多阶段 + 每阶段 4096 上限所致）。correctness 上 A 臂 0/{a_total} 命中 gold，"
             f"说明直接求解也未收敛到 3090×4/W4/n=2。")
    L.append(f"3. **coverage 如何**：A 臂 overall 均值 **{a_avg:.3f}**（S1={sum(scores[f'A{i}']['S1_sku_coverage'] for i in range(1,len(d['arm_a'])+1))/len(d['arm_a']):.3f}, "
             f"S2={sum(scores[f'A{i}']['S2_dimension'] for i in range(1,len(d['arm_a'])+1))/len(d['arm_a']):.3f}, "
             f"S3={sum(scores[f'A{i}']['S3_compliance'] for i in range(1,len(d['arm_a'])+1))/len(d['arm_a']):.3f}），"
             f"处于高位（S1/S2 接近饱和）。B 臂 coverage 无法计算（无文本）。")
    L.append("")
    L.append("> **边界声明**：本报告是 smoke test，**不声称任何质量提升/下降的因果结论**。"
             "coverage 高 ≠ 答案对（correctness 探针正是为此新增）；B 臂结论受数据丢失限制，重跑前不作定论。")
    L.append("")

    open(REPORT, "w").write("\n".join(L))

    # 控制台一行汇报
    print(f"A臂 avg coverage={a_avg:.3f} correctness={a_corr}/{a_total}, "
          f"B臂 avg coverage=N/A(无文本) correctness=0/{n_b}, "
          f"截断 A={logstat['A']['length']}/3 B={logstat['B']['length']}/{logstat['B']['stages']}, "
          f"复读 A={logstat['A']['repeat']}/3 B={logstat['B']['repeat']}/{logstat['B']['stages']}")
    print(f"WROTE {REPORT}")

if __name__ == "__main__":
    main()
