#!/usr/bin/env python3
"""Q6 budget scan 全量分析 — 队列 15 run 跑完后一次出全

整合四个跨域对比 (GPU 基准 = rep-scan 15 run):
  1. metacog 域不变性: 5 档 gap_rate / healthy_gap_rate 曲线
  2. B4 gold 域特异性: 域内 (q6 gold) vs 跨域 (gpu gold) cov, 5 档
  3. repair low-yield 跨域: node-level 修复率 (rework>0 且最终 verified)
  4. judge 5 档 (域内 gold)

用法: python3 q6_full_analysis.py
前置: q6_budget_scan_queue.sh 15 run 全部完成
每个 run 的 judge/metacog 只算一次 (embedding 慢, 缓存复用)。
"""
import sys, json, glob, os, re
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "modules", "B-pipeline-ablation"))
from judge_v1 import judge_run
from metacog_axis import compute_metacog, load_run_nodes

SCAN = os.path.join(ROOT, "modules", "B-pipeline-ablation", "data", "q6-budget-scan")
REP = os.path.join(ROOT, "modules", "B-pipeline-ablation", "data", "rep-scan")
GQ = os.path.join(ROOT, "modules", "B-pipeline-ablation", "data", "gold-q6-units.json")
GG = os.path.join(ROOT, "modules", "B-pipeline-ablation", "data", "gold-gpu-units.json")

TIERS = [50, 100, 150, 300, 719]


def load_runs(d, prefix):
    runs = defaultdict(list)
    for f in sorted(glob.glob(os.path.join(d, f"{prefix}-*.json"))):
        if f.endswith("scores.json"):
            continue
        m = re.search(rf"{prefix}-(\d+)-r(\d+)-", os.path.basename(f))
        if m:
            runs[int(m.group(1))].append(f)
    return runs


def main():
    q6 = load_runs(SCAN, "q6")
    rep = load_runs(REP, "rep")
    n_q6 = sum(len(v) for v in q6.values())
    print(f"=== Q6 全量分析: Q6 {n_q6}/15 run, GPU rep-scan {sum(len(v) for v in rep.values())} run ===\n")

    gq = json.load(open(GQ))
    gg = json.load(open(GG))

    # 每 run 算一次, 缓存
    per_run = {}
    for t in TIERS:
        for f in q6.get(t, []):
            print(f"  scoring {os.path.basename(f)} ...", flush=True)
            ri = judge_run(f, gold_units=gq)
            rx = judge_run(f, gold_units=gg)
            rm = compute_metacog(load_run_nodes(f))
            d = json.load(open(f))
            rw = [n for n in d.get("nodes", []) if int(n.get("rework_count", "0") or 0) > 0]
            per_run[f] = {
                "tier": t,
                "n_nodes": ri["n_nodes_raw"],
                "gap": rm["gap_rate"], "hg": rm["healthy_gap_rate"],
                "cov_in": ri["layers"]["coverage"]["coverage"],
                "cov_x": rx["layers"]["coverage"]["coverage"],
                "judge": ri["total_score"],
                "rw": len(rw), "fix": sum(1 for n in rw if n.get("status") == "verified"),
            }

    # GPU 基准
    rep_gaps = []
    for t, fs in rep.items():
        for f in fs:
            rep_gaps.append(compute_metacog(load_run_nodes(f))["gap_rate"])

    print("\n[1] metacog 域不变性:")
    print(f"  {'tier':>5} {'gap':>7} {'hg':>6} {'n_nodes':>12} {'n':>3}")
    for t in TIERS:
        rs = [per_run[f] for f in q6.get(t, [])]
        if not rs:
            continue
        ns = [r["n_nodes"] for r in rs]
        print(f"  {t:>5} {sum(r['gap'] for r in rs)/len(rs):>7.4f} "
              f"{sum(r['hg'] for r in rs)/len(rs):>6.3f} [{min(ns)},{max(ns)}] {len(rs):>3}")
    print(f"  {'GPU':>5} {sum(rep_gaps)/len(rep_gaps):>7.4f} {'':>6} {'':>12} {len(rep_gaps):>3}")

    print("\n[2] B4 gold 域特异性 (cov):")
    print(f"  {'tier':>5} {'域内':>7} {'跨域':>7} {'Δ':>8} {'n':>3}")
    for t in TIERS:
        rs = [per_run[f] for f in q6.get(t, [])]
        if not rs:
            continue
        ci = sum(r["cov_in"] for r in rs) / len(rs)
        cx = sum(r["cov_x"] for r in rs) / len(rs)
        print(f"  {t:>5} {ci:>7.4f} {cx:>7.4f} {ci-cx:>+8.4f} {len(rs):>3}")

    print("\n[3] repair low-yield 跨域 (node-level):")
    tot_rw = sum(r["rw"] for r in per_run.values())
    tot_fix = sum(r["fix"] for r in per_run.values())
    if tot_rw:
        print(f"  Q6 全 run: {tot_fix}/{tot_rw} = {tot_fix/tot_rw*100:.1f}%  (GPU 固化版 3.7% = 331/8870)")

    print("\n[4] judge 5 档 (域内 q6 gold):")
    for t in TIERS:
        rs = [per_run[f] for f in q6.get(t, [])]
        if not rs:
            continue
        print(f"  {t:>5}: {sum(r['judge'] for r in rs)/len(rs):.4f} (n={len(rs)})")


if __name__ == "__main__":
    main()
