#!/usr/bin/env python3
"""Generate results.md from runs.json + scores.json (written LAST, per protocol)."""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE, "runs.json")) as f:
    runs = json.load(f)
with open(os.path.join(BASE, "scores.json")) as f:
    scores = json.load(f)

by_id = {s["run_id"]: s for s in scores}
FLAG_WORDS = ["needs measurement", "cheapest probe", "special case",
              "需要测量", "最便宜的探针", "特例"]

def flag_total(cond):
    tot = {w: 0 for w in FLAG_WORDS}
    for r in runs:
        if r["condition"] == cond and r["status"] == "ok":
            fw = by_id[r["run_id"]]["flag_words"]
            for w in FLAG_WORDS:
                tot[w] += fw.get(w, 0)
    return tot

def main():
    L = []
    L.append("# TASK-T4b Pilot Results — T1-T5 模板 before/after（本地 27b）")
    L.append("")
    L.append("> origin: ai · 2026-11-26 · 自动生成自 runs.json + scores.json（机械 rubric，见 audit-rubric.md）")
    L.append("> 注：本文件为 2026-11-26 00:47 树重写后的重跑产物（首轮输出已丢失，详见 audit-rubric.md 重跑说明）。")
    L.append("")
    L.append("## 设置")
    L.append("")
    L.append("- 端点 `http://127.0.0.1:8787/v1/chat/completions`，model=`qwen3.8-27b-mtp`")
    L.append("- 条件 A（baseline）：system = \"You are a helpful assistant.\"；条件 B（treatment）：system = \"Follow these five thinking disciplines in your answer:\" + T1-T5 全文")
    L.append("- temperature=0.7, max_tokens=1500, n=1/cell, 串行执行间隔 1s")
    L.append("")
    L.append("## 得分表（0/1 机械 rubric）")
    L.append("")
    L.append("| prompt | 模板 | A baseline | B treatment | B−A |")
    L.append("|--------|------|-----------|-------------|-----|")
    ids = [r["run_id"] for r in runs]
    for pid in ["P1", "P2", "P3", "P4", "P5"]:
        sa = by_id[f"{pid}-A"]; sb = by_id[f"{pid}-B"]
        ta = runs[ids.index(f"{pid}-A")]
        tb = runs[ids.index(f"{pid}-B")]
        def fmt(e, r):
            if r["status"] == "error":
                return f"error ({r['error'][:40]})"
            fr = r["finish_reason"]
            tok = r["completion_tokens"]
            return f"**{e['score']}** ({fr}, {tok} tok)"
        a_s = sa["score"]; b_s = sb["score"]
        delta = (b_s - a_s) if (a_s is not None and b_s is not None) else "—"
        L.append(f"| {pid} | {sa['template']} | {fmt(sa, ta)} | {fmt(sb, tb)} | {delta} |")
    def tot(cond):
        vals = [by_id[f"{p}-{cond}"]["score"] for p in ["P1","P2","P3","P4","P5"]
                if by_id[f"{p}-{cond}"]["score"] is not None]
        return f"{sum(vals)}/{len(vals)}"
    L.append(f"| **合计** | | **{tot('A')}** | **{tot('B')}** | |")
    L.append("")
    L.append("## 逐 run 明细")
    L.append("")
    L.append("| run | status | finish_reason | completion_tokens | latency_s | score | 机械判据命中 |")
    L.append("|-----|--------|---------------|-------------------|-----------|-------|--------------|")
    for r in runs:
        e = by_id[r["run_id"]]
        checks = "; ".join(f"{k}={'✓' if v else '✗'}" for k, v in e["checks"].items()) or "—"
        L.append(f"| {r['run_id']} | {r['status']} | {r['finish_reason']} | {r['completion_tokens']} | {r['latency_s']} | {e['score']} | {checks} |")
    L.append("")
    L.append("## 标志词计数（不计分，grep 大小写不敏感）")
    L.append("")
    L.append("| 标志词 | A 合计 | B 合计 |")
    L.append("|--------|--------|--------|")
    fa, fb = flag_total("A"), flag_total("B")
    for w in FLAG_WORDS:
        L.append(f"| `{w}` | {fa[w]} | {fb[w]} |")
    L.append("")
    L.append("## 解读（初步方向性观察，供 T4a M7 使用；非统计结论）")
    L.append("")
    L.append("- 模板注入（B）相对 baseline（A）的增量出现在 **P1（T1 特例验证）与 P5（T5 指明缺 ground truth 的步骤）**：这两项的 prompt 原文未点名目标结构，只有模板注入补齐；P2/P3/P4 的 prompt 原文已点名目标结构（\"single formula\" / \"testable quantitative prediction\" / \"dimension by dimension\"），baseline 亦满分，模板无增量。")
    L.append("- 因此本表测量的是**模板对 prompt 未诱导维度的补齐效果**，不是模板的普遍增益；B−A 差值含截断窗口位置成分（B 的 system prompt 更长→输出更长→撞 1500 上限，模板短语更易落在窗口内）。")
    L.append("- 详细机制分析与两条可检验预言见 `mechanism-note.md`（非交付物，供 T4a/Lead 参考）。")
    L.append("")
    L.append("## 局限性声明")
    L.append("")
    L.append("1. **n=1/cell**：每格仅 1 次调用，无统计显著性声明（论文中如实这么写）。")
    L.append("2. **单模型**：仅 qwen3.8-27b-mtp（本地 vLLM），结论不外推到其他模型/规模。")
    L.append("3. **无统计检验**：5 个二值分不构成可检验的差异；B−A 仅作方向性观察。")
    L.append("4. **分数是机械 checklist 非质量分**：0/1 由关键词/结构存在性判定（见 audit-rubric.md 的正则组），不衡量答案质量、正确性或推理深度；命中关键词≠真正执行了对应思考纪律。")
    L.append("5. **采样噪声**：temperature=0.7，单次采样结果含随机性；finish_reason=length 的 run 输出可能被 max_tokens=1500 截断（截断本身如实记录在 runs.json）。")
    L.append("6. **截断影响（重要）**：所有 run max_tokens=1500，9/10 finish_reason=length（输出在 1500 token 处截断），rubric 是对截断后文本打分；两条件相同上限，对照受控公平，但\"结构存在性\"检查受截断影响（写到一半可能丢后续结构项）。")
    L.append("")
    L.append("## 文件清单")
    L.append("")
    L.append("- `runs.json` — 10 个 run 原始输出（prompt id / condition / full text / tokens / latency / status / finish_reason）")
    L.append("- `raw/<run_id>.json` — 每次调用的 API 原始返回（未编造核验用）")
    L.append("- `audit-rubric.md` — rubric 原文 + 机械实现说明 + 重跑说明")
    L.append("- `scores.json` — 逐 run 判据命中明细（本表的数据源）")
    L.append("")
    with open(os.path.join(BASE, "results.md"), "w") as f:
        f.write("\n".join(L))
    print("results.md written:", os.path.join(BASE, "results.md"))

if __name__ == "__main__":
    main()
