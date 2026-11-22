#!/usr/bin/env python3
"""
T-JUDGE-1 公式 judge（第三轨，机械验证，不依赖 LLM/embedding）
================================================================
动机: 旧 LLM judge = 长度代理(Spearman 0.785 与 depth); embedding judge = 文本存在性
(召回高/精度低)。公式 judge 把判定降到计算层: 结构对不对(sympy 化简)、系数在不在区间、
排序对不对。三层全是机械的, 客观性直接拉满。

三层:
  结构层(硬): 公式结构等价(sympy.simplify(a-b)==0) + 展开/停止对齐 gold 停止准则
  系数层(软): 经验值在不在 gold 区间 + BOUND 弹性加权
  结论层(终极): 选卡排序对不对(赢家 3090×4/W4/n=2)

防 hack: tricky 输入(√2,√3,1/√5,√7 代数独立点)。两个公式在足够多代数独立点上
输出相同 => 同一公式(非巧合)。标准输入(3090×4/W4)模型可能背过, tricky 输入必须真算。

用法:
  python3 tjudge1_formula.py --emit-sidecar          # 生成 gold-gpu-formulas.json
  python3 tjudge1_formula.py --smoke <tree.json>     # 在模型树上冒烟
  python3 tjudge1_formula.py --selftest              # 验证器自检(tricky 数值)
"""
import json, re, sys, math
import sympy as sp
from sympy.core.relational import Relational

# ---------------------------------------------------------------------------
# Gold 公式表（源 = bench/rubric-v3/ablation/gold-tree.md, frozen ed552c4）
# kind: formula=恒等式/定义式(验结构) | param=经验/参数(验区间) | ncu=微架构(27b 不可达)
#       constraint=不等式门槛 | set=候选集
# expand: True=gold 在此 split(应展开) | False=leaf(应停, S-a/b/c)
# sympy: 公式字符串(仅 kind=formula/constraint)
# ref: 参考值/区间(仅 kind=param)
# share/bound: 来自 gold 树的 SHARE 权重 / BOUND 弹性
# ---------------------------------------------------------------------------
GOLD = [
 # unit_id, depth, kind, expand, sympy, lhs, ref, share, bound
 ("N-0",   1, "formula", True,  "c_hour/(u*lam_raw*G_pass)", "c_pass", None, 1.00, None),
 ("N-1",   1, "formula", True,  "amort+elec_cost+fail_cost",  "c_hour", None, 0.25, None),
 ("N-1.1", 2, "formula", True,  "(gpu_price+host_price-gpu_price*resid)/H", "amort", "42.8%", None, None),
 ("N-1.1.1",3,"param",   False, None, "gpu_price",  "2-3x 价差", 0.55, "2.2x"),
 ("N-1.1.2",3,"param",   False, None, "host_price", None, 0.15, None),
 ("N-1.1.3",3,"param",   False, None, "resid",      None, 0.10, "B8"),
 ("N-1.1.4",3,"param",   False, None, "H",          None, 0.20, "2.02x"),
 ("N-1.2", 2, "formula", True,  "power_kw*elec",              "elec_cost", "49.3%", None, None),
 ("N-1.2.1",3,"param",   False, None, "power_kw",   None, 0.50, None),
 ("N-1.2.2",3,"param",   False, None, "elec",       None, 0.50, "1.88x"),
 ("N-1.3", 2, "formula", True,  "p_fail*gpu_price/H",         "fail_cost", "8.0%", None, None),
 ("N-1.3.1",3,"param",   False, None, "p_fail",     None, 0.50, "B8"),
 ("N-2",   1, "formula", True,  "duty_demand*sched_eff",      "u", None, 0.25, None),
 ("N-2.1", 2, "param",   False, None, "duty_demand", "[0.10,0.80]", 0.60, "8.00x"),
 ("N-2.2", 2, "param",   False, None, "sched_eff",  None, 0.40, None),
 ("N-3",   1, "formula", True,  "3600/(t_prefill+t_decode/n)", "lam_raw", None, 0.25, None),
 ("N-3.1", 2, "formula", True,  "prefill_flops/(n_cards*tf_peak*mfu*tp_eff)", "t_prefill", "40.1%", None, None),
 ("N-3.1.1",3,"param",   False, None, "prefill_flops", "~594 TFLOP", 0.30, None),
 ("N-3.1.2",3,"param",   False, None, "tf_peak",    None, 0.25, None),
 ("N-3.1.3",3,"formula", True,  "(T_kernel/T_step)*sum_k(T_k/T_step*F_k/(T_k*C_peak))", "mfu", None, 0.45, "1.20x"),
 ("N-3.1.3.1",4,"ncu",   False, None, "sm_occupancy", "NCU sm__warps_active", None, None),
 ("N-3.1.3.2",4,"ncu",   False, None, "tensor_util",  "NCU PIPE_TENSOR_ACTIVE", None, None),
 ("N-3.1.3.3",4,"ncu",   False, None, "l2_hit",       "NCU lts__t_sector_hit_rate", None, None),
 ("N-3.2", 2, "formula", True,  "out_tok*(w_bytes+n*kv_per_stream)/(n_cards*bw_peak*eta_bw*tp_eff)", "t_decode", "59.9%", None, None),
 ("N-3.2.1",3,"param",   False, None, "w_bytes",      "W4=14/W8=27/W16=54 GB", 0.25, None),
 ("N-3.2.2",3,"param",   False, None, "kv_per_stream", None, 0.20, "2.0x"),
 ("N-3.2.3",3,"param",   False, None, "bw_peak",      None, 0.25, None),
 ("N-3.2.4",3,"formula", True,  "(T_mem/T_wall)*(hbm_bytes_s/B_peak)", "eta_bw", None, 0.30, "1.43x"),
 ("N-3.2.4.1",4,"ncu",   False, None, "hbm_sol",      "NCU dram__bytes/B_peak", None, None),
 ("N-3.2.4.2",4,"ncu",   False, None, "l2_hit",       "NCU lts__t_sector_hit_rate", None, None),
 ("N-3.2.4.3",4,"ncu",   False, None, "launch_gap",   "Nsight timeline gap", None, None),
 ("N-4",   1, "param",   False, None, "G_pass",       "nuisance", 0.25, "1.57x"),
 ("N-5",   1, "set",     True,  None, "feasible_set", None, None, None),
 ("N-5.1", 2, "constraint", False, "n*kv_per_stream+w_bytes<=mem_avail", "n_cap", None, None, None),
 ("N-5.2", 2, "constraint", False, "bw_eff>=bw_floor", "bw_ok", "W4=774/W8=1034/W16=1574 GB/s", None, None),
 ("N-5.3", 2, "param",   False, None, "cache_hit_rate", "nuisance", None, "7.6x"),
]
# 注: N-1.3.2 是 SHARED 指针(→N-1.1.1), 已去重, 故 36 单元(非 37)。

# tricky 输入: 代数独立点, 防"背标准答案"。标准输入 3090×4/W4/n=2 模型可能见过。
TRICKY = [math.sqrt(2), math.sqrt(3), 1/math.sqrt(5), math.sqrt(7), math.sqrt(2)*math.sqrt(3)]

# 参考配置(赢家 3090×4 / W4 / n=2), 用于结论层排序
REF_CONFIG = {"n_cards": 4, "quant": "W4", "n": 2}
REF_W_BYTES = {"W4": 14, "W8": 27, "W16": 54}   # GB
REF_BW_FLOOR = {"W4": 774, "W8": 1034, "W16": 1574}  # GB/s


def gold_records():
    """GOLD 表 → list[dict]。"""
    out = []
    for (uid, depth, kind, expand, sympy_s, lhs, ref, share, bound) in GOLD:
        rec = {"unit_id": uid, "depth": depth, "kind": kind, "expand": expand,
               "lhs": lhs, "ref": ref, "share": share, "bound": bound}
        if sympy_s:
            rec["sympy"] = sympy_s
        out.append(rec)
    return out


def emit_sidecar(path):
    data = {
        "_schema": "gold-gpu-formulas/v1",
        "_doc": "T-JUDGE-1 公式 judge gold sidecar (2026-11-22)。源 = bench/rubric-v3/ablation/gold-tree.md (frozen ed552c4)。"
                "kind: formula=恒等式(验结构)/param=经验值(验区间)/ncu=微架构(27b不可达)/constraint=不等式门槛/set=候选集。"
                "expand=True 表示 gold 在此 split(应展开), False=leaf(应停)。sympy 字段为可 sympify 的公式。"
                "tricky 输入防 hack(代数独立点)。原树文件不修改(冻结资产)。",
        "source": "bench/rubric-v3/ablation/gold-tree.md",
        "tricky_inputs": TRICKY,
        "ref_config": REF_CONFIG,
        "ref_w_bytes_gb": REF_W_BYTES,
        "ref_bw_floor_gbs": REF_BW_FLOOR,
        "units": gold_records(),
    }
    with open(path, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    # 自检: 每个 formula/constraint 的 sympy 必须能 parse
    bad = []
    for r in data["units"]:
        if r.get("sympy"):
            try:
                sp.sympify(r["sympy"])
            except Exception as e:
                bad.append((r["unit_id"], str(e)))
    print(f"[emit] {path}: {len(data['units'])} units, {sum(1 for r in data['units'] if r.get('sympy'))} with sympy")
    if bad:
        print("[emit] SYMPY PARSE FAIL:", bad)
        sys.exit(1)
    print("[emit] all sympy parse OK")


def structural_equiv(fa, fb):
    """两个 sympy 表达式结构等价? (化简差为 0)"""
    try:
        return sp.simplify(sp.sympify(fa) - sp.sympify(fb)) == 0
    except Exception:
        return False


def tricky_check(expr_s, n_points=5, tol=1e-9):
    """在 tricky 代数独立点上求值, 返回 (ok, values)。
    表达式 → float 值; 不等式(Relational) → 布尔真值。
    用于自检验证器 + 数值层验证。"""
    expr = sp.sympify(expr_s)
    syms = list(expr.free_symbols)
    vals = []
    for i, t in enumerate(TRICKY[:n_points]):
        sub = {s: sp.Float(t) for s in syms}
        try:
            v = expr.subs(sub)
            # 全代入后不等式会塌缩成 sympy 的 BooleanTrue/BooleanFalse(不是 Python bool,
            # float() 拒收), 也可能仍是 Relational — 两者都按布尔处理。
            # 用类型名判断, 不依赖 sp.Boolean/sp.Relational 顶层导出(1.14 没有)。
            if isinstance(v, Relational) or type(v).__name__ in ("BooleanTrue", "BooleanFalse"):
                vals.append(bool(v))
            else:
                vals.append(float(v))
        except Exception:
            return False, None
    return True, vals


def extract_formula(claim):
    """从节点 claim 抽 'X = expr' 的 RHS。返回 (lhs, rhs_str) 或 (None, None)。
    RHS 不含逗号(逗号会 sympify 成 tuple); 只处理 ASCII 公式
    (中文 claim 里的公式靠 LLM 补写, 微信在做)。"""
    m = re.search(r"([A-Za-z_][A-Za-z0-9_.]*)\s*=\s*([A-Za-z0-9_+\-*/().\s^]+)", claim)
    if m:
        return m.group(1), m.group(2).strip()
    return None, None


def smoke(tree_path, sidecar_path="gold-gpu-formulas.json"):
    sc = json.load(open(sidecar_path))
    units = {u["unit_id"]: u for u in sc["units"]}
    d = json.load(open(tree_path))
    nodes = d["nodes"]
    print(f"[smoke] tree={tree_path} n_nodes={len(nodes)}")

    # 1) 模型节点公式可提取率
    extracted = 0
    parseable = 0
    parse_list = []
    for nd in nodes:
        lhs, rhs = extract_formula(nd["claim"])
        if rhs:
            extracted += 1
            try:
                sp.sympify(rhs)
                parseable += 1
                parse_list.append((nd["id"], lhs, rhs[:60]))
            except Exception:
                pass
    print(f"[smoke] 含可提取公式: {extracted}/{len(nodes)}, sympy 可解析: {parseable}")

    # 2) 验证器自检: gold 公式在 tricky 点上求值
    n_formula = 0
    n_numeric = 0
    for uid, u in units.items():
        if u.get("sympy") and u["kind"] in ("formula", "constraint"):
            n_formula += 1
            ok, vals = tricky_check(u["sympy"])
            if ok:
                n_numeric += 1
            elif "sum_k" in u["sympy"]:
                # Σ 恒等式(MFU 定义): 符号标注, 纯结构验证, 不走数值 — 预期
                pass
            else:
                print(f"[smoke]   !! {uid} tricky 求值失败: {u['sympy']}")
    print(f"[smoke] gold 公式/约束单元: {n_formula}, 数值自检通过 {n_numeric} (Σ 恒等式走结构验证)")

    # 3) 结构匹配示例: 模型公式 vs gold 公式(按变量重叠)
    print("[smoke] 结构匹配示例(模型公式 vs gold, 变量重叠≥2 才比):")
    shown = 0
    for nid, lhs, rhs in parse_list:
        mvars = set(sp.sympify(rhs).free_symbols) if _safe(rhs) else set()
        for uid, u in units.items():
            if not u.get("sympy"):
                continue
            gvars = set(sp.sympify(u["sympy"]).free_symbols)
            if len(mvars & gvars) >= 2:
                eq = structural_equiv(rhs, u["sympy"])
                print(f"   {nid} ({lhs}) vs gold {uid}: equiv={eq}  vars∩={sorted(v.name for v in (mvars&gvars))}")
                shown += 1
                break
        if shown >= 8:
            break
    if shown == 0:
        print("   (无变量重叠≥2 的匹配 — 预期: 模型公式用词与 gold 符号不同, 需 LLM 补写对齐符号)")


def _safe(s):
    try:
        e = sp.sympify(s)
        return not isinstance(e, (tuple, list))
    except Exception:
        return False


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--emit-sidecar", action="store_true")
    ap.add_argument("--smoke", metavar="TREE")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--sidecar", default="gold-gpu-formulas.json")
    a = ap.parse_args()
    if a.emit_sidecar:
        emit_sidecar(a.sidecar)
    if a.selftest:
        for uid, u in [(r["unit_id"], r) for r in gold_records()]:
            if u.get("sympy"):
                ok, vals = tricky_check(u["sympy"])
                print(f"  {uid:10s} ok={ok} vals={['%.4f'%v for v in (vals or [])]}")
        print("[selftest] done")
    if a.smoke:
        smoke(a.smoke, a.sidecar)
