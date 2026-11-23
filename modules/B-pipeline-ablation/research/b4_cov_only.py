#!/usr/bin/env python3
"""B4 轻量版: 只算 cov 层 (bge-m3 机械匹配), 跳过 LLM depth。
域特异性核心: Q6 runs × Q6 gold (域内) vs × GPU gold (跨域)。
模型只加载一次, 8 run × 2 gold = 16 次 encode (CPU, 快)。
"""
import json, os, sys, glob
from collections import defaultdict
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
from judge_v1 import layer_coverage, load_run_nodes, COS_THRESHOLD

SCAN = os.path.join(HERE, 'data', 'q6-budget-scan')
q6_gold = json.load(open(os.path.join(HERE, 'data', 'gold-q6-units.json')))
gpu_gold = json.load(open(os.path.join(HERE, 'data', 'gold-gpu-units.json')))
print(f"gold: q6={len(q6_gold)} units, gpu={len(gpu_gold)} units")

from sentence_transformers import SentenceTransformer
print("loading bge-m3 ...", flush=True)
model = SentenceTransformer("BAAI/bge-m3")
print("loaded.", flush=True)

runs = sorted(glob.glob(os.path.join(SCAN, 'q6-*.json')))
runs = [f for f in runs if not f.endswith('scores.json')]
print(f"Q6 runs: {len(runs)}")

by_t = defaultdict(lambda: {'in': [], 'out': []})
for f in runs:
    nodes = load_run_nodes(f)
    # 域内: Q6 gold
    cov_in, _ = layer_coverage(nodes, q6_gold, model, COS_THRESHOLD)
    # 跨域: GPU gold
    cov_out, _ = layer_coverage(nodes, gpu_gold, model, COS_THRESHOLD)
    # 从文件名提取 budget
    base = os.path.basename(f)
    budget = int(base.split('-')[1])
    by_t[budget]['in'].append(cov_in)
    by_t[budget]['out'].append(cov_out)
    print(f"  {base:45s} cov_in(q6)={cov_in:.4f}  cov_out(gpu)={cov_out:.4f}")

print("\nB4 域特异性 (cov 层, 分档均值):")
print(f"  {'budget':>8} {'cov_in(q6)':>12} {'cov_out(gpu)':>14} {'diff':>8}")
for t in sorted(by_t):
    mi = sum(by_t[t]['in'])/len(by_t[t]['in'])
    mo = sum(by_t[t]['out'])/len(by_t[t]['out'])
    print(f"  {t:>8} {mi:>12.4f} {mo:>14.4f} {mi-mo:>+8.4f}")
print("\n结论: 若 cov_in 系统性 > cov_out (diff 正), gold 域特异性成立")
