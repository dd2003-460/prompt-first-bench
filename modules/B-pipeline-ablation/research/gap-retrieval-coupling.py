#!/usr/bin/env python3
"""Stored computation: does gap-marking (a) drive retrieval (b)?

D's AGI definition: (a) judge own info sufficiency [gap marking] -> (b) acquire
[retrieval] -> (c) reason. This tests the (a)->(b) coupling at the run level:
across the 15 rep-scan runs, does a higher gap-marking rate predict a higher
retrieval rate / post-retrieval accuracy?

Reproduce: python3 gap-retrieval-coupling.py
Expected: cor(gap,retrieval)=+0.029, cor(gap,post_acc)=+0.064 (both ns, n=15).
Scope: GPU domain, rep-scan era (11-23), n=15. Single-domain, single-era.
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
    mc = compute_metacog(load_nodes(f))
    rows.append((int(m.group(1)), int(m.group(2)), mc["n_total"],
                 mc["gap_rate"], mc["retrieval_rate"], mc["post_retrieval_accuracy"]))
rows.sort()
print(f"{'bud':>4} {'rep':>4} {'n':>5} {'gap':>7} {'retr':>7} {'post':>7}")
for b, r, n, g, ret, post in rows:
    print(f"{b:>4} {r:>4} {n:>5} {g:>7.4f} {ret:>7.4f} {post:>7.4f}")


def pear(x, y):
    n = len(x); mx = sum(x) / n; my = sum(y) / n
    num = sum((a - mx) * (b - my) for a, b in zip(x, y))
    den = (sum((a - mx) ** 2 for a in x) * sum((b - my) ** 2 for b in y)) ** 0.5
    return num / den if den else float("nan")


G = [x[3] for x in rows]; R = [x[4] for x in rows]; P = [x[5] for x in rows]
n = len(G)
print(f"\nn = {n} (GPU domain, rep-scan era)")
for name, (x, y) in {"gap~retrieval": (G, R), "gap~post_acc": (G, P),
                     "retrieval~post_acc": (R, P)}.items():
    r = pear(x, y)
    t = r * ((n - 2) / (1 - r * r)) ** 0.5 if abs(r) < 1 else float("inf")
    print(f"cor({name}) = {r:+.4f}  t={t:+.3f}  (|t|>2.18 for p<0.05)")
