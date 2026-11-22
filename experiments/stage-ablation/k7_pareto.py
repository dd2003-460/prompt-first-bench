#!/usr/bin/env python3
"""K7 budget-scan Pareto 分析（research-agi-budget goal, E4）。

真正的自变量 = 实际节点数（覆盖因子数 = 算力成本），不是 budget 参数
（budget 是下界非上限，各档实际节点数重叠）。质量轴 = depth_score。

输出：
  1. 每档（budget 参数）聚合 mean depth + bootstrap 95% CI
  2. 实际节点数 vs depth 的 Spearman 相关 + 分段均值
  3. Pareto 包络：按节点数排序，标记"新增节点未带来 depth 提升"的平台期
  4. 性价比 = depth / elapsed_s（每单位墙钟的 depth）

用法：
  python3 k7_pareto.py [--runs-dir DIR] [--out MD]
  默认读 modules/B-pipeline-ablation/data/t53b/runs_budget_scan/
"""
import argparse, glob, json, math, os, sys
from collections import defaultdict

def spearman(xs, ys):
    def rank(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0]*len(v)
        i = 0
        while i < len(order):
            j = i
            while j+1 < len(order) and v[order[j+1]] == v[order[i]]:
                j += 1
            avg = (i + j) / 2 + 1
            for k in range(i, j+1):
                r[order[k]] = avg
            i = j+1
        return r
    rx, ry = rank(xs), rank(ys)
    n = len(xs)
    if n < 3:
        return float('nan')
    mx, my = sum(rx)/n, sum(ry)/n
    cov = sum((rx[i]-mx)*(ry[i]-my) for i in range(n))
    vx = math.sqrt(sum((x-mx)**2 for x in rx))
    vy = math.sqrt(sum((y-my)**2 for y in ry))
    if vx == 0 or vy == 0:
        return float('nan')
    return cov/(vx*vy)

def pearson(xs, ys):
    n = len(xs)
    if n < 3:
        return float('nan')
    mx, my = sum(xs)/n, sum(ys)/n
    cov = sum((xs[i]-mx)*(ys[i]-my) for i in range(n))
    vx = math.sqrt(sum((x-mx)**2 for x in xs))
    vy = math.sqrt(sum((y-my)**2 for y in ys))
    if vx == 0 or vy == 0:
        return float('nan')
    return cov/(vx*vy)

def bootstrap_ci(vals, n_boot=2000, ci=0.95, seed=42):
    import random
    rng = random.Random(seed)
    if len(vals) < 2:
        m = sum(vals)/len(vals)
        return m, m, m
    means = []
    n = len(vals)
    for _ in range(n_boot):
        sample = [vals[rng.randrange(n)] for _ in range(n)]
        means.append(sum(sample)/n)
    means.sort()
    lo = means[int((1-ci)/2*n_boot)]
    hi = means[int((1+ci)/2*n_boot)]
    return sum(vals)/n, lo, hi

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs-dir", default="modules/B-pipeline-ablation/data/t53b/runs_budget_scan")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    rows = []
    for f in sorted(glob.glob(os.path.join(args.runs_dir, "*.json"))):
        try:
            d = json.load(open(f))
        except Exception as e:
            print(f"WARN skip {f}: {e}", file=sys.stderr)
            continue
        rows.append({
            "run": d.get("run"),
            "budget": d.get("budget_max_nodes"),
            "nodes": d.get("n_nodes"),
            "depth": d.get("depth_score"),
            "cov": d.get("coverage"),
            "s": d.get("elapsed_s"),
        })

    valid = [r for r in rows if r["depth"] is not None and r["nodes"]]
    print(f"完成 run: {len(rows)}, 有效（depth+nodes）: {len(valid)}\n")
    print("⚠ 质量轴声明（anatomy-0.5184.md, 2026-11-22）: depth_score 与旧 judge cov15 "
          "Pearson r=0.861 —— 质量轴 = 同族 LLM judge 分，非独立树结构度量；"
          "存在 self-judge 偏差，结论限于'开源 27b 模型 + 本地 4×V100'条件。\n")

    # 1. 每档聚合
    by_b = defaultdict(list)
    for r in valid:
        by_b[r["budget"]].append(r["depth"])
    print("## 每档（budget 参数）depth 聚合 + bootstrap 95% CI\n")
    print("| budget | n | mean | CI95 | min | max |")
    print("|---|---|---|---|---|---|")
    for b in sorted(by_b):
        v = by_b[b]
        m, lo, hi = bootstrap_ci(v)
        print(f"| {b} | {len(v)} | {m:.4f} | [{lo:.4f}, {hi:.4f}] | {min(v):.4f} | {max(v):.4f} |")

    # 2. 实际节点数 vs depth
    pts = sorted([(r["nodes"], r["depth"], r["run"]) for r in valid], key=lambda p: p[0])
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    rs = spearman(xs, ys); rp = pearson(xs, ys)
    print(f"\n## 实际节点数 vs depth（n={len(pts)}）\n")
    print(f"- Spearman ρ = {rs:.3f}")
    print(f"- Pearson r = {rp:.3f}")
    print(f"\n| 节点数 | depth | run |")
    print(f"|---|---|---|")
    for x, y, run in pts:
        print(f"| {x} | {y:.4f} | {run} |")

    # 分段
    lo = [p[1] for p in pts if p[0] < 200]
    hi = [p[1] for p in pts if p[0] >= 200]
    if lo and hi:
        print(f"\n分段均值：")
        print(f"- <200 节点: {sum(lo)/len(lo):.4f} (n={len(lo)})")
        print(f"- >=200 节点: {sum(hi)/len(hi):.4f} (n={len(hi)})")

    # 3. Pareto 包络
    print(f"\n## Pareto 包络（按节点数升序，标记平台期）\n")
    print("平台期判据：新增节点后 depth 未创新高（边际增益 ≤ 0）。\n")
    print("| 节点数 | depth | run | 是否包络点 |")
    print("|---|---|---|---|")
    best = -1
    for x, y, run in pts:
        is_envelope = y > best
        if is_envelope:
            best = y
        print(f"| {x} | {y:.4f} | {run} | {'★' if is_envelope else ''} |")

    # 4. 性价比
    print(f"\n## 性价比（depth / 墙钟秒）\n")
    print("| run | 节点 | depth | 秒 | depth/s×1000 |")
    print("|---|---|---|---|---|")
    for r in sorted(valid, key=lambda r: -(r["depth"]/(r["s"] or 1))):
        print(f"| {r['run']} | {r['nodes']} | {r['depth']:.4f} | {r['s']} | {r['depth']/(r['s'] or 1)*1000:.4f} |")

    # 写 markdown
    if args.out:
        md = []
        md.append("# K7 预算扫描 Pareto 分析\n")
        md.append(f"完成 run: {len(rows)}, 有效: {len(valid)}\n")
        md.append("⚠ 质量轴声明（anatomy-0.5184.md）: depth_score 与旧 judge cov15 r=0.861，"
                  "质量轴 = 同族 LLM judge 分（self-judge 偏差），非独立结构度量；"
                  "结论限于开源 27b + 4×V100 条件。\n")
        md.append("## 每档 depth 聚合 + bootstrap 95% CI\n")
        md.append("| budget | n | mean | CI95 | min | max |")
        md.append("|---|---|---|---|---|---|")
        for b in sorted(by_b):
            v = by_b[b]
            m, lo, hi = bootstrap_ci(v)
            md.append(f"| {b} | {len(v)} | {m:.4f} | [{lo:.4f}, {hi:.4f}] | {min(v):.4f} | {max(v):.4f} |")
        md.append(f"\n## 实际节点数 vs depth（n={len(pts)}）\n")
        md.append(f"- Spearman ρ = {rs:.3f}")
        md.append(f"- Pearson r = {rp:.3f}")
        md.append(f"\n| 节点数 | depth | run |")
        md.append(f"|---|---|---|")
        for x, y, run in pts:
            md.append(f"| {x} | {y:.4f} | {run} |")
        md.append(f"\n## Pareto 包络\n")
        md.append("| 节点数 | depth | run | 包络点 |")
        md.append("|---|---|---|---|")
        best = -1
        for x, y, run in pts:
            is_env = y > best
            if is_env: best = y
            md.append(f"| {x} | {y:.4f} | {run} | {'★' if is_env else ''} |")
        open(args.out, "w").write("\n".join(md) + "\n")
        print(f"\n[written] {args.out}")

if __name__ == "__main__":
    main()
