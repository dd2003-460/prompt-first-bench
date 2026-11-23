#!/usr/bin/env python3
"""52.5% unverified (GPU 域) 承重数字固化 — draft finding 1

draft abstract: "the tree grows around its 52.5% unverified nodes
(5,630/10,730 across the 33-tree GPU-domain corpus, deduped)".

口径 (T-JUDGE-1 line 178 闭环判定):
  - GPU 域 = sm-gpu-* + budget-* (K7 15 runs) 的 run json (runs-s5-sm-*.json)
  - 非 verified = status != 'verified' (含 pending + degraded)
  - 33 棵去重 GPU 树, 10730 节点, 5630 非 verified = 52.5%
  - 全语料口径 (160 棵/21945) = 45.5% (9984/21945) — 见 §4.4
Reproduce: python3 gpu-unverified-52pct.py
"""
import json, glob, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
ARCH = os.path.join(ROOT, 'experiments', 'stage-ablation', 'checkpoints', 'archive')


def unverified(patterns):
    files = set()
    for pat in patterns:
        files.update(glob.glob(os.path.join(ARCH, pat, 'runs-s5-sm-*.json')))
    total = nonver = 0
    for f in sorted(files):
        try:
            d = json.load(open(f))
        except Exception:
            continue
        ns = d.get('nodes', [])
        total += len(ns)
        nonver += sum(1 for n in ns if n.get('status') != 'verified')
    return nonver, total


gpu_nv, gpu_tot = unverified(('sm-gpu-*', 'budget-*'))
all_nv, all_tot = unverified(('sm-gpu-*', 'budget-*', 'sm-nat-*', 'sm-soc-*',
                              'idea2-*', 'repscan-*', 'rep-*'))

print(f"GPU 域: {gpu_nv}/{gpu_tot} = {gpu_nv/gpu_tot*100:.1f}%  (目标 5630/10730 = 52.5%)")
print(f"全语料: {all_nv}/{all_tot} = {all_nv/all_tot*100:.1f}%  (目标 9984/21945 = 45.5%)")
