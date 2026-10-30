#!/usr/bin/env python3
"""assert-goldrank-crossdomain.py — batch2 跨域重验断言骨架（RV3G3-threshold-crossdomain-reverify）

机判对象：bench/rubric-v3/goldrank-threshold-proof.md L4.2「改回 top-10 为主判据」的
条件 (a) t=4 过线集合跨域稳定性 + (b) tie-sensitivity 审计（第二域数据到来后重验）。
本脚本为 **schema 预注册骨架**（同 r136 assert-kappa-receipt.py 模式）：batch2 数据
未到来时对当前 ablation 面常态输出 SIGNAL blocked-on-external + exit 0（不伪造数据
转绿）；数据落盘后零改动接入。

────────────────────────────────────────────────────────────
输入 schema 预注册（最小字段集，每字段带理由）
────────────────────────────────────────────────────────────
约定目录：bench/rubric-v3/ablation/batch2/（不存在 = blocked-on-external）

  hit-matrix-batch2.json   # 第二域 hit-matrix（h 值载体；(a)/(b) 复算协议本身不消费
                           #   h 值——与第一域 assert-goldrank-threshold.py ⑤ 同协议，
                           #   只需权重侧输入；此文件是未来 claim 级判据的组成部分，
                           #   schema 存在性仍校验防半套数据）
    = { "<run_id>": { "<node_id>": {"h": 0|1, "evidence": str|null}, ... }, ... }
    最小规模：≥1 run × ≥5 gold 节点可定位（gold_nodes 声明的成员必须全部出现）

  prior-estimates-batch2.json   # 第二域 orig-judge 权重（镜像第一域 nodes 结构）
    = { "nodes": { "<node_id>": {"parent_id": str|null, "p_tilde": float|null,
                                 "w1": <number>, "w2": <number>|null,
                                 "parent_share": <number>|null}, ... },
        "gold_nodes": [<node_id> x5],   # D1：换题面时必须显式声明；缺省 = 沿用第一域
                                        #   GOLD 清单且题面必须同题面（变体矩阵冻结），
                                        #   换题面而未声明 = ERROR fail-loud
        "prompt_version": <str> }       # 题面版本标识（与 DRAFT v2 冻结快照对照用）

  judge-blindtest-batch2.json    # 第二域 new-judge 侧（镜像 judge-blindtest-r1.json
                                  #   w3_full_ranking 结构；可整体缺失 = D5 降级）
    = { "judge": <str>, "w3_full_ranking": [ {"node": str, "p_tilde": float|null,
                                              "w1": number, "w2": number, "w3": number},
                                            ... ] }

方案权重合成（与第一域权威实现逐字同协议，assert-goldrank-threshold.py L90-99）：
  W1      = w1                    W2-orig = w2_exact(p_tilde)
  W3-orig = w1 × w2_exact         W4-orig = w1 + w2_exact
  W2-new  = w2                    W3-new  = w3            W4-new = w1 + w2
  w2_exact(p): p is None → F(1)；否则 F(min(-log2(F(p)), log2(1/EPS))).limit_denominator(10**6) + 1，EPS=0.01

────────────────────────────────────────────────────────────
判定语义（设计决策 D3/D5，预注册——成璐可推翻项，见 04.5）
────────────────────────────────────────────────────────────
S1 = 第一域 t=4 过线集合 = {W3-orig, W4-orig, W3-new}（goldrank-threshold-proof.md L57/L83）
S2 = 第二域各方案 top-10 gold 计数 ≥4 的方案集合（仅含两域同名方案——D5 交集对照）

(a) 跨域稳定：S2 == S1∩(第二域实际方案) → PASS
             |S2| == |S1∩…| 但成员不同     → SIGNAL（人工裁决）
             否则                          → FAIL
(b) tie-sensitivity：对第二域每个过线方案做全量合法 tie-break 可达计数审计
    （DP 席位预算法，R2 引理：只有跨 cut 并列组影响 top-10 gold 计数）
    所有过线方案可达计数恒 ≥4 → PASS；任一过线方案存在 <4 可达值 → FAIL
    （tie-sensitive 方案的 t=4 读数须带限定语引用——freeze §4 规则 1 类推）

exit code：0 = 无 FAIL（含 SIGNAL blocked-on-external / (a)(b) verdict 输出）
           1 = (a) 或 (b) FAIL
           2 = schema 违例 / 换题面无 gold_nodes 声明 / 输入不可读（ERROR fail-loud）
"""
import json
import math
import sys
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]          # bench/rubric-v3/ablation
BATCH2 = BASE / "batch2"
GOLD_DOMAIN1 = ["N-2.1", "N-3.2.2", "N-2", "N-4", "N-1.3"]
S1 = {"W3-orig", "W4-orig", "W3-new"}               # 第一域 t=4 过线集合（proof L57）
T_PASS = 4                                          # t=4 严判据（proof L55 推荐）
EPS = 0.01


def w2_exact(p):
    """与 assert-goldrank-threshold.py L38-42 逐字同协议。"""
    if p is None:
        return F(1)
    v = min(-math.log2(float(F(p))), math.log2(1 / EPS))
    return F(v).limit_denominator(10 ** 6) + 1


def build_schemes(nodes, blindtest=None):
    """七方案合成（第一域协议）。blindtest=None 时只产 orig 侧四方案（D5 降级）。"""
    schemes = {
        "W1": {nid: F(str(d["w1"])) for nid, d in nodes.items()},
        "W2-orig": {nid: w2_exact(d["p_tilde"]) for nid, d in nodes.items()},
        "W3-orig": {nid: F(str(d["w1"])) * w2_exact(d["p_tilde"]) for nid, d in nodes.items()},
        "W4-orig": {nid: F(str(d["w1"])) + w2_exact(d["p_tilde"]) for nid, d in nodes.items()},
    }
    if blindtest:
        for r in blindtest["w3_full_ranking"]:
            schemes.setdefault("W2-new", {})[r["node"]] = F(str(r["w2"]))
            schemes.setdefault("W3-new", {})[r["node"]] = F(str(r["w3"]))
            schemes.setdefault("W4-new", {})[r["node"]] = F(str(r["w1"])) + F(str(r["w2"]))
    return schemes


def top10_gold_count(ws, gold):
    """top-10 gold 计数。排序键 (-w, nid)，w 为 Fraction（X1 处置：比 float 更严格）。"""
    items = sorted(ws.items(), key=lambda kv: (-kv[1], kv[0]))
    return sum(nid in gold for nid, _ in items[:10])


def reachable_top10_gold_counts(ws, gold):
    """全量合法 tie-break 下 top-10 gold 计数的可达集合（R2 DP 席位预算法）。

    引理：只有跨越 rank 10/11 cut 的并列组能改变计数。按 (-w, id) 基准序分组后，
    设跨 cut 组为 G₁..Gₘ（第 j 组大小 s_j、gold 数 g_j、基准序下在 top-10 内的成员数
    b_j = 10 − lo_pos_j）；非跨 cut 组的 gold 贡献 c_fixed 恒定（整组在 cut 上方者全计）。
    合法 tie-break = 各组内部任意排列 → 第 j 组排进 top-10 的成员数 k_j ∈ [max(0, s_j − o_j),
    min(s_j, b_j)]（o_j = s_j − b_j 为基准序下组外成员数），且 Σk_j ≤ 10 全局席位约束；
    该组贡献 gold 数 gg_j ∈ [max(0, k_j − (s_j − g_j)), min(k_j, g_j)]。
    DP 状态 = (已用席位数, 累计 gold)。返回 sorted set of 可达总计数。

    实现注记（精确预算约束）：不同权重组之间不可交错——cut 上方的组永远排在 cut 下方
    的组之前。故所有跨 cut 组的席位占用之和被钉死：Σk_j == 10 − above_members
    （above_members = 整组在 cut 上方的组成员总数）。DP 转移仍枚举 k 从 0 起（单组内
    k 的下限 max(0, s−b) 在多组交互下不成立——后面的组会占据部分组外位置），但终态
    只保留 used == 10 − above_members 的状态；其余状态物理不可达（M0 fuzz 暴力互验）。
    """
    items = sorted(ws.items(), key=lambda kv: (-kv[1], kv[0]))
    groups = []
    for nid, w in items:
        if groups and groups[-1][0] == w:
            groups[-1][1].append(nid)
        else:
            groups.append([w, [nid]])

    fixed_gold = 0
    above_members = 0                            # 整组在 cut 上方的组成员总数（席位预算锚）
    crossing = []
    pos = 0                                          # 累计名次（组序 ≠ 名次起点，须累加前组大小）
    for w, members in groups:
        lo_pos, hi_pos = pos, pos + len(members) - 1  # 基准序名次区间（0-based）
        if hi_pos < 10:                                # 整组在 cut 上方（全进 top-10）
            fixed_gold += sum(m in gold for m in members)
            above_members += len(members)
        elif lo_pos >= 10:                             # 整组在 cut 下方（全不进）
            pass
        else:                                          # 跨 cut 组
            b = 10 - lo_pos                            # 基准序下组内进 top-10 的成员数
            crossing.append({"s": len(members), "g": sum(m in gold for m in members),
                             "b_hi": min(len(members), b)})
        pos += len(members)

    reachable = {(0, 0)}  # (used_seats, gold_from_crossing)
    for c in crossing:
        nxt = set()
        for used, gcnt in reachable:
            # k ∈ [0, min(b_hi, 10 − used)]（见 docstring 实现注记：终态再按精确预算过滤）
            k_hi = min(c["b_hi"], 10 - used)
            for k in range(0, k_hi + 1):
                g_lo = max(0, k - (c["s"] - c["g"]))
                g_hi = min(k, c["g"])
                for gg in range(g_lo, g_hi + 1):
                    nxt.add((used + k, gcnt + gg))
        reachable = nxt
    budget = 10 - above_members                     # 跨 cut 组合计必须占满的席位数
    counts = {fixed_gold + gc for u, gc in reachable if u == budget}
    return sorted(counts)


def brute_force_top10_gold_counts(ws, gold):
    """暴力全枚举（仅用于 M0 小样例互验，置换总数受限调用方保证）。"""
    items = sorted(ws.items(), key=lambda kv: (-kv[1], kv[0]))
    groups = []
    for nid, w in items:
        if groups and groups[-1][0] == w:
            groups[-1][1].append(nid)
        else:
            groups.append([w, [nid]])
    out = set()
    group_perms = [list(permutations(m)) for _, m in groups]
    def rec(i, seq):
        if i == len(groups):
            out.add(sum(nid in gold for nid in seq[:10]))
            return
        for perm in group_perms[i]:
            rec(i + 1, seq + list(perm))
    rec(0, [])
    return sorted(out)


def load_batch2():
    """加载第二域三文件；返回 (ok, data_dict_or_error_msg)。"""
    if not BATCH2.is_dir():
        return False, "batch2/ directory absent"
    errs = []
    data = {}
    for fname, key in [("hit-matrix-batch2.json", "hit_matrix"),
                       ("prior-estimates-batch2.json", "prior"),
                       ("judge-blindtest-batch2.json", "blindtest")]:
        p = BATCH2 / fname
        if not p.exists():
            if key != "blindtest":      # blindtest 可缺（D5 降级）
                errs.append(f"{fname} missing")
            continue
        try:
            data[key] = json.load(open(p))
        except (json.JSONDecodeError, OSError) as e:
            errs.append(f"{fname} unreadable: {e}")
    if errs:
        return False, "; ".join(errs)
    # schema 违例检查
    pe = data["prior"]
    if "nodes" not in pe or not isinstance(pe["nodes"], dict):
        return False, "prior-estimates-batch2.json: 'nodes' object required"
    gold = pe.get("gold_nodes")
    if gold is None:
        gold = GOLD_DOMAIN1              # D1 默认沿用（同题面冻结）
    elif not (isinstance(gold, list) and all(isinstance(x, str) for x in gold)):
        return False, "gold_nodes must be a list of node-id strings"
    for nid, d in pe["nodes"].items():
        for f in ("w1",):
            if f not in d:
                return False, f"nodes.{nid}: field '{f}' required"
        if "p_tilde" not in d:
            return False, f"nodes.{nid}: field 'p_tilde' required (null allowed)"
    if "hit_matrix" in data:
        for rid, cells in data["hit_matrix"].items():
            for nid in gold:
                if nid not in cells:
                    return False, f"hit-matrix {rid}: gold node {nid} absent"
    if "blindtest" in data:
        for r in data["blindtest"].get("w3_full_ranking", []):
            for f in ("node", "w1", "w2", "w3"):
                if f not in r:
                    return False, f"w3_full_ranking entry missing '{f}': {r}"
    data["gold"] = gold
    return True, data


def main():
    ok, payload = load_batch2()
    if not ok:
        if payload == "batch2/ directory absent":
            print("[SIGNAL] blocked-on-external: batch2 data absent "
                  "(等 batch2 数据落盘 bench/rubric-v3/ablation/batch2/ 后零改动接入)")
            print(f"[INFO] 预注册锚点: S1={sorted(S1)}, T_PASS={T_PASS}, "
                  f"GOLD_DOMAIN1={GOLD_DOMAIN1}")
            sys.exit(0)
        print(f"[ERROR] schema violation: {payload}")
        sys.exit(2)

    pe, gold = payload["prior"], payload["gold"]
    bt = payload.get("blindtest")
    schemes = build_schemes(pe["nodes"], bt)
    if bt is None:
        print("[SIGNAL] D5 降级: judge-blindtest-batch2.json 缺失 → new 侧方案不参与对照")

    # (a) 跨域稳定
    s2 = {name for name, ws in schemes.items()
          if top10_gold_count(ws, gold) >= T_PASS}
    comparable = S1 & set(schemes)          # D5 交集
    counts = {name: top10_gold_count(ws, gold) for name, ws in schemes.items()}
    print(f"[INFO] 第二域 top-10 gold 计数: {counts}")
    print(f"[INFO] S2={sorted(s2)} vs S1∩域={sorted(comparable)}")
    a_verdict = "PASS" if s2 == comparable else (
        "SIGNAL" if len(s2) == len(comparable) else "FAIL")
    print(f"[{a_verdict}] (a) 跨域稳定: {'S2==S1∩域' if a_verdict=='PASS' else '成员/计数不一致'}")

    # (b) tie-sensitivity
    b_fail = []
    for name in sorted(s2):
        reach = reachable_top10_gold_counts(schemes[name], gold)
        robust = all(c >= T_PASS for c in reach)
        tag = "tie-robust" if robust else "tie-sensitive"
        print(f"[INFO] (b) {name} 可达 top-10 gold 计数集合 = {reach} ({tag})")
        if not robust:
            b_fail.append(name)
    b_verdict = "PASS" if not b_fail else "FAIL"
    detail = "" if not b_fail else f" — tie-sensitive 过线方案: {b_fail}"
    print(f"[{b_verdict}] (b) tie-sensitivity 审计{detail}")

    fails = (a_verdict == "FAIL") or (b_verdict == "FAIL")
    print(f"\nSUMMARY: (a)={a_verdict} (b)={b_verdict}")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()