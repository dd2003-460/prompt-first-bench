#!/usr/bin/env python3
"""Per-layer anatomy for the 30 era-matched GPU trees (K7 15 + rep-scan 15).

Recompute the §4.4 per-layer table from FULL node data (K7: archive checkpoint
node.json trees, deduped by id keeping latest mtime; rep-scan: run-json).
Finds the earlier draft table OMITTED L5 (761 nodes, only in the two 719-budget
trees with max_depth=5): header said 8,767 nodes but the table summed to 8,006.

Reproduce: python3 per-layer-anatomy-30trees.py
"""
import glob, json, os, re
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
# research/ -> B-pipeline-ablation/ -> modules/ -> pfb root
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
K7 = os.path.join(ROOT, "experiments", "stage-ablation", "checkpoints", "archive")
REP = os.path.join(HERE, "..", "data", "rep-scan")


def load_k7_tree(archive_dir):
    best = {}
    for f in glob.glob(archive_dir + "/**/node.json", recursive=True):
        try:
            n = json.load(open(f))
        except Exception:
            continue
        nid = n.get("id")
        if nid is None:
            continue
        mt = os.path.getmtime(f)
        if nid not in best or mt > best[nid][0]:
            best[nid] = (mt, n)
    return [v[1] for v in best.values()]


def load_rep_nodes(f):
    t = json.load(open(f))
    return t if isinstance(t, list) else t.get("nodes", [])


trees = []
for f in sorted(glob.glob(os.path.join(K7, "budget-*"))):
    m = re.search(r"budget-(\d+)-r(\d+)", os.path.basename(f))
    if not m:
        continue
    trees.append((f"K7-{m.group(1)}-r{m.group(2)}", int(m.group(1)), load_k7_tree(f)))
for f in glob.glob(os.path.join(REP, "rep-*.json")):
    if f.endswith("scores.json"):
        continue
    m = re.search(r"rep-(\d+)-r(\d+)", os.path.basename(f))
    if not m:
        continue
    trees.append((f"REP-{m.group(1)}-r{m.group(2)}", int(m.group(1)), load_rep_nodes(f)))

layer = defaultdict(Counter)
max_depths = []
for name, budget, nodes in trees:
    lv_max = max(int(str(n.get("level", "L1")).lstrip("L")) for n in nodes)
    max_depths.append((name, budget, lv_max, len(nodes)))
    for n in nodes:
        lv = int(str(n.get("level", "L1")).lstrip("L"))
        layer[lv]["total"] += 1
        layer[lv][n.get("status", "?")] += 1

tot = sum(v["total"] for v in layer.values())
print(f"trees={len(trees)}  total_nodes={tot}")
for lv in sorted(layer):
    c = layer[lv]
    v, dg, pd = c.get("verified", 0), c.get("degraded", 0), c.get("pending", 0)
    print(f"L{lv}: total={c['total']} verified={v} degraded={dg} pending={pd} "
          f"ver%={v / c['total'] * 100:.1f}")

by_tier = defaultdict(lambda: [0, 0])
for name, budget, md, nn in max_depths:
    by_tier[budget][1] += 1
    if md < 4:
        by_tier[budget][0] += 1
print("\nno-L4 by tier:")
for b in sorted(by_tier):
    a, t = by_tier[b]
    print(f"  budget {b}: {a}/{t}")
