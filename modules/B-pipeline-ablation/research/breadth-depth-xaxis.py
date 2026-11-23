#!/usr/bin/env python3
"""补充44 固化: Breadth-without-Depth 的 x 轴 = realized node count

draft §4.3/标题级承重数字:
  cor(机械depth, 实际节点数) = +0.981 (t=+18.33, df=13, p<0.001)
  名义 tier 均值: 50/100/150 = 0.667, 300 = 0.800, 719 = 0.933

口径 (与补充44 一致):
  scope = K7-era 15 runs (archive budget-*, runs-s5-sm-gpu.json)
  机械 depth = min(max_depth / 5, 1.0), max_depth = 节点 level 最大值 (L1→1, L5→5)
  x = run json n_nodes (realized, 非 nominal tier)
"""
import json, glob, os, re, math

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
ARCH = os.path.join(ROOT, 'experiments', 'stage-ablation', 'checkpoints', 'archive')


def max_depth(rj):
    m = 0
    for n in rj.get('nodes', []):
        lv = n.get('level', '')
        mm = re.match(r'L(\d+)', str(lv))
        if mm:
            m = max(m, int(mm.group(1)))
    return m


def pearson(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    vx = sum((x - mx) ** 2 for x in xs) ** 0.5
    vy = sum((y - my) ** 2 for y in ys) ** 0.5
    r = cov / (vx * vy) if vx * vy else float('nan')
    # t 检验
    t = r * math.sqrt((n - 2) / (1 - r * r)) if abs(r) < 1 else float('inf')
    return r, t, n - 2


def main():
    rows = []
    for d in sorted(glob.glob(os.path.join(ARCH, 'budget-*'))):
        rf = os.path.join(d, 'runs-s5-sm-gpu.json')
        if not os.path.exists(rf):
            continue
        rj = json.load(open(rf))
        nn = rj.get('n_nodes')
        md = max_depth(rj)
        mech = min(md / 5.0, 1.0)
        tier = re.match(r'budget-(\d+)-', os.path.basename(d)).group(1)
        rows.append((int(tier), nn, md, mech))
    rows.sort(key=lambda r: r[1])
    print(f"runs: {len(rows)} (expect 15)")
    print(f"{'tier':>5} {'n_nodes':>8} {'max_d':>6} {'mech':>6}")
    for t, nn, md, mech in rows:
        print(f"{t:>5} {nn:>8} {md:>6} {mech:>6.3f}")

    ns = [r[1] for r in rows]
    ms = [r[3] for r in rows]
    r, t, df = pearson(ns, ms)
    print(f"\ncor(mech_depth, n_nodes) = {r:+.3f}  (t={t:+.2f}, df={df})")

    # 名义 tier 均值
    from collections import defaultdict
    by_tier = defaultdict(list)
    for t, nn, md, mech in rows:
        by_tier[t].append(mech)
    print("名义 tier 均值:")
    for t in sorted(by_tier):
        v = by_tier[t]
        print(f"  {t}: {sum(v)/len(v):.3f} (n={len(v)})")


if __name__ == '__main__':
    main()
