#!/usr/bin/env python3
"""Q6 重跑批 vs 原批 深度形状对照 (2026-11-23 23:59)

300-r1 发现: 独立检索批 L3 更窄 (58 vs 91), 更快撞深度墙 (252 vs 300 节点)。
cache 不只压低方差, 还改变展开形状 (宽 vs 深) → 改变哪个约束先绑定。
本脚本量化 6 runs (300/719 × 3 rep) 的形状差异, 检查是否稳健 (n=1→n=6)。

输出 (stdout + data/q6-budget-scan-rerun/q6-rerun-shape.json):
  每 run: n_nodes, L1-L4 分布, max_level, 停止原因
  对照: 原批同档 (cache 共享) vs 重跑批 (独立检索) 的 L3/L4 比例
  判定: L3 比例重跑 < 原批 (展开偏深) 且 停止机制不同 → 形状差异稳健

用法: /usr/bin/python3 q6_rerun_shape_check.py (重跑批 6 runs 落地后)
"""
import sys, os, json, glob, re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
BPL = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, BPL)
from metacog_axis import load_run_nodes

ORIG = os.path.join(BPL, "data", "q6-budget-scan")
RERUN = os.path.join(BPL, "data", "q6-budget-scan-rerun")
OUT = os.path.join(RERUN, "q6-rerun-shape.json")

def level_dist(f):
    nodes = load_run_nodes(f)
    lv = Counter(n.get("level", "?") for n in nodes)
    return len(nodes), lv

def stop_reason(d, b, rep):
    sp = os.path.join(d, f"q6-{b}-r{rep}.stdout")
    if os.path.exists(sp):
        for line in open(sp, errors="ignore"):
            if "max_depth=" in line or "max_nodes=" in line:
                return line.strip()[-25:]
    return "?"

rows = []
for b in [300, 719]:
    for rep in [1, 2, 3]:
        # 原批
        of = sorted(glob.glob(os.path.join(ORIG, f"q6-{b}-r{rep}-[0-9]*.json")))
        rf = sorted(glob.glob(os.path.join(RERUN, f"q6-{b}-r{rep}-[0-9]*.json")))
        o_n, o_lv = level_dist(of[0]) if of else (0, Counter())
        r_n, r_lv = level_dist(rf[0]) if rf else (0, Counter())
        o_stop = stop_reason(ORIG, b, rep)
        r_stop = stop_reason(RERUN, b, rep)
        rows.append({
            "budget": b, "rep": rep,
            "orig_n": o_n, "orig_L3": o_lv.get("L3", 0), "orig_L4": o_lv.get("L4", 0),
            "orig_L3_pct": round(o_lv.get("L3", 0) / o_n, 3) if o_n else None,
            "orig_stop": o_stop,
            "rerun_n": r_n, "rerun_L3": r_lv.get("L3", 0), "rerun_L4": r_lv.get("L4", 0),
            "rerun_L3_pct": round(r_lv.get("L3", 0) / r_n, 3) if r_n else None,
            "rerun_stop": r_stop,
        })

out = {"rows": rows,
       "note": ("cache 改变展开形状: 独立检索批 L3 更窄 (偏深) → 深度墙更早绑定; "
                "cache 共享批 L3 更宽 (偏宽) → 预算更早绑定。n=6 检查形状差异稳健性。"
                "停止机制不同 = 哪个约束先绑定不同, 是形状差异的直接后果")}
json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
for r in rows:
    print(f"  b{r['budget']} r{r['rep']}: orig n={r['orig_n']} L3={r['orig_L3']}({r['orig_L3_pct']}) {r['orig_stop']} "
          f"| rerun n={r['rerun_n']} L3={r['rerun_L3']}({r['rerun_L3_pct']}) {r['rerun_stop']}")
print(f"  → {os.path.basename(OUT)}")
