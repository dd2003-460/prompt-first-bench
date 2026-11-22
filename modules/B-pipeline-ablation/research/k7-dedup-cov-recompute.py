#!/usr/bin/env python3
"""K7 15-run 去重 cov 重算（2026-11-23, magnet 伪影修复后验证）。
每 run 增量写 /tmp/k7-dedup-cov.json，崩了不丢进度。"""
import json, sys, glob, os, numpy as np
sys.path.insert(0, 'modules/B-pipeline-ablation')
from sentence_transformers import SentenceTransformer
import judge_v1
from collections import defaultdict

OUT = '/tmp/k7-dedup-cov.json'
model = SentenceTransformer("BAAI/bge-m3")
gold_units = judge_v1.load_gold("gpu")
gold_emb = model.encode([u["text"] for u in gold_units], normalize_embeddings=True)
res = json.load(open('modules/B-pipeline-ablation/data/t53b/results-budget-scan.json'))
by_b = defaultdict(list)
for r in res:
    b, rep = r['budget'], r['rep']
    cks = glob.glob(f'experiments/stage-ablation/checkpoints/archive/budget-{b}-r{rep}-*/runs-s5-sm-gpu.json')
    if not cks:
        print(f"MISSING ckpt: budget-{b}-r{rep}", flush=True); continue
    nodes = json.load(open(cks[0]))['nodes']
    ne = model.encode([n["claim"] for n in nodes], normalize_embeddings=True)
    sim = ne @ gold_emb.T
    top1 = sim.argmax(axis=1); top1_sim = sim[np.arange(len(nodes)), top1]
    matched = top1_sim >= 0.70
    dedup_cov = len(set(top1[matched]))/len(gold_units)
    by_b[b].append({'rep': rep, 'nodes': len(nodes), 'depth': r['depth'],
                    'cov_old': r['coverage'], 'cov_dedup': round(dedup_cov, 4)})
    json.dump({str(k): v for k, v in by_b.items()}, open(OUT, 'w'), indent=1)
    print(f"b{b:>3} r{rep}: nodes={len(nodes):>4} depth={r['depth']:.4f} cov_old={r['coverage']:.4f} cov_dedup={dedup_cov:.4f}", flush=True)
# 峰位置
print("\n=== 去重 cov 口径: 峰在哪? ===", flush=True)
for wd, wc in [(0.5, 0.5), (1.0, 0.0), (0.0, 1.0)]:
    means = {b: (wd*np.array([x['depth'] for x in v]) + wc*np.array([x['cov_dedup'] for x in v])).mean() for b, v in by_b.items()}
    print(f"{wd:.1f}*d+{wc:.1f}*c: " + " ".join(f"{b}:{means[b]:.4f}" for b in sorted(means)) + f"  峰={max(means, key=means.get)}", flush=True)
print("DONE", flush=True)
