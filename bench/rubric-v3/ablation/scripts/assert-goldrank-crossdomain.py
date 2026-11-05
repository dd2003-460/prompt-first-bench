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
                                        #   GOLD 清单且题面必须同题面（变体矩阵冻结）。
                                        #   r150：显式声明时成员须 ⊆ nodes 键集（缺失 = exit 2，
                                        #   防判定层静默漏计）；完整「换题面未声明」fail-loud
                                        #   对照协议 = 导出候选（权威源映射表待第二域题面落盘）
        "prompt_version": <str> }       # 题面版本标识。r150 M2 C-最小消费：存在性 + 非空 str
                                        #   机判（缺失/空串/非 str = exit 2）；与 DRAFT v2 冻结
                                        #   快照的内容级对照 = 导出候选（同上）

  judge-blindtest-batch2.json    # 第二域 new-judge 侧（镜像 judge-blindtest-r1.json
                                  #   w3_full_ranking 结构；可整体缺失 = D5 降级）
    = { "judge": <str>, "w3_full_ranking": [ {"node": str, "p_tilde": float|null,
                                              "w1": number, "w2": number, "w3": number},
                                            ... ] }

  prompt-version-gold-map.json    # 「题面版本↔gold_nodes」权威源（r153，本目录根下，
                                  #   非 batch2/ 内）。schema：_schema="prompt-version-gold-map/v1"
                                  #   + domains.<domain_id>.versions.<prompt_version>.gold_nodes。
                                  #   消费方 = load_batch2 C-对照检查（主模式；--lint-only 不触发——
                                  #   lint 是纯 schema 校验且须对既有样例 byte-exact）。
                                  #   文件缺失 = 对照能力不可用 → INFO 降级跳过（T6，不误杀存量调用方）

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

C-对照检查（r153「换题面未声明/错配」fail-loud 承接，权威源 = prompt-version-gold-map.json）：
    P = prior.prompt_version，G = prior.gold_nodes（可缺省），M[P] = 映射表绑定清单
    T1 P∈表 ∧ G 声明 ∧ sorted(G)==sorted(M[P])      → PASS（[PASS] 行）
    T2 P∈表 ∧ G 声明 ∧ 集合不等                      → FAIL exit 2（指名道姓双向列出）
    T3 P∉表（含所属 domain 无条目）                   → SIGNAL exit 0（新域/新版本，不代裁）
    T4 P∈表 ∧ G 缺省 ∧ M[P]≠GOLD_DOMAIN1（排序后）   → SIGNAL exit 0（缺省沿用第一域清单，提示显式声明）
       P∈表 ∧ G 缺省 ∧ M[P]==GOLD_DOMAIN1            → 静默 PASS（缺省值==绑定值，报 SIGNAL 是噪音）
    T6 映射表文件缺失                                → INFO exit 0（对照能力不可用，降级跳过）
    T7 映射表 schema 违例                            → ERROR exit 2（fail-loud）
    注：P 缺失/空串/非 str 由 Y2 先行拦截（本检查不重复该职责）；比较用排序后集合相等
    （gold_nodes 顺序下游零消费，顺序敏感会误判等价声明）。

exit code：0 = 无 FAIL（含 SIGNAL blocked-on-external / (a)(b) verdict 输出 / C-对照 T3/T4 SIGNAL）
           1 = (a) 或 (b) FAIL
           2 = schema 违例 / gold_nodes 键集缺失 / prompt_version 缺失或非空 str 违例
               / C-对照 T2 错配或 T7 映射表 schema 违例 / 输入不可读（ERROR fail-loud）
--lint-only 模式（r147 入口，r150 docstring 补齐）：纯 schema 校验，不跑 (a)/(b) 判定、
           也不触发 C-对照检查（r153 X4 约束：既有 lint 样例的 prompt_version 值不在映射表，
           且 lint 输出须 byte-exact）——
           0 = 全通过（含目录不存在 = 「数据未落盘」SIGNAL / blindtest 缺失 = D5 降级提示）
           2 = schema 违例或输入不可读；lint 模式永不 exit 1
"""
import json
import math
import sys
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]          # bench/rubric-v3/ablation
BATCH2 = BASE / "batch2"
GOLD_MAP = BASE / "prompt-version-gold-map.json"    # r153：题面版本↔gold_nodes 权威源
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


def gold_map_check(pe, batch2_dir):
    """C-对照检查（r153）：prompt_version 声明的题面版本 → 映射表查得 gold 清单 →
    与显式 gold_nodes 一致性机判。真值表 T1-T7 见 docstring「C-对照检查」节。

    返回 (verdict, msg)：
      verdict ∈ {"PASS", "SIGNAL", "FAIL", "INFO"}；msg = 打印文案（PASS/INFO 时由调用方决定静默或打印）。
    消费方：主模式 load_batch2 必触发；--lint-only 默认不触发（X4 byte-exact 约束），
    显式 --check-goldmap 开启时触发且输出并入 lint 报告（r154 (b)，开关关闭时零行为变化）。
    """
    pv = pe["prompt_version"]                       # Y2 已保证非空 str
    if not GOLD_MAP.exists():                        # T6：表缺失 = 对照能力不可用，降级跳过
        return "INFO", ("[INFO] gold-map: prompt-version-gold-map.json absent → "
                        "对照检查跳过（r153 前行为兼容态）")
    try:
        m = json.load(open(GOLD_MAP))
    except (json.JSONDecodeError, OSError) as e:     # T7：表损坏 fail-loud
        return "FAIL", f"[ERROR] gold-map unreadable: {e}"
    if not isinstance(m, dict) or m.get("_schema") != "prompt-version-gold-map/v1" \
            or not isinstance(m.get("domains"), dict):   # T7
        return "FAIL", "[ERROR] gold-map schema violation: _schema/domains missing or wrong type"
    # domain 解析：P 形如 "<family>/<variant>"（family ∈ pre-v3 | v3）；
    # 单域期（当前映射表仅 decomp-hw-27b）取唯一 domain。多域期路由优先级
    # （r154 RV3G3cdx-goldmap-multidomain-upgrade (a) 预注册协议，batch2 数据到来时
    # 由 RV3G3-batch2-arrival-closure goal 同批激活验证）：
    #   ① prior.domain 显式字段存在且 ∈ domains 键集 → 直接采用（权威路由）；
    #   ② prior.domain 存在但 ∉ domains 键集 → SIGNAL exit 0（不代裁新域建表）；
    #   ③ prior.domain 缺省 + 单域期 → 取唯一 domain（兼容态，零行为变化）；
    #   ④ prior.domain 缺省 + 多域期 → 按 P 的 family 前缀匹配 domain 键，
    #      唯一命中才采用；0 个或多个命中 → SIGNAL exit 0（歧义不代裁）。
    dom_field = pe.get("domain")
    if dom_field is not None:
        if not isinstance(dom_field, str) or not dom_field.strip():
            return "FAIL", ("[ERROR] gold-map schema violation: prior.domain must be a "
                            "non-empty str when present (or absent for single-domain default)")
        if dom_field in m["domains"]:
            dom_id = dom_field
        else:
            return "SIGNAL", (f"[SIGNAL] gold-map: prior.domain={dom_field} 未在映射表登记"
                              f"（纯新域）——建表后重跑；本轮不做清单对照（不代裁）")
    elif len(m["domains"]) == 1:
        dom_id = next(iter(m["domains"]))
    else:
        prefix = pv.split("/", 1)[0] if "/" in pv else None
        candidates = [k for k in m["domains"] if prefix is not None and k.startswith(prefix)]
        if len(candidates) != 1:
            return "SIGNAL", (f"[SIGNAL] gold-map: prompt_version={pv} 所属 domain 无法唯一确定"
                              f"（多域期，待 domain 字段路由协议）——本轮不做清单对照（不代裁）")
        dom_id = candidates[0]
    versions = m["domains"][dom_id].get("versions", {})
    entry = versions.get(pv)                        # 版本键 = 完整 prompt_version 字符串
    if entry is None:                                # T3/T5：未登记版本或纯新域——不代裁
        why = (f"prompt_version={pv} 未在映射表登记（新域/新版本）"
               if dom_id in m["domains"]
               else f"prompt_version={pv} 所属 domain 未在映射表登记（纯新域）")
        return "SIGNAL", (f"[SIGNAL] gold-map: {why}——建表后重跑；本轮不做清单对照（不代裁）")
    bound = entry.get("gold_nodes")
    if not (isinstance(bound, list) and all(isinstance(x, str) for x in bound)):
        return "FAIL", (f"[ERROR] gold-map schema violation: domains.{dom_id}.versions.{pv}"
                        f".gold_nodes must be a list of node-id strings")
    declared = pe.get("gold_nodes")                  # load_batch2 上游已校验类型（list[str] 或 None）
    if declared is not None:                         # T1/T2：显式声明 → 集合相等机判
        if sorted(declared) == sorted(bound):
            return "PASS", (f"[PASS] gold-map: prompt_version={pv} 与 gold_nodes 一致"
                            f"（{len(bound)} 节点）")
        return "FAIL", (f"[ERROR] gold-map mismatch: prompt_version={pv} 期望 gold_nodes="
                        f"{bound}，实得 {declared}")
    if sorted(bound) != sorted(GOLD_DOMAIN1):        # T4：缺省沿用第一域清单且 ≠ 绑定清单
        return "SIGNAL", (f"[SIGNAL] gold-map: prompt_version={pv} 已登记但 gold_nodes 未显式声明"
                          f"——缺省沿用 GOLD_DOMAIN1，若 P 绑定清单 ≠ GOLD_DOMAIN1 请显式声明")
    return "PASS", ""                                # 缺省 == 绑定清单：静默 PASS


def load_batch2(base_dir=None):
    """加载第二域三文件；返回 (ok, data_dict_or_error_msg)。

    base_dir：lint 自验入口（--lint-only --dir）与主模式样例矩阵入口（--dir，r153）
    参数化目录，默认约定目录 BATCH2。
    """
    batch2 = Path(base_dir) if base_dir else BATCH2
    if not batch2.is_dir():
        return False, "batch2/ directory absent"
    errs = []
    data = {}
    for fname, key in [("hit-matrix-batch2.json", "hit_matrix"),
                       ("prior-estimates-batch2.json", "prior"),
                       ("judge-blindtest-batch2.json", "blindtest")]:
        p = batch2 / fname
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
    declared = pe.get("gold_nodes")
    if declared is not None:                    # r150 Y1：仅显式声明时查键集（缺省路径零变化）
        missing = [g for g in declared if g not in pe["nodes"]]
        if missing:
            return False, (f"prior-estimates-batch2.json: gold_nodes members absent "
                           f"from nodes key set: {missing}")
    pv = pe.get("prompt_version")               # r150 Y2：M2 C-最小消费（存在性+非空 str）
    if pv is None or not isinstance(pv, str) or not pv.strip():
        return False, "prior-estimates-batch2.json: 'prompt_version' required (non-empty str)"
    verdict, msg = gold_map_check(pe, batch2)   # r153 C-对照检查（主模式；lint 路径不打印）
    if verdict == "FAIL":
        return False, msg[len("[ERROR] "):]     # 走既有 error 通道 → [ERROR] schema violation + exit 2
    data["goldmap"] = (verdict, msg)            # PASS/SIGNAL/INFO 由 main() 打印（lint 模式忽略）
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


def lint_main(base_dir=None, check_goldmap=False):
    """--lint-only 入口：纯 schema 校验（不跑 (a)/(b) 判定），供数据提供方落盘前自验。

    exit：0 = 全通过（含目录不存在 = 「还没写数据」信号 / blindtest 缺失 = D5 降级提示）
          2 = schema 违例或输入不可读
    --check-goldmap（r154 (b)）：开启后 C-对照检查并入 lint 报告——数据提供方落盘前
          一步完成「schema + gold-map 对照」双步自验。默认关闭，既有调用方输出零变化
          （X4 byte-exact）。开启时 T2/T7 FAIL 走 exit 2；T3/T4 SIGNAL 打印但 exit 0
          （新域/未声明属待裁态非错误，与主模式语义一致）。
    """
    ok, payload = load_batch2(base_dir)
    target = base_dir if base_dir else str(BATCH2)
    if not ok:
        if payload == "batch2/ directory absent":
            print(f"[SIGNAL] lint: {target} absent — 数据未落盘，无对象可校验（非错误）")
            sys.exit(0)
        print(f"[ERROR] lint FAIL ({target}): {payload}")
        sys.exit(2)
    for fname in ("hit-matrix-batch2.json", "prior-estimates-batch2.json"):
        print(f"[PASS] {fname}: schema OK")
    if "blindtest" in payload:
        print("[PASS] judge-blindtest-batch2.json: schema OK")
    else:
        print("[INFO] judge-blindtest-batch2.json absent → D5 降级（new 侧不参与对照，合法形态）")
    gold = payload["gold"]
    default_note = "（缺省沿用第一域 GOLD_DOMAIN1）" if gold == GOLD_DOMAIN1 else ""
    print(f"[INFO] gold_nodes={gold}{default_note}, runs={len(payload.get('hit_matrix', {}))}")
    if check_goldmap:                                # r154 (b)：C-对照检查并入 lint 报告
        gm_verdict, gm_msg = payload["goldmap"]
        if gm_verdict == "FAIL":
            print(f"[ERROR] lint FAIL ({target}): {gm_msg[len('[ERROR] '):]}")
            sys.exit(2)
        if gm_msg:                                   # PASS 且静默态 msg 为空 → 不打印
            print(gm_msg)
    print("SUMMARY: lint PASS (3-file schema)")
    sys.exit(0)


def main():
    args = sys.argv[1:]
    if "--lint-only" in args:
        i = args.index("--lint-only")
        base_dir = None
        check_goldmap = "--check-goldmap" in args   # r154 (b)：双步自验开关（默认关闭）
        j = i + 1
        while j < len(args):                        # 跳过 --check-goldmap 等旗标再找 --dir
            if args[j] == "--dir":
                base_dir = args[j + 1] if j + 1 < len(args) else None
                break
            elif not args[j].startswith("--"):
                base_dir = args[j]                  # 位置参数形态
                break
            j += 1
        lint_main(base_dir, check_goldmap)
        return

    # r153：主模式 --dir 参数化（gold-map 样例矩阵消费入口；无参行为零变化）
    main_dir = None
    if "--dir" in args:
        i = args.index("--dir")
        if i + 1 < len(args):
            main_dir = args[i + 1]

    ok, payload = load_batch2(main_dir)
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
    if "goldmap" in payload:                       # r153：C-对照检查 verdict 打印（主模式专属）
        gm_verdict, gm_msg = payload["goldmap"]
        if gm_msg:                                 # PASS 且缺省==绑定清单时 msg 为空 → 静默
            print(gm_msg)
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