#!/usr/bin/env python3
"""Q7 budget scan 域内 gold 分析 — 第三域验证 cov 饱和点跨题稳健性 (K7 待办③)

用法: python3 q7_domain_gold_analyze.py
前置: q7_budget_scan_queue.sh 15 run 落地 (data/q7-budget-scan/q7-{50,100,150,300,719}-r{1,2,3}-*.json)

口径: judge_v1 + Q7 域内 gold (52 units, data/gold-q7-units.json), 与 Q6 域内 gold 分析同口径。
输出:
  1. 每档 cov/struct/total 池化均值 (n=3/档)
  2. cov 饱和点定位 (边际增益 < 0.01 视为进入平台)
  3. metacog 轴 (gold-free) 每档均值
  4. 跨题对比: Q7 vs Q6 的 cov 曲线形状 (饱和点位置是否一致 ~300)
  5. 落盘 data/q7-budget-scan/q7-domain-gold-analysis.json
"""
import sys, os, json, glob, re, statistics

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "modules", "B-pipeline-ablation"))
from judge_v1 import judge_run
from metacog_axis import compute_metacog, load_run_nodes

SCAN = os.path.join(ROOT, "modules", "B-pipeline-ablation", "data", "q7-budget-scan")
GOLD = os.path.join(ROOT, "modules", "B-pipeline-ablation", "data", "gold-q7-units.json")
OUT = os.path.join(SCAN, "q7-domain-gold-analysis.json")

gold = json.load(open(GOLD))
gu = gold["units"] if isinstance(gold, dict) and "units" in gold else gold
print(f"Q7 gold units: {len(gu)}")

recs = {}
for f in sorted(glob.glob(os.path.join(SCAN, "q7-*-r*.json"))):
    m = re.search(r"q7-(\d+)-r(\d+)-", os.path.basename(f))
    if not m:
        continue
    budget, rep = int(m.group(1)), int(m.group(2))
    try:
        rj = judge_run(f, gold_units=gu)
        rm = compute_metacog(load_run_nodes(f))
        recs[(budget, rep)] = {
            "budget": budget, "rep": rep,
            "n_nodes": rj["n_nodes_raw"],
            "struct": rj["layers"]["structure"]["depth_score"],
            "cov": rj["layers"]["coverage"]["coverage"],
            "n_units_hit": rj["layers"]["coverage"].get("n_confirmed"),
            "total": rj["total_score"],
            "metacog": round(rm["metacog_total"], 4),
            "gap": round(rm["gap_rate"], 4),
        }
        print(f"  [score] {budget}-r{rep} n={rj['n_nodes_raw']} cov={rj['layers']['coverage']['coverage']:.4f} total={rj['total_score']:.4f} metacog={rm['metacog_total']:.4f}")
    except Exception as e:
        print(f"  [score-err] {budget}-r{rep}: {e}")

if not recs:
    print("!! 无落地 run — relay 还没跑到 Q7, 退出")
    sys.exit(0)

tiers = sorted({b for b, _ in recs})
summary = {}
for b in tiers:
    vals = [recs[(b, r)] for r in sorted(recs) if recs[(b, r)]["budget"] == b]
    n = len(vals)
    summary[b] = {
        "n": n,
        "n_nodes_mean": round(statistics.mean(v["n_nodes"] for v in vals), 1),
        "cov_mean": round(statistics.mean(v["cov"] for v in vals), 4),
        "cov_sd": round(statistics.stdev(v["cov"] for v in vals), 4) if n > 1 else 0.0,
        "total_mean": round(statistics.mean(v["total"] for v in vals), 4),
        "metacog_mean": round(statistics.mean(v["metacog"] for v in vals), 4),
        "gap_mean": round(statistics.mean(v["gap"] for v in vals), 4),
    }

# cov 饱和点: 相邻档边际增益 < 0.01
sat = None
for i in range(1, len(tiers)):
    delta = summary[tiers[i]]["cov_mean"] - summary[tiers[i - 1]]["cov_mean"]
    if delta < 0.01:
        sat = tiers[i]
        break

# 跨题对比 (Q6 域内 gold 的 cov 曲线 — 与 Q7 cov 轴同口径; 原批 q6-gold-rescore.json)
# 注意: 原批 300 档三 rep 同分 0.1304 (cache 伪影, sd=0), rerun rep 隔离值 = 0.138
# (见 draft §4.3 provenance 说明); 形状结论对 300 取 0.1304 或 0.138 均稳健 (单调)
q6_cmp = None
q6f = os.path.join(ROOT, "modules", "B-pipeline-ablation", "data", "q6-budget-scan", "q6-gold-rescore.json")
if os.path.exists(q6f):
    q6 = json.load(open(q6f))
    q6_tiers = {}
    for r in q6:
        q6_tiers.setdefault(r["budget"], []).append(r["cov"])
    q6_cmp = {b: round(statistics.mean(v), 4) for b, v in sorted(q6_tiers.items())}

result = {
    "gold_units": len(gu),
    "n_runs": len(recs),
    "per_run": [recs[k] for k in sorted(recs)],
    "tier_summary": summary,
    "cov_saturation_point": sat,
    "q6_cov_curve_comparison": q6_cmp,
}
json.dump(result, open(OUT, "w"), ensure_ascii=False, indent=1)
print(f"\n=== Q7 域内 gold 分析 ({len(gu)} units, n={len(recs)} runs) ===")
for b in tiers:
    s = summary[b]
    print(f"  {b:>4}: n={s['n']} cov={s['cov_mean']:.4f} (sd {s['cov_sd']:.4f}) total={s['total_mean']:.4f} metacog={s['metacog_mean']:.4f} n_nodes={s['n_nodes_mean']}")
print(f"cov 饱和点: {sat if sat else '未达 (全程增益 >= 0.01)'}")
if q6_cmp:
    print(f"Q6 cov 曲线对比 (原批口径, 300 档 cache 伪影 0.1304): {q6_cmp}")
print(f"→ {os.path.basename(OUT)}")
