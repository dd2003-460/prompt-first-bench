#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_j3a_properties.py — J3a S2 机械检查：从 S1 JSON 生成 j3a-hierarchy.md 的 §1/§4/§2 线索
# origin: ai · 2026-11-26 · 载体修正（同 S1）：三性质里 §1 树形/§4 覆盖/§2 shared 线索是机械检查，
#   不该派 reasoning sub（27b 在"想"阶段烧光输出预算，J3a 家族 4 次同死因）。
#   本脚本生成机械部分落盘；§2 正交判断/§3 最小/§5 作用域由 Lead 基于本脚本输出做品味判断后追加。
# 用法: python3 verify_j3a_properties.py  （pfb-thinkmech 根目录）
# 产出: modules/G-think-mechanism/think-trigger/exp-results/j3a-hierarchy.md（§1/§4/§2 线索 + §3/§5 占位）
"""
import json, os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
SRC  = os.path.join(ROOT, "modules/G-think-mechanism/think-trigger/exp-results/j3a-factors.json")
OUT  = os.path.join(ROOT, "modules/G-think-mechanism/think-trigger/exp-results/j3a-hierarchy.md")

# c_pass 公式结构（来自 gold-tree 公式行 + calc.py，固定）：
# c_pass = c_hour / (u × λ_raw × G_pass)
# 每个公式参数 → 它由哪些叶子 param 支撑（覆盖检查的"应覆盖"清单，用真实 leaf param 名）
FORMULA_PARAMS = {
    "c_hour/摊销": ["gpu_price", "host_price", "resid", "H"],
    "c_hour/电费": ["power_kw", "elec"],
    "c_hour/故障": ["p_fail", "gpu_price"],
    "u": ["duty_demand", "sched_eff"],
    "λ_raw/prefill": ["prefill_flops", "tf_peak", "mfu"],
    "λ_raw/decode": ["w_bytes", "kv_per_stream", "bw_peak", "eta_bw"],
    "G_pass": [],  # nuisance, stopped, 无分解叶子
}
# 树外标定常数（在 calc.py 但非 gold 树叶子，覆盖检查单列，不算缺口）
TREE_EXTERNAL_CONSTS = ["tp_eff", "out_tok"]

def main():
    d = json.load(open(SRC, encoding="utf-8"))
    nodes = {n["id"]: n for n in d["nodes"]}
    leaf_params = {n["id"]: n["param"] for n in d["nodes"] if n["param"]}
    all_leaf_params = set(leaf_params.values())

    # ---- §1 树形（按 level 缩进）----
    L1 = ["## §1 层级因素树（转录自 S1 JSON，机械）", ""]
    for n in sorted(d["nodes"], key=lambda x: (x["level"], x["id"])):
        ind = "  " * n["level"]
        tag = f" `{n['param']}`" if n["param"] else ""
        sh = f" share={n['share']}" if n["share"] else ""
        typ = n["type"] or "?"
        bb = f" {n['blackbox']}" if n["blackbox"] else ""
        sr = f" SHARED→{n['shared_ref']}" if n["shared_ref"] else ""
        L1.append(f"{ind}- **{n['id']}** {n['name']}{tag} [{typ}]{sh}{bb}{sr}")
    L1 += ["", "> 顶层 5 节点 = 3 性能(u/λ_raw/G_pass) + 1 成本(c_hour) + 1 约束(feasible_set)。", ""]

    # ---- §4 覆盖表（公式参数 → 叶子 param 映射）----
    L4 = ["## §4 完备检查：c_pass 公式参数 → 叶子覆盖（机械映射）", "",
          "| 公式参数 | 应覆盖叶子 param | 命中 | 缺口 |", "|---|---|---|---|"]
    for fp, want in FORMULA_PARAMS.items():
        hit, miss = [], []
        for w in want:
            if w in all_leaf_params:
                ids = [k for k, v in leaf_params.items() if v == w]
                hit.append(f"{w}({','.join(ids)})")
            else:
                miss.append(w)
        L4.append(f"| {fp} | {', '.join(want) or '—'} | {', '.join(hit) or '—'} | {', '.join(miss) or '✓ 无缺口'} |")
    # 反向：叶子 param 未被任何公式参数引用 = 冗余候选（树外常数单列不算冗余）
    referenced = set(w for ws in FORMULA_PARAMS.values() for w in ws)
    unused = all_leaf_params - referenced
    L4 += ["", f"**树外标定常数（覆盖检查单列，不算缺口）**：{TREE_EXTERNAL_CONSTS}（在 calc.py，非 gold 树叶子）",
           "", f"**反向（冗余候选）**：叶子 param 未被 c_pass 公式直接引用 = {sorted(unused) or '无'}", ""]

    # ---- §2 正交线索（shared_ref 非空 + 同层 share）----
    L2 = ["## §2 正交检查：线索（机械列出，判断见下）", "",
          "**SHARED 节点（正交性破绽候选，shared_ref 非空）**：", ""]
    shared = [n for n in d["nodes"] if n["shared_ref"]]
    if shared:
        L2.append("| 节点 | param | 共享自 | 含义 |")
        L2.append("|---|---|---|---|")
        for n in shared:
            L2.append(f"| {n['id']} {n['name']} | {n['param'] or '—'} | {n['shared_ref']} | 同一底层因素进两层 |")
    else:
        L2.append("（无 shared_ref 节点）")
    L2 += ["", "**同层因素 + share（正交判断的输入）**：", ""]
    by_level = {}
    for n in d["nodes"]:
        by_level.setdefault(n["level"], []).append(n)
    for lv in sorted(by_level):
        if lv == 0:
            continue
        row = " | ".join(f"{n['id']} {n['name']}(share={n['share'] or '?'})" for n in by_level[lv])
        L2.append(f"- L{lv}: {row}")
    L2 += ["", "**判断（Lead 填）**：", "- [ ] 每个 SHARED 节点是否构成真正的非正交？（共享底层因素 vs 独立分解）",
           "- [ ] 同层两因素是否会同时变动？（如 N-1.1 摊销 vs N-1.2 电费：资本 vs 运营，独立？）",
           "- 证不出 = 标 [开放] + 缺什么", ""]

    # ---- §3/§5 占位 ----
    L3 = ["## §3 最小检查（Lead 判断）", "", "- [ ] 逐层：删该层后下层是否失去压缩（用 c_pass 公式结构论证）",
          "- 示例：删 N-3(λ_raw) → t_task 失去 prefill/decode 分解 → decode 时间项失去解释", ""]
    L5 = ["## §5 作用域（Lead 判断，引 J3b 4 判据）", "",
          "- [ ] 候选集依赖 / tf_peak 作用域 / 价格口径 / 芯片命名（引 j3b_generalization.py 4 判据段）",
          "- 不做质量提升 claim", ""]

    doc = ["# J3a 层级因素树 + 三性质检查", "# origin: ai · 2026-11-26 · §1/§4/§2 线索=脚本机械生成，§2 判断/§3/§5=Lead 品味", ""]
    doc += L1 + L4 + L2 + L3 + L5
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(doc))
    # 紧凑摘要（供 Lead 判断，<40 行）
    print(f"OK wrote {os.path.relpath(OUT, ROOT)}")
    print(f"nodes={len(d['nodes'])} leaves={len([n for n in d['nodes'] if n['type']=='leaf'])}")
    print(f"shared 节点={[(n['id'], n['shared_ref']) for n in shared]}")
    print(f"unused 叶子 param={sorted(unused)}")
    gaps4 = [(fp, [w for w in want if w not in all_leaf_params]) for fp, want in FORMULA_PARAMS.items() if any(w not in all_leaf_params for w in want)]
    print(f"§4 缺口={gaps4 or '无'}")

if __name__ == "__main__":
    main()
