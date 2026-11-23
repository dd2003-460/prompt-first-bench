#!/usr/bin/env python3
"""Cross-domain node-level (a)<->(b) coupling — from ARCHIVE checkpoints.

CORRECTS Supplementary 30 (b28ba91ff), which wrongly claimed the 48 nat/soc
runs' node-level data were "unrecoverable" because the 83-run corpus only stores
run-level aggregates. That claim was made WITHOUT checking checkpoints/archive/,
which holds 21 sm-nat-* + 21 sm-soc-* archives, each with r1/r2/r3 node.json
trees (full source/status/claim/evidence/corrected_claim). 5836 nat + 10442 soc
node.json files exist.

This script collects every node.json across all archives, dedupes by
(id, level, source, status, claim-prefix) so a node re-archived across resume
cycles is counted once, then computes the defensive-vs-nondefensive search-source
fraction per domain (the node-level (a)<->(b) coupling test).

Reproduce: python3 gap-retrieval-cross-domain-archive.py
Scope: nat + soc domains, all archived runs (11-20..11-22 era). GPU already done
in gap-retrieval-node-level.py (15 rep-scan runs).
"""
import glob, json, os, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from metacog_axis import DEFENSIVE_RE

STAGE = os.path.join(HERE, "..", "..", "..", "experiments", "stage-ablation")
ARCHIVE = os.path.join(STAGE, "checkpoints", "archive")


def is_def(n):
    return bool(DEFENSIVE_RE.search(
        str(n.get("claim", "")) + " " + str(n.get("evidence", "")) + " " +
        str(n.get("corrected_claim", ""))))


def dedup_key(n):
    return (n.get("id"), str(n.get("level", "")), n.get("source"),
            n.get("status"), str(n.get("claim", ""))[:60])


def two_prop_z(p1, n1, p2, n2):
    if n1 == 0 or n2 == 0:
        return float("nan")
    p = (p1 * n1 + p2 * n2) / (n1 + n2)
    if not (0 < p < 1):
        return float("nan")
    return (p1 - p2) / (p * (1 - p) * (1 / n1 + 1 / n2)) ** 0.5


for dom in ["nat", "soc"]:
    seen = set()
    def_nodes, nondef_nodes = [], []
    n_files = 0
    for f in glob.glob(os.path.join(ARCHIVE, f"sm-{dom}-*", f"sm-{dom}-r*", "**", "node.json"), recursive=True):
        try:
            n = json.load(open(f))
        except Exception:
            continue
        n_files += 1
        k = dedup_key(n)
        if k in seen:
            continue
        seen.add(k)
        (def_nodes if is_def(n) else nondef_nodes).append(n)

    sd = sum(1 for n in def_nodes if n.get("source") == "search") / len(def_nodes) if def_nodes else 0
    sn = sum(1 for n in nondef_nodes if n.get("source") == "search") / len(nondef_nodes) if nondef_nodes else 0
    z = two_prop_z(sd, len(def_nodes), sn, len(nondef_nodes))
    print(f"{dom:4s}: {n_files} node.json files, {len(seen)} unique nodes "
          f"({len(def_nodes)} def / {len(nondef_nodes)} nondef)")
    print(f"      search fraction: def={sd:.3f}  nondef={sn:.3f}  (diff {sd - sn:+.3f})  z={z:+.2f}")
    ct = Counter(n.get("source", "?") for n in def_nodes)
    print(f"      def source dist: {dict(ct)}")
