#!/usr/bin/env python3
"""719 r3 落地后手动重评 (Q6 gold) — 不依赖队列脚本自动评分 (heredoc 预读不确定性).
用法: python3 q6_719_r3_rescore.py
输出: 719 r3 的 cov/total/depth + metacog 字段, 并更新 K7 报告 rerun 719 档数据.
"""
import json, sys, glob, re, statistics
sys.path.insert(0, '/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation')
from judge_v1 import judge_run
from metacog_axis import compute_metacog, load_run_nodes

gu = json.load(open('/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/gold-q6-units.json'))
gu = gu['units'] if isinstance(gu, dict) and 'units' in gu else gu

files = sorted(glob.glob('/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/q6-budget-scan-rerun/q6-719-r*.json'))
if not files:
    print("无 719 run 落地"); sys.exit(1)

print("rerun 719 全 rep (Q6 gold 重评):")
cows, mets = [], []
for f in files:
    m = re.search(r'q6-719-r(\d+)-', f)
    if not m: continue
    rj = judge_run(f, gold_units=gu)
    rm = compute_metacog(load_run_nodes(f))
    cov = rj['layers']['coverage']['coverage']
    mt = rm['metacog_total']
    cows.append(cov); mets.append(mt)
    print("  719-r%s: n=%s cov=%.4f total=%.4f metacog=%.4f" % (m.group(1), rj['n_nodes_raw'], cov, rj['total_score'], mt))

if len(cows) >= 2:
    print("cov mean=%.4f sd=%.4f (n=%d)" % (statistics.mean(cows), statistics.stdev(cows), len(cows)))
    print("metacog mean=%.4f sd=%.4f (n=%d)" % (statistics.mean(mets), statistics.stdev(mets), len(mets)))
    print("对照: 原批 719 cov=0.130/0.174/0.196 (mean 0.167, sd 0.033); 原批 metacog sd=0.0304")
    print("判据: rerun cov sd > 原批 0.033 → cache 共享压低方差假设在 719 档也支持")
