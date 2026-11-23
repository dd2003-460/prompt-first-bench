#!/usr/bin/env python3
"""Node-level (a)<->(b) coupling: does gap-marking co-occur with retrieval?

OVERTURNS the run-level finding in gap-retrieval-coupling.py (Supplementary 28),
which was an ecological fallacy: at the run level both gap_rate and retrieval_rate
are near-constant (~0.10 / ~0.30), so the within-run coupling is invisible.

At the NODE level, across the 15 rep-scan runs (GPU domain, 11-23 era):
  - defensive-marked nodes: 66.0% are source=search
  - non-defensive nodes:     27.5% are source=search
  - two-proportion z = +15.55 (p < 0.001); 15/15 runs show defensive > non-defensive

DIRECTION: the dominant defensive pattern is search+degraded (60.6%) — the model
retrieved, got an insufficient source, then marked the gap. The evidence text is
post-retrieval critique ("[质询]...参考来源仅提供了概述"), not pre-retrieval
triggering. So the supported direction is (b)retrieve -> (a)critique, NOT the
D-AGI definition's (a)know-it-doesn't-know -> (b)go-retrieve.

A 30% subset of defensive nodes are source=knowledge (marked without retrieval) —
ambiguous (genuine pre-retrieval "I don't know" vs. chose-not-to-retrieve).

Third variable: defensive marking concentrates in L1/L2 (17%) vs L3/L4 (9%),
i.e. the shallow planning/branching layers.

Reproduce: python3 gap-retrieval-node-level.py
Scope: GPU domain, rep-scan era, n=15 runs / 3849 nodes. Single-domain, single-era.
"""
import glob, json, os, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from metacog_axis import DEFENSIVE_RE

DATA = os.path.join(HERE, "..", "data", "rep-scan")


def load_nodes(p):
    t = json.load(open(p))
    return t if isinstance(t, list) else t.get("nodes", [])


def is_def(n):
    return bool(DEFENSIVE_RE.search(
        n.get("claim", "") + " " + n.get("evidence", "") + " " + n.get("corrected_claim", "")))


files = [f for f in glob.glob(os.path.join(DATA, "rep-*.json")) if not f.endswith("scores.json")]
def_nodes, nondef_nodes = [], []
per_run = []
for f in files:
    nodes = load_nodes(f)
    d = [n for n in nodes if is_def(n)]
    nd = [n for n in nodes if not is_def(n)]
    def_nodes += d
    nondef_nodes += nd
    if d and nd:
        ds = sum(1 for x in d if x.get("source") == "search") / len(d)
        ns = sum(1 for x in nd if x.get("source") == "search") / len(nd)
        per_run.append((os.path.basename(f)[:12], ds, ns, len(d)))


def search_frac(nodes):
    return sum(1 for n in nodes if n.get("source") == "search") / len(nodes)


def two_prop_z(p1, n1, p2, n2):
    p = (p1 * n1 + p2 * n2) / (n1 + n2)
    return (p1 - p2) / (p * (1 - p) * (1 / n1 + 1 / n2)) ** 0.5


sd, sn = search_frac(def_nodes), search_frac(nondef_nodes)
z = two_prop_z(sd, len(def_nodes), sn, len(nondef_nodes))
print(f"defensive nodes: {len(def_nodes)}   non-defensive: {len(nondef_nodes)}")
print(f"search fraction: defensive={sd:.3f}  non-defensive={sn:.3f}  (diff {sd - sn:+.3f})")
print(f"two-proportion z = {z:+.2f}  (|z|>1.96 for p<0.05)")
print(f"runs with defensive > non-defensive: "
      f"{sum(1 for _, ds, ns, _ in per_run if ds > ns)}/{len(per_run)}")

print("\nper-run:")
for name, ds, ns, nd in per_run:
    print(f"  {name:12s} def={ds:.2f} nondef={ns:.2f} (n_def={nd})")

print("\ndefensive nodes source x status:")
ct = Counter((n.get("source", ""), n.get("status", "")) for n in def_nodes)
for (s, st), c in ct.most_common():
    print(f"  {s:10s} {st:10s} {c} ({c / len(def_nodes) * 100:.1f}%)")

print("\ndefensive marking by level (third-variable check):")
lv = Counter(n.get("level", "?") for n in def_nodes + nondef_nodes)
dlv = Counter(n.get("level", "?") for n in def_nodes)
for k in sorted(lv):
    print(f"  {k}: total={lv[k]}, defensive={dlv.get(k, 0)} ({dlv.get(k, 0) / lv[k] * 100:.1f}%)")
