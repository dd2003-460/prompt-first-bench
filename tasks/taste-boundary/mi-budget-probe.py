#!/usr/bin/env python3
"""MI probe: I(budget档; judge_total分箱) on q7 budget scan + permutation test.

Spec (task book): 5 budget-level points (budget, judge_total_mean), 4 quartile bins,
MI in bits, 2000-permutation p-value. Pre-registered consistency rule:
  log fit says monotone-increasing + saturating => level-bin association expected;
  MI>0 with p<0.05 => consistent, else underpowered (n=5 flagged low-power).

Supplement (clearly labeled, outside spec): 14 per-rep points (300-r2 dup excluded)
so levels repeat and the permutation test is non-degenerate.
Pure computation, no judgment.
"""
import json, math, os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
CURVE = os.path.normpath(os.path.join(HERE,
    "../../modules/B-pipeline-ablation/data/q7-budget-scan/q7-budget-response-curve.json"))
RAW = os.path.normpath(os.path.join(HERE,
    "../../modules/B-pipeline-ablation/data/q7-budget-scan/q7-scan-scores.json"))
OUT = os.path.join(HERE, "mi-budget-probe-result.md")


def mutual_information_bits(a, b):
    """Plug-in discrete MI (bits) for two integer-label arrays, same length."""
    mi = 0.0
    n = len(a)
    for av in np.unique(a):
        for bv in np.unique(b):
            p_ij = np.mean((a == av) & (b == bv))
            if p_ij <= 0:
                continue
            mi += p_ij * math.log2(p_ij / (np.mean(a == av) * np.mean(b == bv)))
    return mi


def quartile_bins(scores):
    qs = np.quantile(scores, [0.25, 0.5, 0.75])
    return np.digitize(scores, qs), qs  # bins 0..3


def perm_test(levels, bins, n_perm=2000, seed=20261128):
    mi_obs = mutual_information_bits(levels, bins)
    rng = np.random.default_rng(seed)
    ge = sum(mutual_information_bits(rng.permutation(levels), bins) >= mi_obs
             for _ in range(n_perm))
    return mi_obs, (ge + 1) / (n_perm + 1)


def main():
    with open(CURVE) as f:
        curve = json.load(f)
    rows = curve["rows"]
    budgets = np.array([r["budget"] for r in rows], dtype=float)
    scores = np.array([r["judge_total_mean"] for r in rows], dtype=float)
    assert len(budgets) == 5

    # --- spec'd probe: 5 level-mean points ---
    levels = np.arange(5)
    bins, qs = quartile_bins(scores)
    mi5, p5 = perm_test(levels, bins)
    h5 = -sum((c / 5) * math.log2(c / 5) for c in np.bincount(bins) if c > 0)

    # --- supplement: 14 per-rep points (300-r2 dup excluded) ---
    with open(RAW) as f:
        raw = json.load(f)
    raw = [r for r in raw if not (r["budget"] == 300 and r["rep"] == 2)]
    lvl14 = np.array([r["budget"] for r in raw])
    sc14 = np.array([r["judge"]["total"] for r in raw])
    bins14, qs14 = quartile_bins(sc14)
    mi14, p14 = perm_test(lvl14, bins14)
    assert len(raw) == 14

    fit = curve["fits"]["log_saturation"]
    verdict = "consistent" if p5 < 0.05 else "underpowered"

    lines = [
        "# MI 探针: I(budget档; judge_total分箱) — q7 budget scan",
        "",
        "## 数据点 (spec: 5 档均值)",
        "| budget | judge_total_mean | 箱 |",
        "|---|---|---|",
        *[f"| {int(b)} | {s:.4f} | {int(k)} |" for b, s, k in zip(budgets, scores, bins)],
        f"- 来源: q7-budget-response-curve.json rows[] (一手 = q7-scan-scores.json 15 条逐 rep; 300-r2 为 r1 字节级复制, 上游已剔除)",
        f"- 四分位切点: {qs[0]:.4f} / {qs[1]:.4f} / {qs[2]:.4f}; 箱占用 " + ", ".join(f"bin{i}={c}" for i, c in enumerate(np.bincount(bins))),
        "",
        "## 结果 (spec 探针, n=5)",
        f"- MI = {mi5:.4f} bits (= H(箱) {h5:.4f} bits, 即 MI/H=100%)",
        f"- permutation (2000 次, seed=20261128): p = {p5:.4f}",
        f"- **结构性退化**: 5 档各仅 1 点, 分箱又由分数分位构造 ⇒ 箱是档的确定性函数 (H(箱|档)=0) ⇒ MI≡H(箱) 对一切排列不变, permutation 检验功效恒为零 (p 恒=1.0)",
        f"- 与 log 拟合 (jt={fit['intercept']}+{fit['slope']}·ln(budget), R²={fit['r2']}, 单调递增+饱和) 一致性: **{verdict}** (p≥0.05, 且为结构性零功效, 非样本量不够那么简单)",
        "",
        "## 补充 (spec 外, 14 逐 rep 点, 300-r2 剔除)",
        f"- 切点 {qs14[0]:.4f}/{qs14[1]:.4f}/{qs14[2]:.4f}; 箱占用 " + ", ".join(f"bin{i}={c}" for i, c in enumerate(np.bincount(bins14))),
        f"- MI = {mi14:.4f} bits; permutation (2000 次): p = {p14:.4f} → {'支持档-分箱关联' if p14 < 0.05 else '不显著'}",
        "",
        f"- ⚠ 主探针 n=5 功效不足 (结构性零功效), 结论仅示意, 不硬下判断。",
        f"- 一句话结论: 5 点 spec 探针下 MI 无判别力 (p=1.0, 功效不足); 14-rep 补充探针 p={p14:.4f} {'与 log 饱和拟合的单调结论一致' if p14 < 0.05 else '未达显著'}, 信息论度量与参数化拟合在形状层面{'一致' if p14 < 0.05 else '无法确认'}。",
    ]
    with open(OUT, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(json.dumps({"mi5": round(mi5, 4), "p5": round(p5, 4),
                      "mi14": round(mi14, 4), "p14": round(p14, 4),
                      "verdict": verdict, "out": OUT}))


if __name__ == "__main__":
    main()
