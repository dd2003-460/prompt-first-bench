#!/usr/bin/env python3
"""覆盖层阈值标定：15 budget runs × gold 36 unit 的 top-1 sim 分布 + 阈值敏感性。
产出: 各阈值下 coverage 曲线, 供冻结 cosine 阈值。"""
import json, glob, os, re, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tjudge1_parse import load_gold
from sentence_transformers import SentenceTransformer

ARCH = "/Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation/checkpoints/archive"
model = SentenceTransformer("BAAI/bge-m3")
gold = load_gold("gpu")
gold_emb = model.encode([u["text"] for u in gold], normalize_embeddings=True)

runs = sorted(glob.glob(os.path.join(ARCH, "budget-*/runs-s5-sm-gpu.json")))
print(f"{len(runs)} runs")
pgb = []
for r in runs:
    dd = json.load(open(r))
    ne = model.encode([n["claim"] for n in dd["nodes"]], normalize_embeddings=True)
    s = ne @ gold_emb.T
    pgb.append(s.max(axis=0))  # (36,) 每 gold unit 的最高 sim
pgb = np.stack(pgb)  # (15, 36)

print("\n每 gold unit 最高 sim 分布 (15 runs × 36 units = 540 值):")
for q in (50, 75, 90, 95, 99):
    print(f"  p{q}: {np.percentile(pgb, q):.3f}")

print("\n阈值敏感性 (mean coverage over 15 runs):")
for thr in (0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80):
    cov = (pgb >= thr).mean()
    print(f"  thr={thr}: {cov:.3f}")

print("\nper-run coverage @0.70:")
for i, r in enumerate(runs):
    name = re.search(r"budget-(\d+)-r(\d+)", r).group(0)
    c = (pgb[i] >= 0.70).sum()
    print(f"  {name}: {c}/36 = {(pgb[i] >= 0.70).mean():.3f}")

# 保存
out = {"per_gold_best_sim": pgb.tolist(),
       "run_names": [re.search(r"budget-(\d+)-r(\d+)", r).group(0) for r in runs]}
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "judge-v1-cov-calibration.json"), "w"), indent=1)
print("\nsaved → judge-v1-cov-calibration.json")
