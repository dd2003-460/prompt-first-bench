#!/usr/bin/env python3
"""assert-goldrank-threshold.py — goldrank 阈值论证防漂移断言（RV3G3-goldrank-threshold-proof）

校验：
  ① 论证文档 bench/rubric-v3/goldrank-threshold-proof.md 存在且含精确基线值
     （50/31、74/2697、158/899、0.027438、0.175751 字符串）
  ② freeze doc §2.1 不再含未回填占位语「threshold_top10 := RV3G3-goldrank-threshold-proof 产出值」，
     且已指向 goldrank-threshold-proof.md
  ③ freeze doc §2.3 门禁行状态已翻 ✅（含「✅ 完成」且不再含「❌ 未完成（queue 中）」）
  ④ 超几何现场 Fraction 复算 == 文档声明值（E[X]=50/31, P≥3=158/899, P≥4=74/2697, P≥5=4/2697），
     且 L1 表行逐格存在（防「篡改 L1 单元格但 token 仍残留在 L2」逃逸）
  ⑤ 当前数据 top-10 gold 计数复算 == 文档 L2 表（W1=3, W2-orig=3, W3-orig=4, W4-orig=4,
     W2-new=2, W3-new=4, W4-new=3；tie-break = 节点 ID 字典序，与 assert-gmr-recompute.py 同协议），
     且 L2 实测表行逐格存在（防文档表文本被篡改而现场复算不受影响）
exit 0 = 全部 PASS, exit 1 = 存在 FAIL
"""
import json, math, re, sys
from fractions import Fraction as F
from math import comb

BASE = "bench/rubric-v3"
ABLA = f"{BASE}/ablation"
PROOF = f"{BASE}/goldrank-threshold-proof.md"
FREEZE = f"{BASE}/gmr-criterion-freeze.md"
GOLD = ["N-2.1", "N-3.2.2", "N-2", "N-4", "N-1.3"]
EPS = 0.01

def w2_exact(p):
    if p is None:
        return F(1)
    v = min(-math.log2(float(F(p))), math.log2(1 / EPS))
    return F(v).limit_denominator(10**6) + 1

def main():
    passed = failed = 0
    def check(name, ok, detail=""):
        nonlocal passed, failed
        status = "PASS" if ok else "FAIL"
        if ok: passed += 1
        else: failed += 1
        print(f"[{status}] {name}" + (f" — {detail}" if detail and not ok else ""))

    proof = open(PROOF).read()
    freeze = open(FREEZE).read()

    # ① 文档存在且含精确基线值
    for token in ["50/31", "74/2697", "158/899", "0.027438", "0.175751"]:
        check(f"① 论证文档含 {token}", token in proof)

    # ② freeze §2.1 回填完成
    check("② freeze 不含未回填占位符",
          "threshold_top10 := RV3G3-goldrank-threshold-proof 产出值" not in freeze)
    check("② freeze §2.1 指向论证文档", "goldrank-threshold-proof.md" in freeze)

    # ③ freeze §2.3 门禁翻转
    check("③ freeze 门禁行含 ✅ 完成", "✅ 完成" in freeze)
    check("③ freeze 不再含 ❌ 未完成（queue 中）", "❌ 未完成（queue 中）" not in freeze)

    # ④ 超几何现场复算 == 文档值
    n, k, r = 31, 5, 10
    tot = comb(n, r)
    exact = {t: F(sum(comb(k, i) * comb(n - k, r - i) for i in range(t, k + 1)), tot)
             for t in (3, 4, 5)}
    expect_frac = {"P(X≥3)": ("158/899", exact[3]),
                   "P(X≥4)": ("74/2697", exact[4]),
                   "P(X≥5)": ("4/2697", exact[5])}
    for label, (doc_str, calc) in expect_frac.items():
        check(f"④ {label} 文档 {doc_str} == 现场复算 {calc.numerator}/{calc.denominator}",
              F(doc_str) == calc and doc_str in proof)
    check("④ E[X] 文档 50/31 == 现场复算", F("50/31") == F(k * r, n))
    # L1 表行逐格存在（防篡改 L1 单元格而 token 残留在 L2 的逃逸路径）
    l1_rows = [
        "| E[X] | **50/31** | 1.612903… |",
        "| P(X≥1) | 2374/2697 | 0.880237 |",
        "| P(X≥2) | 1424/2697 | 0.527994 |",
        "| P(X≥3) | 158/899 | 0.175751 |",
        "| P(X≥4) | 74/2697 | 0.027438 |",
        "| P(X≥5) | 4/2697 | 0.001483 |",
    ]
    for row in l1_rows:
        check(f"④ L1 表行存在: {row.split('|')[2].strip()}", row in proof)

    # ⑤ top-10 gold 计数复算 == 文档 L2 表
    pe = json.load(open(f"{ABLA}/prior-estimates.json"))
    bt = json.load(open(f"{ABLA}/judge-blindtest-r1.json"))
    nodes = pe["nodes"]
    schemes = {
        "W1": {nid: F(str(d["w1"])) for nid, d in nodes.items()},
        "W2-orig": {nid: w2_exact(d["p_tilde"]) for nid, d in nodes.items()},
        "W3-orig": {nid: F(str(d["w1"])) * w2_exact(d["p_tilde"]) for nid, d in nodes.items()},
        "W4-orig": {nid: F(str(d["w1"])) + w2_exact(d["p_tilde"]) for nid, d in nodes.items()},
        "W2-new": {r_["node"]: F(str(r_["w2"])) for r_ in bt["w3_full_ranking"]},
        "W3-new": {r_["node"]: F(str(r_["w3"])) for r_ in bt["w3_full_ranking"]},
        "W4-new": {r_["node"]: F(str(r_["w1"])) + F(str(r_["w2"])) for r_ in bt["w3_full_ranking"]},
    }
    expected_counts = {"W1": 3, "W2-orig": 3, "W3-orig": 4, "W4-orig": 4,
                       "W2-new": 2, "W3-new": 4, "W4-new": 3}
    for name, ws in schemes.items():
        items = sorted(ws.items(), key=lambda kv: (-float(kv[1]), kv[0]))
        cnt = sum(nid in GOLD for nid, _ in items[:10])
        check(f"⑤ {name} top-10 gold 计数 == {expected_counts[name]}",
              cnt == expected_counts[name], f"实算 {cnt}")
    # L2 实测表行逐格存在（防文档表文本被篡改而现场复算不受影响）
    l2_rows = [
        "| W1-orig / W1-new | 3 / 3 | 10.20 |",
        "| W2-orig | 3 | 8.20 |",
        "| W3-orig / W4-orig | 4 / 4 | 5.40 |",
        "| W2-new | 2 | 9.80 |",
        "| W3-new / W4-new | 4 / 3 | 7.60 |",
    ]
    for row in l2_rows:
        check(f"⑤ L2 表行存在: {row.split('|')[2].strip()}", row in proof)

    print(f"\nSUMMARY: {passed} PASS / {failed} FAIL")
    sys.exit(0 if failed == 0 else 1)

if __name__ == "__main__":
    main()