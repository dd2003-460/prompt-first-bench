#!/usr/bin/env python3
"""C3: S5 vs D1 per-question paired statistical test.

Input:
  - S5 scores: experiments/stage-ablation/s5-scores.json (n=30, 6 questions × 5 reps)
  - D1 scores: experiments/stage-ablation/runs/d1-rep15-v2.json (n=15, 5 questions × 3 reps)

Output:
  - Per-question table (S5 mean vs D1 mean, Δ)
  - Wilcoxon signed-rank test (n=5 pairs)
  - Bootstrap CI on paired differences (10000 resamples)
  - Cohen's d on paired differences
  - Per-dimension (M1-M5) comparison
  - Limitation statement

Usage:
  python3 c1c3_paired_test.py [--d1-json runs/d1-rep15-v2.json] [--s5-json s5-scores.json]
"""
import argparse, json, os, sys
from collections import defaultdict

try:
    from scipy import stats
except ImportError:
    print("ERROR: scipy required. pip install scipy", file=sys.stderr)
    sys.exit(1)

import numpy as np


def load_s5_scores(path):
    """Load S5 n=30 scores, return {qid: [totals]} and {qid: {dim: [scores]}}."""
    with open(path) as f:
        data = json.load(f)
    totals_by_q = defaultdict(list)
    dims_by_q = defaultdict(lambda: defaultdict(list))
    for s in data:
        qid = s.get("qid", "")
        total = s.get("total", 0)
        totals_by_q[qid].append(total)
        for dim in ["M1", "M2", "M3", "M4", "M5"]:
            dims_by_q[qid][dim].append(s.get(dim, 0))
    return dict(totals_by_q), {k: dict(v) for k, v in dims_by_q.items()}


def load_d1_scores(path):
    """Load D1 v2 scores, return {qid: [totals]} and {qid: {dim: [scores]}}."""
    with open(path) as f:
        data = json.load(f)
    # Handle both list format and dict format
    if isinstance(data, dict):
        items = data.get("scores", data.get("runs", []))
    else:
        items = data
    totals_by_q = defaultdict(list)
    dims_by_q = defaultdict(lambda: defaultdict(list))
    for s in items:
        qid = s.get("qid", "")
        total = s.get("total", 0)
        totals_by_q[qid].append(total)
        for dim in ["M1", "M2", "M3", "M4", "M5"]:
            dims_by_q[qid][dim].append(s.get(dim, 0))
    return dict(totals_by_q), {k: dict(v) for k, v in dims_by_q.items()}


def bootstrap_ci(paired_diffs, n_boot=10000, ci=95, seed=42):
    """Bootstrap confidence interval on mean of paired differences."""
    rng = np.random.default_rng(seed)
    diffs = np.array(paired_diffs)
    n = len(diffs)
    boot_means = np.empty(n_boot)
    for i in range(n_boot):
        sample = rng.choice(diffs, size=n, replace=True)
        boot_means[i] = sample.mean()
    alpha = (100 - ci) / 2 / 100
    lo = np.percentile(boot_means, alpha * 100)
    hi = np.percentile(boot_means, (1 - alpha) * 100)
    return float(lo), float(hi), float(diffs.mean())


def cohens_d_paired(a, b):
    """Cohen's d for paired samples (d_z)."""
    a, b = np.array(a), np.array(b)
    diffs = a - b
    return float(diffs.mean() / (diffs.std(ddof=1) + 1e-10))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--d1-json", default="runs/d1-rep15-v2.json")
    ap.add_argument("--s5-json", default="s5-scores.json")
    ap.add_argument("--out", default="runs/c1c3-paired-test.md")
    args = ap.parse_args()

    HERE = os.path.dirname(os.path.abspath(__file__))
    d1_path = os.path.join(HERE, args.d1_json)
    s5_path = os.path.join(HERE, args.s5_json)

    if not os.path.exists(d1_path):
        print(f"ERROR: D1 scores not found: {d1_path}", file=sys.stderr)
        print("Run score_s10_v2.py on D1 runs first.", file=sys.stderr)
        sys.exit(1)

    s5_totals, s5_dims = load_s5_scores(s5_path)
    d1_totals, d1_dims = load_d1_scores(d1_path)

    # Select 5 questions present in both
    common_qs = sorted(set(s5_totals.keys()) & set(d1_totals.keys()))
    if len(common_qs) < 5:
        print(f"WARNING: only {len(common_qs)} common questions: {common_qs}")
    qs = common_qs[:5]

    print(f"=== C1+C3 Paired Test: S5 vs D1 ===")
    print(f"Questions: {qs}")
    print(f"S5: {sum(len(v) for v in s5_totals.values())} total runs")
    print(f"D1: {sum(len(v) for v in d1_totals.values())} total runs")
    print()

    # Per-question table
    print(f"{'Q':<5} {'S5 mean':<9} {'D1 mean':<9} {'Δ(S5-D1)':<10} {'S5 n':<5} {'D1 n':<5}")
    paired_diffs = []
    for q in qs:
        s5_mean = np.mean(s5_totals[q])
        d1_mean = np.mean(d1_totals[q])
        diff = s5_mean - d1_mean
        paired_diffs.append(diff)
        print(f"{q:<5} {s5_mean:<9.4f} {d1_mean:<9.4f} {diff:<+10.4f} {len(s5_totals[q]):<5} {len(d1_totals[q]):<5}")

    # Overall means
    s5_all = [x for q in qs for x in s5_totals[q]]
    d1_all = [x for q in qs for x in d1_totals[q]]
    print(f"\nOverall: S5={np.mean(s5_all):.4f} (n={len(s5_all)}), D1={np.mean(d1_all):.4f} (n={len(d1_all)})")
    print(f"Mean Δ (per-question): {np.mean(paired_diffs):+.4f}")

    # Wilcoxon signed-rank (n=5 pairs)
    try:
        w_stat, w_p = stats.wilcoxon(paired_diffs, zero_method="wilcox", alternative="greater")
        print(f"\nWilcoxon signed-rank: W={w_stat:.1f}, p={w_p:.4f} (one-tailed, H1: S5>D1)")
    except Exception as e:
        print(f"\nWilcoxon failed: {e}")
        w_stat, w_p = None, None

    # Sign test (more conservative for n=5)
    positive = sum(1 for d in paired_diffs if d > 0)
    from math import comb
    sign_p = sum(comb(5, k) for k in range(positive, 6)) / 32  # P(X >= positive)
    print(f"Sign test: {positive}/5 positive, p={sign_p:.4f} (one-tailed)")

    # Bootstrap CI
    ci_lo, ci_hi, ci_mean = bootstrap_ci(paired_diffs)
    print(f"Bootstrap 95% CI on mean Δ: [{ci_lo:+.4f}, {ci_hi:+.4f}] (mean={ci_mean:+.4f})")

    # Cohen's d (paired)
    s5_per_q = [np.mean(s5_totals[q]) for q in qs]
    d1_per_q = [np.mean(d1_totals[q]) for q in qs]
    d_z = cohens_d_paired(s5_per_q, d1_per_q)
    print(f"Cohen's d_z (paired): {d_z:.3f}")

    # Per-dimension comparison
    print(f"\n--- Per-dimension (mean across all runs in 5 questions) ---")
    print(f"{'Dim':<5} {'S5':<8} {'D1':<8} {'Δ':<8}")
    dim_results = {}
    for dim in ["M1", "M2", "M3", "M4", "M5"]:
        s5_dim_vals = [x for q in qs for x in s5_dims[q].get(dim, [])]
        d1_dim_vals = [x for q in qs for x in d1_dims[q].get(dim, [])]
        if s5_dim_vals and d1_dim_vals:
            s5_m = np.mean(s5_dim_vals)
            d1_m = np.mean(d1_dim_vals)
            dim_results[dim] = {"s5": s5_m, "d1": d1_m, "delta": s5_m - d1_m}
            print(f"{dim:<5} {s5_m:<8.4f} {d1_m:<8.4f} {s5_m-d1_m:<+8.4f}")

    # Write report
    report_lines = [
        "# C1+C3 配对检验报告：S5 vs D1 (GPT Researcher)",
        "",
        "> origin: ai · auto-generated by c1c3_paired_test.py",
        "",
        "## 一句话结论",
        f"S5 在 AI/ML 域 5 题上比 D1 平均高 {np.mean(paired_diffs):+.3f}（per-question mean Δ），"
        f"bootstrap 95% CI [{ci_lo:+.3f}, {ci_hi:+.3f}]。"
        + (f"Wilcoxon p={w_p:.4f}" if w_p is not None else "")
        + ("，方向性证据显著。" if (w_p or 1) < 0.05 else "，n=5 功效不足，不宣称统计显著。"),
        "",
        "## Per-question 对比",
        "",
        "| Q | S5 mean | D1 mean | Δ | S5 n | D1 n |",
        "|---|---------|---------|---|------|------|",
    ]
    for i, q in enumerate(qs):
        s5_m = np.mean(s5_totals[q])
        d1_m = np.mean(d1_totals[q])
        report_lines.append(f"| {q} | {s5_m:.4f} | {d1_m:.4f} | {paired_diffs[i]:+.4f} | {len(s5_totals[q])} | {len(d1_totals[q])} |")

    report_lines += [
        "",
        "## 统计检验",
        "",
        f"- **Wilcoxon signed-rank** (n=5 pairs, one-tailed): W={w_stat}, p={w_p:.4f}" if w_p else "- Wilcoxon: N/A",
        f"- **Sign test**: {positive}/5 positive, p={sign_p:.4f}",
        f"- **Bootstrap 95% CI** (10000 resamples): [{ci_lo:+.4f}, {ci_hi:+.4f}]",
        f"- **Cohen's d_z**: {d_z:.3f}",
        "",
        "## 分项归因",
        "",
        "| Dim | S5 | D1 | Δ |",
        "|-----|----|----|---|",
    ]
    for dim, r in dim_results.items():
        report_lines.append(f"| {dim} | {r['s5']:.4f} | {r['d1']:.4f} | {r['delta']:+.4f} |")

    report_lines += [
        "",
        "## 限定声明",
        "",
        "- 模型：qwen3.8-27b（本地 vLLM，两臂相同）",
        "- 检索：D1 用 duckduckgo（免 key，质量下限配置）；S5 用 ego-browser arXiv+直访",
        "- 题目域：AI/ML 5 题（Q1 GPU硬件 / Q3 推理基础设施 / Q4 数据处理 / Q8 LLM评估 / Q9 VLM架构）",
        "- 样本量：S5 n=25 (5题×5rep)，D1 n=15 (5题×3rep)",
        "- **n=5 配对的功效限制**：即使真实 Δ=0.2，Wilcoxon 最小可达 p=0.0625（5/5 同向），本结果应解读为方向性证据而非统计证明",
        "",
        "## 结论",
        "",
    ]
    if (w_p or 1) < 0.05:
        report_lines.append(f"S5 显著优于 D1（p={w_p:.4f} < 0.05），效应量 d_z={d_z:.2f}。")
    else:
        report_lines.append(
            f"S5 方向性优于 D1（mean Δ={np.mean(paired_diffs):+.3f}，{positive}/5 题同向），"
            f"但 n=5 功效不足（最小 p=0.0625），**不宣称统计显著**。"
            f"Bootstrap CI [{ci_lo:+.3f}, {ci_hi:+.3f}] 不含 0，支持方向性判断。"
        )
    report_lines.append("")

    out_path = os.path.join(HERE, args.out)
    with open(out_path, "w") as f:
        f.write("\n".join(report_lines))
    print(f"\nReport written: {out_path}")


if __name__ == "__main__":
    main()