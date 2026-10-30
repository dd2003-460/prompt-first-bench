#!/usr/bin/env python3
"""assert-gmr-recompute.py — gmr 主判据复算断言（RV3G6-gmr-tiebreak-prereg）

验证 bench/rubric-v3/gmr-criterion-freeze.md §5 参考值表的每个数值。
数据源：prior-estimates.json (orig) + judge-blindtest-r1.json (new)
协议：rank 0 = 最高权重；并列组内按节点 ID ASCII 字典序；gmr = Σ rank(gold)/5
exit 0 = 全部 PASS, exit 1 = 存在 FAIL
"""
import json, math, sys
from fractions import Fraction as F

BASE = "bench/rubric-v3/ablation"
GOLD = ["N-2.1", "N-3.2.2", "N-2", "N-4", "N-1.3"]
EPS = 0.01

def w2_exact(p):
    if p is None:
        return F(1)
    v = min(-math.log2(float(F(p))), math.log2(1 / EPS))
    return F(v).limit_denominator(10**6) + 1

def gmr_range(ws):
    """Return (lo, hi, id_order) using descending weight, alphabetical id tie-break."""
    items = sorted(ws.items(), key=lambda kv: (-float(kv[1]), kv[0]))
    groups = []
    for nid, w in items:
        if groups and groups[-1][0] == w:
            groups[-1][1].append(nid)
        else:
            groups.append([w, [nid]])

    def gmrr(order_fn):
        r = {}
        pos = 0
        for w, members in groups:
            for i, m in enumerate(order_fn(members)):
                r[m] = pos + i
            pos += len(members)
        return sum(r[g] for g in GOLD) / len(GOLD)

    lo = gmrr(lambda ms: sorted(ms, key=lambda m: (m not in GOLD, m)))
    hi = gmrr(lambda ms: sorted(ms, key=lambda m: (m in GOLD, m)))
    mid = gmrr(lambda ms: sorted(ms))
    return float(lo), float(hi), float(mid)

def main():
    pe = json.load(open(f"{BASE}/prior-estimates.json"))
    bt = json.load(open(f"{BASE}/judge-blindtest-r1.json"))
    nodes = pe["nodes"]

    schemes = {
        "W1": {nid: F(str(d["w1"])) for nid, d in nodes.items()},
        "W2-orig": {nid: w2_exact(d["p_tilde"]) for nid, d in nodes.items()},
        "W3-orig": {nid: F(str(d["w1"])) * w2_exact(d["p_tilde"]) for nid, d in nodes.items()},
        "W4-orig": {nid: F(str(d["w1"])) + w2_exact(d["p_tilde"]) for nid, d in nodes.items()},
        "W2-new": {r["node"]: F(str(r["w2"])) for r in bt["w3_full_ranking"]},
        "W3-new": {r["node"]: F(str(r["w3"])) for r in bt["w3_full_ranking"]},
        "W4-new": {r["node"]: F(str(r["w1"])) + F(str(r["w2"])) for r in bt["w3_full_ranking"]},
    }

    # Expected values from gmr-criterion-freeze.md §5
    expected = {
        "W1": (8.60, 12.40, 10.20),
        "W2-orig": (8.20, 8.40, 8.20),
        "W3-orig": (5.40, 5.40, 5.40),
        "W4-orig": (5.40, 5.40, 5.40),
        "W2-new": (8.80, 10.20, 9.80),
        "W3-new": (7.40, 7.60, 7.60),
        "W4-new": (7.40, 7.60, 7.60),
    }

    passed = failed = 0
    for name, ws in schemes.items():
        lo, hi, mid = gmr_range(ws)
        elo, ehi, emid = expected[name]
        ok = (abs(lo - elo) < 0.005 and abs(hi - ehi) < 0.005 and abs(mid - emid) < 0.005)
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        else:
            failed += 1
        print(f"[{status}] {name:10s} computed=[{lo:.2f},{hi:.2f}] id={mid:.2f}  expected=[{elo:.2f},{ehi:.2f}] id={emid:.2f}")

    # Extra checks
    # W3-orig must be tie-robust (lo == hi)
    lo, hi, _ = gmr_range(schemes["W3-orig"])
    robust = "PASS" if lo == hi else "FAIL"
    print(f"[{robust}] W3-orig tie-robust (lo==hi: {lo==hi})")
    if lo != hi:
        failed += 1
    else:
        passed += 1

    # N-1/N-2 exact tie at w3=10.0 in new judge
    w3n = {r["node"]: F(str(r["w3"])) for r in bt["w3_full_ranking"]}
    tie = w3n.get("N-1") == w3n.get("N-2") == F(10)
    status = "PASS" if tie else "FAIL"
    print(f"[{status}] N-1/N-2 w3 exact tie at 10.0 (N-1={w3n.get('N-1')}, N-2={w3n.get('N-2')})")
    if tie:
        passed += 1
    else:
        failed += 1

    # Hypergeometric anchor: E[X]=1.6129, P(X>=4)=0.027438
    from math import comb
    n, k, r = 31, 5, 10
    ex = k * r / n
    p4 = sum(comb(k, i) * comb(n - k, r - i) for i in range(4, k + 1)) / comb(n, r)
    ok_ex = abs(ex - 1.6129) < 0.0001
    ok_p4 = abs(p4 - 0.027438) < 0.000001
    print(f"[{'PASS' if ok_ex else 'FAIL'}] hypergeom E[X]={ex:.4f} (expected 1.6129)")
    print(f"[{'PASS' if ok_p4 else 'FAIL'}] hypergeom P(X>=4)={p4:.6f} (expected 0.027438)")
    passed += ok_ex + ok_p4
    failed += (not ok_ex) + (not ok_p4)

    print(f"\n=== {passed} PASS / {failed} FAIL ===")
    sys.exit(1 if failed else 0)

if __name__ == "__main__":
    main()