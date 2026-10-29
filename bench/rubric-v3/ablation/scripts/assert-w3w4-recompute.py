#!/usr/bin/env python3
"""C3 W3W4 复算断言（RV3G6-draft-revision-batch1，G5 机判化候选 C3）。

目的：stats-w3w4.json 的分数链「hit-matrix + prior-estimates → W0-W4 × 8 run」
必须可独立复算。本脚本从原始冻结数据重新计算全部 40 个分数并与落盘值比对，
任何对 hit-matrix / prior-estimates / stats-w3w4 的单点篡改都会破坏等式被捕获。

公式（stats-w3w4.json recompute_method 字段原文）：
    O3 = Σ w_v·h_v / Σ w_v，直接读 hit-matrix.json + prior-estimates.json 原始数据
权重方案（与 stats-w3w4.json scores 键一致）：
    W0 flat:      w_v = 1
    W1 importance: w_v = w1_v（prior-estimates.nodes[v].w1）
    W2 surprisal:  w_v = w2_v（prior-estimates.nodes[v].w2）
    W3 = w1×w2    W4 = w1+w2

容差：stats-w3w4.json 分数为 4 位小数 → tol = 5e-5（与 G3/G6 既有复验口径一致）。

只读输入：hit-matrix.json / prior-estimates.json / stats-w3w4.json（冻结数据，零修改）。
输出：逐方案 PASS/FAIL + 汇总计数。exit 0 = 全部通过；exit 1 = 存在 FAIL。
SIGNAL 行不影响 exit code。
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
AB = os.path.dirname(HERE)
TOL = 5e-5


def load(name):
    with open(os.path.join(AB, name)) as f:
        return json.load(f)


def main():
    hm = load("hit-matrix.json")
    pe = load("prior-estimates.json")["nodes"]
    sw = load("stats-w3w4.json")

    runs = sorted(hm.keys())
    nodes = sorted(next(iter(hm.values())).keys())
    assert len(runs) == 8 and len(nodes) == 31, f"结构异常: {len(runs)} runs × {len(nodes)} nodes"

    def weight(nid, scheme):
        w1 = pe[nid]["w1"]
        w2 = pe[nid]["w2"]
        if scheme == "W0":
            return 1.0
        if scheme == "W1":
            return w1
        if scheme == "W2":
            return w2
        if scheme == "W3":
            return w1 * w2
        if scheme == "W4":
            return w1 + w2
        raise ValueError(scheme)

    total_fail = 0
    for scheme in ["W0", "W1", "W2", "W3", "W4"]:
        fails = []
        ok = 0
        for run in runs:
            num = sum(weight(nid, scheme) * hm[run][nid]["h"] for nid in nodes)
            den = sum(weight(nid, scheme) for nid in nodes)
            calc = round(num / den, 4)
            disk = sw["scores"][scheme][run]
            if abs(calc - disk) <= TOL:
                ok += 1
            else:
                fails.append((run, calc, disk))
        status = "PASS" if not fails else "FAIL"
        print(f"[{scheme}] {status}: {ok}/8 run 分数复算一致 (tol={TOL:g})")
        for run, calc, disk in fails:
            print(f"  FAIL {scheme}/{run}: 复算={calc} 落盘={disk}")
        total_fail += len(fails)

    print(f"SIGNAL: W0-W4 × 8 run 合计 {'0 mismatch' if total_fail == 0 else str(total_fail) + ' mismatch'}")
    sys.exit(1 if total_fail else 0)


if __name__ == "__main__":
    main()