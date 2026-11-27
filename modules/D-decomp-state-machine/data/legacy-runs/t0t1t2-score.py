#!/usr/bin/env python3
"""T0/T1/T2 措辞梯度快速指标：token 剂量 + 缺口标注率 + 结构完整度。

不依赖 rubric 评委（那步走 arena 异族 judge），先出机器可检的三组数字：
1. out_tokens: 输出 token 数（剂量维度）
2. gap_rate: 输出中 [待核验]/不确定/记不清 等缺口标记的出现次数 / 输出千 token
3. section_rate: 是否出现「拆解/分解/主导」类分析结构词（结构激活维度）
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ARMS = ["T0", "T1", "T2"]
GAP_RE = re.compile(r"待核验|不确定|记不清|没把握|查不到|需要进一步查证|可能不准确")
STRUCT_RE = re.compile(r"拆解|分解|主导项|口径|标称|子因素|影响因素")

def collect(arms, qs):
    rows = []
    for arm in arms:
        for qid in qs:
            for rep in range(1, 6):
                p = os.path.join(HERE, f"{arm}-{qid}-r{rep}.json")
                if not os.path.exists(p):
                    continue
                d = json.load(open(p))
                txt = d.get("output_text", "")
                out_t = d.get("tokens", {}).get("out", 0)
                gaps = len(GAP_RE.findall(txt))
                struct = len(STRUCT_RE.findall(txt))
                rows.append({
                    "arm": arm, "qid": qid, "rep": rep,
                    "out_tokens": out_t,
                    "gap_per_ktok": round(gaps / max(out_t, 1) * 1000, 2),
                    "struct_hits": struct,
                    "has_struct": 1 if struct > 0 else 0,
                })
    return rows

def summarize(rows):
    print(f"{'arm':5} {'n':>3} {'out_tok_mean':>12} {'gap/kTok_mean':>13} {'struct%':>8}")
    for arm in ARMS:
        sub = [r for r in rows if r["arm"] == arm]
        if not sub:
            continue
        n = len(sub)
        ot = sum(r["out_tokens"] for r in sub) / n
        gr = sum(r["gap_per_ktok"] for r in sub) / n
        sp = 100 * sum(r["has_struct"] for r in sub) / n
        print(f"{arm:5} {n:>3} {ot:>12.0f} {gr:>13.2f} {sp:>7.0f}%")

if __name__ == "__main__":
    qs = sys.argv[1].split(",") if len(sys.argv) > 1 else ["Q1", "Q2"]
    rows = collect(ARMS, qs)
    print(f"collected {len(rows)} runs")
    if rows:
        summarize(rows)
    # per-question detail
    print("\nper-question:")
    for qid in qs:
        print(f"  {qid}:")
        for arm in ARMS:
            sub = [r for r in rows if r["arm"] == arm and r["qid"] == qid]
            if sub:
                ot = [r["out_tokens"] for r in sub]
                print(f"    {arm}: out_tokens={ot}")
