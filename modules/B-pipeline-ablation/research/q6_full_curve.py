#!/usr/bin/env python3
"""Q6 budget scan 全曲线分析 (A1 主线收尾, 队列 15/15 后运行)。

三轴 × 5 档 (50/100/150/300/719) × 3 reps:
  ① judge 轴 (域内 Q6 gold): total/depth/cov — 与 GPU K7 机械 depth 轴对比
  ② 监控轴 (claim field, 8-pattern): gap_rate — 与 GPU 0.105/0.106/0.114 (flat) 对比
  ③ cov 域特异性: 域内 (Q6 gold) vs 跨域 (GPU gold, 预期 0)
输出: per-tier mean±sd + 全曲线表, 供 draft §7 终稿数字。
口径: 8-pattern = [待核验]/不确定/未验证/待确认/需要验证/无法确定/缺乏数据/信息不足;
     claim field only (监控轴, detector-robust 轴); scores 由 q6_rescore.py 生成。
"""
import json, glob, os, re
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
SCAN = os.path.join(HERE, "..", "data", "q6-budget-scan")
CUR = re.compile(r'\[待核验\]|不确定|未验证|待确认|需要验证|无法确定|缺乏数据|信息不足')

runs = [f for f in glob.glob(os.path.join(SCAN, "q6-*.json")) if "scores" not in f]
by_b = defaultdict(list)
for f in runs:
    b = int(re.search(r'q6-(\d+)-r', f).group(1))
    d = json.load(open(f))
    nodes = d.get("nodes", d) if isinstance(d, dict) else d
    if isinstance(nodes, list):
        by_b[b].append((f, nodes))

scores = json.load(open(os.path.join(SCAN, "q6-scan-scores.json")))
sc_by_b = defaultdict(list)
for e in scores:
    sc_by_b[e["budget"]].append(e)

print("Q6 budget scan 全曲线 (n per tier):")
print(f"{'budget':>7} {'n':>2} {'judge':>14} {'depth':>12} {'cov':>12} {'mon_claim':>12}")
for b in sorted(by_b):
    js = [e["judge"]["total"] for e in sc_by_b.get(b, [])]
    ds = [e["judge"]["depth"] for e in sc_by_b.get(b, [])]
    cs = [e["judge"]["cov"] for e in sc_by_b.get(b, [])]
    mons = []
    for f, nodes in by_b[b]:
        hits = sum(1 for n in nodes if CUR.search(n.get("claim", "")))
        mons.append(hits / len(nodes) if nodes else 0.0)
    def fmt(v):
        if not v:
            return "n/a"
        m = sum(v) / len(v)
        sd = (sum((x - m) ** 2 for x in v) / len(v)) ** 0.5 if len(v) > 1 else 0.0
        return f"{m:.3f}±{sd:.3f}"
    print(f"{b:>7} {len(by_b[b]):>2} {fmt(js):>14} {fmt(ds):>12} {fmt(cs):>12} {fmt(mons):>12}")
print("\nGPU 同口径参考 (rep-scan, n=5/5/5): judge 机械 depth 0.625/0.725/0.800/0.933,")
print("监控轴 0.105/0.106/0.114 (flat), cov 域内随 budget 升 (K7 era)")
print("对比问题: ① Q6 judge 曲线形状 vs GPU (单调升 vs 升后饱和?)")
print("          ② Q6 监控轴是否 flat (GPU-only invariance 是否维持到 719?)")
print("          ③ 719 档 cov 是否继续升 (域内 cov 饱和点?)")
