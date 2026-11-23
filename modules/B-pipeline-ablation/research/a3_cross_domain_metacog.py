#!/usr/bin/env python3
"""A3: 跨域 metacog 曲线对比 (general 方法论验证, gpu vs q6)

输入:
  gpu: modules/B-pipeline-ablation/data/rep-scan/rep-scan-scores.json (15 runs, 软上限时代)
       + K7 era (archive budget-* 15 runs, 从 archive-map 取)
  q6:  modules/B-pipeline-ablation/data/q6-budget-scan/q6-scan-scores.json (队列跑完生成)
输出: 控制台 + 追加到 GENERAL-METHODOLOGY-PATH 文档的 A3 节

口径 (与补充42/44 一致):
  x 轴 = realized node count (n_nodes), 不用 nominal budget (软上限时代 nominal 不干净)
  y 轴 = gap_rate (metacog 轴核心, gold-free)
  检验: ① 每域 gap_rate ~ realized n 相关性 (应 ns, 复现 gpu 的 invariance)
        ② 跨域 gap_rate 分布对比 (Mann-Whitney, 应无显著差异 → 域不变性)
        ③ 每域 5 档 nominal 的 gap_rate 均值 (应平坦)
"""
import json, os, sys, glob
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, 'modules', 'B-pipeline-ablation'))
from metacog_axis import compute_metacog, load_run_nodes

REPS = os.path.join(ROOT, 'modules', 'B-pipeline-ablation', 'data', 'rep-scan')
Q6 = os.path.join(ROOT, 'modules', 'B-pipeline-ablation', 'data', 'q6-budget-scan')
ARCH = os.path.join(ROOT, 'experiments', 'stage-ablation', 'checkpoints', 'archive')


def load_scores(path):
    if not os.path.exists(path):
        return []
    return json.load(open(path))


def pearson(xs, ys):
    n = len(xs)
    if n < 3:
        return float('nan')
    mx, my = sum(xs) / n, sum(ys) / n
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    vx = sum((x - mx) ** 2 for x in xs) ** 0.5
    vy = sum((y - my) ** 2 for y in ys) ** 0.5
    return cov / (vx * vy) if vx * vy else float('nan')


def mann_whitney_u(a, b):
    """无 scipy 依赖的 MW-U (小样本精确排名版, n 各 < 50 够用)."""
    combined = sorted([(v, 0) for v in a] + [(v, 1) for v in b])
    ranks = {}
    i = 0
    while i < len(combined):
        j = i
        while j + 1 < len(combined) and combined[j + 1][0] == combined[i][0]:
            j += 1
        avg_rank = (i + 1 + j + 1) / 2
        for k in range(i, j + 1):
            ranks[k] = avg_rank
        i = j + 1
    ra = sum(ranks[k] for k in range(len(combined)) if combined[k][1] == 0)
    n1, n2 = len(a), len(b)
    u1 = ra - n1 * (n1 + 1) / 2
    u2 = n1 * n2 - u1
    mu = n1 * n2 / 2
    sigma = (n1 * n2 * (n1 + n2 + 1) / 12) ** 0.5
    z = (min(u1, u2) - mu) / sigma if sigma else 0
    return min(u1, u2), z


def domain_rows(scores):
    """scores (rep-scan 格式) → [(budget, n_nodes, gap_rate)]"""
    rows = []
    for r in scores:
        if r.get('metacog') and r.get('n_nodes'):
            rows.append((r['budget'], r['n_nodes'], r['metacog']['gap']))
    return rows


def main():
    gpu = domain_rows(load_scores(os.path.join(REPS, 'rep-scan-scores.json')))
    q6f = os.path.join(Q6, 'q6-scan-scores.json')
    q6 = domain_rows(load_scores(q6f)) if os.path.exists(q6f) else []

    print("=== A3 跨域 metacog 曲线对比 ===")
    print(f"gpu rep-scan: {len(gpu)} runs | q6: {len(q6)} runs {'(未跑完/缺失)' if not q6 else ''}")
    if not gpu:
        print("gpu rep-scan scores 缺失, 退出")
        return

    for name, rows in [('gpu', gpu)] + ([('q6', q6)] if q6 else []):
        if len(rows) < 3:
            continue
        ns = [r[1] for r in rows]
        gs = [r[2] for r in rows]
        r = pearson(ns, gs)
        print(f"\n[{name}] n={len(rows)}, gap_rate 均值={sum(gs)/len(gs):.4f}")
        print(f"  gap_rate ~ realized n: r={r:+.3f}")
        by_tier = defaultdict(list)
        for b, n, g in rows:
            by_tier[b].append(g)
        for b in sorted(by_tier):
            v = by_tier[b]
            print(f"  budget {b}: mean gap={sum(v)/len(v):.4f} (n={len(v)})")

    if q6 and len(gpu) >= 3 and len(q6) >= 3:
        ga = [r[2] for r in gpu]
        qb = [r[2] for r in q6]
        u, z = mann_whitney_u(ga, qb)
        print(f"\n跨域 Mann-Whitney (gpu vs q6 gap_rate): U={u:.0f}, z={z:+.3f} "
              f"({'ns, 域不变性成立' if abs(z) < 1.96 else '显著差异, 域不变性不成立'})")


if __name__ == '__main__':
    main()
