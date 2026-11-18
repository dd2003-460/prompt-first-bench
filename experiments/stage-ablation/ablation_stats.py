#!/usr/bin/env python3
"""T53b 消融实验统计汇总。

读 ablation-results.json，输出每题每臂的 coverage/depth 均值±SE + 95%CI（n=10）。
用法: python3 ablation_stats.py
"""
import json, math, os, sys

RESULTS_FILE = "ablation-results.json"
OUT_FILE = "ablation-stats-summary.json"

def mean_se_ci(vals, ci=0.95):
    """均值 ± SE + 置信区间。n<2 时 SE/CI 为 None。"""
    n = len(vals)
    if n == 0:
        return None
    m = sum(vals) / n
    if n < 2:
        return {"mean": m, "se": None, "ci_lo": None, "ci_hi": None, "n": n}
    sd = (sum((x - m) ** 2 for x in vals) / (n - 1)) ** 0.5
    se = sd / math.sqrt(n)
    # t 分布临界值（n=10, df=9, 95% CI）≈ 2.262
    t_val = 2.262 if n == 10 else 1.96  # 近似
    return {
        "mean": round(m, 4),
        "se": round(se, 4),
        "ci_lo": round(m - t_val * se, 4),
        "ci_hi": round(m + t_val * se, 4),
        "n": n,
        "sd": round(sd, 4),
    }

def main():
    if not os.path.exists(RESULTS_FILE):
        print(f"ERROR: {RESULTS_FILE} not found")
        sys.exit(1)

    with open(RESULTS_FILE) as f:
        data = json.load(f)

    runs = data.get("runs", [])
    print(f"Total runs: {len(runs)}")

    # 按 qid + arm 分组
    groups = {}
    for r in runs:
        key = f"{r['qid']}_{r['arm']}"
        groups.setdefault(key, []).append(r)

    summary = {}
    for key in sorted(groups.keys()):
        runs_g = groups[key]
        covs = [r["coverage"] for r in runs_g if r.get("coverage") is not None]
        depths = [r["depth"] for r in runs_g if r.get("depth") is not None]
        n_nodes = [r.get("n_nodes", 0) for r in runs_g]
        n_verified = [r.get("n_verified", 0) for r in runs_g]
        n_degraded = [r.get("n_degraded", 0) for r in runs_g]
        l1_unc = [r.get("l1_uncertainty", False) for r in runs_g]

        summary[key] = {
            "n_runs": len(runs_g),
            "coverage": mean_se_ci(covs),
            "depth": mean_se_ci(depths),
            "n_nodes_mean": round(sum(n_nodes) / len(n_nodes), 1) if n_nodes else None,
            "n_verified_mean": round(sum(n_verified) / len(n_verified), 1) if n_verified else None,
            "n_degraded_mean": round(sum(n_degraded) / len(n_degraded), 1) if n_degraded else None,
            "l1_uncertainty_count": sum(1 for x in l1_unc if x),
            "l1_uncertainty_rate": round(sum(1 for x in l1_unc if x) / len(l1_unc), 3) if l1_unc else None,
        }

        # 打印
        cov = summary[key]["coverage"]
        dep = summary[key]["depth"]
        print(f"\n=== {key} (n={summary[key]['n_runs']}) ===")
        if cov:
            print(f"  coverage: {cov['mean']:.4f} ± {cov['se']:.4f} (95% CI: [{cov['ci_lo']:.4f}, {cov['ci_hi']:.4f}])")
        if dep:
            print(f"  depth:    {dep['mean']:.4f} ± {dep['se']:.4f} (95% CI: [{dep['ci_lo']:.4f}, {dep['ci_hi']:.4f}])")
        print(f"  nodes: {summary[key]['n_nodes_mean']} (verified: {summary[key]['n_verified_mean']}, degraded: {summary[key]['n_degraded_mean']})")
        print(f"  L1 uncertainty: {summary[key]['l1_uncertainty_count']}/{summary[key]['n_runs']} ({summary[key]['l1_uncertainty_rate']:.1%})")

        # 标出好轮次（coverage 或 depth 高于均值 + 1SE）
        good_rounds = []
        for r in runs_g:
            if cov and r.get("coverage") is not None and r["coverage"] > cov["mean"] + cov["se"]:
                good_rounds.append(f"{r['qid']}_{r['arm']}_r{r['round']:02d} (cov={r['coverage']:.3f})")
            elif dep and r.get("depth") is not None and r["depth"] > dep["mean"] + dep["se"]:
                good_rounds.append(f"{r['qid']}_{r['arm']}_r{r['round']:02d} (depth={r['depth']:.3f})")
        if good_rounds:
            print(f"  good rounds (>mean+1SE): {', '.join(good_rounds)}")

    # 保存
    with open(OUT_FILE, "w") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f"\nSaved → {OUT_FILE}")

    # r7 复现判据
    gpu_formula = summary.get("gpu_formula", {})
    gpu_text = summary.get("gpu_text", {})
    print(f"\n=== r7 复现判据 ===")
    print(f"gpu formula: L1 uncertainty {gpu_formula.get('l1_uncertainty_count', 0)}/10 (需 ≥3)")
    print(f"gpu text:    L1 uncertainty {gpu_text.get('l1_uncertainty_count', 0)}/10 (需 ≥3)")
    if gpu_formula.get("l1_uncertainty_count", 0) >= 3 or gpu_text.get("l1_uncertainty_count", 0) >= 3:
        print("✓ r7 复现成功")
    else:
        print("✗ r7 未复现（<3 轮）")

if __name__ == "__main__":
    main()
