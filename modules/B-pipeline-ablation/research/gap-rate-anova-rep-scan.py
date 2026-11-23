#!/usr/bin/env python3
"""Stored computation for the gap_rate budget-invariance claim (承重数字规则).

Recomputes gap_rate per tree from the 15 rep-scan run files via the production
compute_metacog (metacog_axis.py), then the tier means, pooled within-group sd,
and the one-way ANOVA F(2,12) cited in the draft §4.3 / abstract.

Reproduce: python3 gap-rate-anova-rep-scan.py
Expected: tier means 0.099/0.100/0.107 (n=5/5/5), pooled sd 0.0538, F(2,12)=0.036.
"""
import glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from metacog_axis import compute_metacog

DATA = os.path.join(HERE, "..", "data", "rep-scan")


def load_nodes(p):
    t = json.load(open(p))
    return t if isinstance(t, list) else t.get("nodes", [])


files = [f for f in glob.glob(os.path.join(DATA, "rep-*.json"))
         if not f.endswith("scores.json")]
rows = []
for f in files:
    m = re.match(r"rep-(\d+)-r(\d+)", os.path.basename(f))
    if not m:
        continue
    b, r = int(m.group(1)), int(m.group(2))
    mc = compute_metacog(load_nodes(f))
    rows.append((b, r, mc["n_total"], mc["gap_rate"]))
rows.sort()
for b, r, n, g in rows:
    print(f"  {b} r{r}: n={n:4d} gap={g:.4f}")

tiers = {100: [], 150: [], 300: []}
for b, r, n, g in rows:
    if b in tiers:
        tiers[b].append(g)

allg = [g for v in tiers.values() for g in v]
gm = sum(allg) / len(allg)
ssb = sum(len(v) * (sum(v) / len(v) - gm) ** 2 for v in tiers.values())
ssw = sum(sum((x - sum(v) / len(v)) ** 2 for x in v) for v in tiers.values())
k, N = 3, len(allg)
F = (ssb / (k - 1)) / (ssw / (N - k))
pooled_sd = (ssw / (N - k)) ** 0.5
means = {b: sum(v) / len(v) for b, v in tiers.items()}
spread = max(means.values()) - min(means.values())

print(f"\nn per tier: " + " ".join(f"{b}={len(v)}" for b, v in tiers.items()))
print(f"tier means: " + " ".join(f"{b}={means[b]:.4f}" for b in sorted(means)))
print(f"between-tier mean spread = {spread:.4f}")
print(f"pooled within-group sd (sqrt(MSW)) = {pooled_sd:.4f}")
print(f"ratio spread/pooled_sd = {spread / pooled_sd:.2f}  ({pooled_sd / spread:.1f}x smaller)")
print(f"ANOVA F({k - 1},{N - k}) = {F:.4f}")
