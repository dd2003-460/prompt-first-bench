#!/usr/bin/env python3
"""C4 w2 公式断言（RV3G6-draft-revision-batch1，G5 机判化候选 C4）。

目的：消除「p̃ 层纸面协议零防护力」（G4 S3 降档教训）——把 prior-estimates.json /
judge-blindtest-r1.json 中每个节点的 w2 值与公式逐节点复算比对，任何未来对冻结
JSON 的篡改（或新 judge 文件加入时的公式偏离）都会被本脚本捕获。

公式（prior-estimates.json weight_formula 字段原文）：
    w_v = 1 + min(-log2(p_tilde_v), log2(1/epsilon))，epsilon = 0.01（cap ≈ 6.6439）
根节点政策（root_policy 字段原文）：N-0 p_tilde=null → w2 = 1.0（中性权重）。

容差策略（02.5 M3 修正）：按落盘精度分侧取容差——
    orig 侧（prior-estimates.json）w2 为 4 位小数 → tol = 5e-5
    new  侧（judge-blindtest-r1.json）w2 为 3 位小数 → tol = 5e-4
统一用 5e-5 会在 new 侧产生理论误报（3 位值是 4 位值的进一步舍入，最大偏差 5e-4）。

只读输入：prior-estimates.json / judge-blindtest-r1.json（冻结数据，零修改）。
输出：逐节点 PASS/FAIL + 汇总计数。exit 0 = 全部通过；exit 1 = 存在 FAIL。
SIGNAL 行不影响 exit code。
"""
import json, math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
AB = os.path.dirname(HERE)


def load(name):
    with open(os.path.join(AB, name)) as f:
        return json.load(f)


def expected_w2(p, eps):
    """公式复算。p=None → 根节点政策 1.0。"""
    if p is None:
        return 1.0
    cap = math.log2(1.0 / eps)
    return 1.0 + min(-math.log2(p), cap)


def check_file(path, tag, tol):
    data = load(path)
    nodes = data["nodes"]
    eps = data.get("epsilon")
    if eps is None:
        # blindtest 文件无 epsilon 字段，沿用 orig 侧声明值（同一协议）
        eps = load("prior-estimates.json")["epsilon"]
    fails = []
    ok = 0
    null_count = 0
    for nid in sorted(nodes):
        n = nodes[nid]
        p = n["p_tilde"]
        w2_disk = n["w2"]
        w2_calc = expected_w2(p, eps)
        if p is None:
            null_count += 1
        if abs(w2_calc - w2_disk) <= tol:
            ok += 1
        else:
            fails.append((nid, p, w2_calc, w2_disk, abs(w2_calc - w2_disk)))
    total = len(nodes)
    status = "PASS" if not fails else "FAIL"
    print(f"[{tag}] {status}: {ok}/{total} 节点 w2 复算一致 (tol={tol:g}, null→1.0 节点 {null_count})")
    for nid, p, calc, disk, d in fails:
        print(f"  FAIL {nid}: p_tilde={p} 公式值={calc:.6f} 落盘值={disk} |Δ|={d:.6f}")
    return len(fails)


def main():
    total_fail = 0
    total_fail += check_file("prior-estimates.json", "orig-judge", 5e-5)
    total_fail += check_file("judge-blindtest-r1.json", "new-judge", 5e-4)
    print(f"SIGNAL: 双 judge 合计 {'0 mismatch' if total_fail == 0 else str(total_fail) + ' mismatch'}")
    sys.exit(1 if total_fail else 0)


if __name__ == "__main__":
    main()