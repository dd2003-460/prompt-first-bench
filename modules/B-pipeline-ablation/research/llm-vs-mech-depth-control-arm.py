#!/usr/bin/env python3
"""Control arm: does the LLM answer-depth axis track the mechanical tree-depth axis?

Pairs each K7 budget-scan run's LLM depth score (judge_v2_depth, results-budget-scan.json)
with its mechanical depth_score (judge_v1, judge-v1-budget-scan.json) on the SAME 15 runs.

SCOPE (read before citing): the two axes score DIFFERENT objects — the LLM scores the
prose synthesis answer against a depth rubric; the mechanical layer scores the tree
structure. So this correlation tests whether answer-depth tracks tree-depth, and it
does not (r=+0.049, n=15, p~0.86). It does NOT prove the LLM "carries no depth signal"
about the answer itself — only that the two axes are independent. Combined with the
LLM axis showing no significant budget trend at n=3 (150-vs-plateau gap 0.9 run-sd),
the 150 "peak" is best read as rubric noise on a flat, self-biased axis.

承重数字规则: this is the stored computation for the §4.3 control-arm claim.
Reproduce: python3 llm-vs-mech-depth-control-arm.py
"""
import json, os, statistics

HERE = os.path.dirname(os.path.abspath(__file__))
T53 = os.path.join(HERE, "..", "data", "t53b")

rbs = json.load(open(os.path.join(T53, "results-budget-scan.json")))
jv1 = json.load(open(os.path.join(T53, "judge-v1-budget-scan.json")))

llm = {r["run"]: r["depth"] for r in rbs}
mech = {r["run"].replace(".json", ""): r["layers"]["structure"]["depth_score"] for r in jv1["runs"]}
bud = {r["run"]: r["budget"] for r in rbs}

runs = sorted([r for r in llm if r in mech and r in bud])
X = [llm[r] for r in runs]   # LLM depth
Y = [mech[r] for r in runs]  # mechanical depth
B = [bud[r] for r in runs]   # budget


def pear(x, y):
    n = len(x); mx = sum(x) / n; my = sum(y) / n
    num = sum((a - mx) * (b - my) for a, b in zip(x, y))
    den = (sum((a - mx) ** 2 for a in x) * sum((b - my) ** 2 for b in y)) ** 0.5
    return num / den if den else float("nan")


n = len(X)
r_xm = pear(X, Y)
r_xb = pear(X, B)
r_yb = pear(Y, B)
t = r_xm * ((n - 2) / (1 - r_xm ** 2)) ** 0.5

print(f"n = {n} K7 budget-scan runs (paired LLM + mechanical depth)")
print(f"\ncor(LLM_depth, mech_depth) = {r_xm:+.4f}   t={t:.3f}  df={n-2}  (|t|>2.18 for p<0.05)")
print(f"cor(LLM_depth, budget)     = {r_xb:+.4f}")
print(f"cor(mech_depth, budget)    = {r_yb:+.4f}")

print(f"\nLLM range [{min(X):.3f},{max(X):.3f}] sd={statistics.pstdev(X):.4f}")
print(f"mech range [{min(Y):.1f},{max(Y):.1f}] sd={statistics.pstdev(Y):.4f} distinct={sorted(set(Y))}")

# LLM mean grouped by mechanical depth level
print("\nLLM mean by mechanical depth level:")
for lvl in sorted(set(Y)):
    g = [x for x, y in zip(X, Y) if y == lvl]
    print(f"  mech={lvl:.1f} (n={len(g)}): LLM mean={statistics.mean(g):.4f}  range=[{min(g):.3f},{max(g):.3f}]")

# per-tier (budget) means
print("\nPer budget tier:")
for t_ in [50, 100, 150, 300, 719]:
    L = [llm[f"gpu_budget{t_}_r{i}"] for i in (1, 2, 3)]
    M = [mech[f"gpu_budget{t_}_r{i}"] for i in (1, 2, 3)]
    print(f"  budget={t_}: LLM={statistics.mean(L):.4f} (sd {statistics.pstdev(L):.4f})  mech={statistics.mean(M):.3f} {sorted(set(M))}")
