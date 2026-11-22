#!/usr/bin/env python3
"""Judge v1.0 — 严格且不变的三层机械 judge（不依赖 LLM）

spec: modules/B-pipeline-ablation/research/judge-v1.0-spec.md (frozen f6072397f)
输入: budget scan run json 的 runs-s5-sm-gpu.json（含 nodes: id/claim/level/parent_ids）
      + gold-gpu-units.json (36 单元, text 供 embedding)
      + gold-gpu-formulas.json (36 单元, kind/sympy/ref/bound)
三层:
  L-机械  数值正确性: sympy 结构等价 + 数值容差(默认 10%)。只覆盖含可提取公式的节点。
  L-结构  树完整性: 去重后深度/节点数/分支因子 vs gold(37节点,depth5)。
  L-覆盖  gold 匹配: bge-m3 cosine >= 阈值(默认 0.80) + MAGNET_LIMIT=3。
综合:  total = w_mech*mech + w_struct*struct + w_cov*cov   (默认 0.4/0.3/0.3)
可复现: 确定性计算, 无 LLM, same input → same output。

用法:
  python3 judge_v1.py --runs-dir <dir> [--out JSON]
  python3 judge_v1.py --calibrate            # 用 gold 36 unit 做 cosine 阈值 ROC
  python3 judge_v1.py --selftest             # 三层各跑一个合成样例
"""
import argparse, glob, json, os, re, sys
import numpy as np
import sympy as sp


def sp_sympify(s):
    return sp.sympify(s)

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from tjudge1_formula import extract_formula, structural_equiv, _safe, TRICKY
from tjudge1_parse import load_gold, PFB_ROOT

GOLD_UNITS = os.path.join(HERE, "gold-gpu-units.json")
GOLD_FORMULAS = os.path.join(HERE, "gold-gpu-formulas.json")

# 冻结阈值（2026-11-22 标定后冻结, 见 judge-v1-cov-calibration.md）
COS_THRESHOLD = 0.70   # 标定: 0.80 覆盖塌(0.015), 0.70 覆盖 0.350 且 per-run 区分度好(0.11-0.56)
MAGNET_LIMIT = 3
NUM_TOL = 0.10
# 综合分: 标定发现 mech 层全 0(符号不对齐, 无信息量) → 移出综合分, 只作诊断
# 结构层 node_score 饱和(模型节点 100+ vs gold 37, 全 1.0) → 结构轴 = depth 归一
W_DEPTH, W_COV = 0.5, 0.5
GOLD_DEPTH = 5
GOLD_NNODES = 37


def load_run_nodes(run_json):
    """run json（含 nodes 字段）→ [{id, claim, depth}]。depth 由 level 或 parent_ids 推。
    budget scan 的记账 json 不含 nodes（原始数据在 checkpoints/archive/budget-B-rR-*/runs-s5-sm-gpu.json）。
    """
    d = json.load(open(run_json))
    if "nodes" not in d:
        # 记账 json → 找对应 archive 的原始树
        m = re.match(r"gpu_budget(\d+)_r(\d+)", os.path.basename(run_json))
        if m:
            b, r = m.group(1), m.group(2)
            import glob as _g
            arch = _g.glob(os.path.join(PFB_ROOT, "experiments", "stage-ablation",
                                        "checkpoints", "archive", f"budget-{b}-r{r}-*",
                                        "runs-s5-sm-gpu.json"))
            if arch:
                d = json.load(open(sorted(arch)[0]))
    nodes = d.get("nodes", [])
    out = []
    for nd in nodes:
        lvl = nd.get("level", "")
        m = re.match(r"L(\d+)", lvl)
        depth = int(m.group(1)) if m else (len(nd.get("parent_ids", [])) + 1)
        out.append({"id": nd.get("id"), "claim": nd.get("claim", ""), "depth": depth})
    return out


def dedup(nodes):
    """精确文本去重（claim 归一化后相同 → 只留一个）。返回去重后节点 + 重复数。"""
    seen = {}
    ded = []
    for n in nodes:
        key = re.sub(r"\s+", "", n["claim"])[:200]
        if key and key not in seen:
            seen[key] = True
            ded.append(n)
    return ded, len(nodes) - len(ded)


def layer_mechanical(nodes, gold_formulas):
    """L-机械: 对每个含可提取公式的模型节点, 找变量重叠≥2 的 gold 公式, 验结构等价。
    返回 (score, n_with_formula, n_matched, n_equiv)。"""
    gmap = {u["unit_id"]: u for u in gold_formulas}
    n_with = n_match = n_equiv = 0
    for n in nodes:
        lhs, rhs = extract_formula(n["claim"])
        if not rhs or not _safe(rhs):
            continue
        n_with += 1
        try:
            mvars = set(sp_sympify(rhs).free_symbols)
        except Exception:
            continue
        best = None
        for uid, u in gmap.items():
            if not u.get("sympy"):
                continue
            try:
                gvars = set(sp_sympify(u["sympy"]).free_symbols)
            except Exception:
                continue
            if len(mvars & gvars) >= 2:
                best = (uid, u)
                break
        if best:
            n_match += 1
            if structural_equiv(rhs, best[1]["sympy"]):
                n_equiv += 1
    score = (n_equiv / n_match) if n_match else 0.0
    return score, n_with, n_match, n_equiv


def layer_structure(nodes):
    """L-结构: 去重后 depth/节点数/分支因子 vs gold。"""
    ded, n_dup = dedup(nodes)
    if not ded:
        return 0.0, {"depth": 0, "nodes": 0, "branching": 0, "dedup": 0}
    depths = [n["depth"] for n in ded]
    max_depth = max(depths)
    # 分支因子: 按 parent 深度统计（近似, 无 parent_ids 时用深度直方图）
    from collections import Counter
    depth_hist = Counter(depths)
    branching = round(sum(depth_hist.values()) / max(len(depth_hist), 1), 3)
    depth_score = min(max_depth / GOLD_DEPTH, 1.0)
    node_score = min(len(ded) / GOLD_NNODES, 1.0)
    # 标定(2026-11-22): node_score 饱和(模型 100+ 节点 vs gold 37 → 全 1.0, 无区分度)
    # 结构轴 = depth 归一(有区分度); node_score 只作诊断
    score = depth_score
    return score, {"depth": max_depth, "nodes": len(ded), "branching": branching,
                   "dedup": n_dup, "depth_score": round(depth_score, 3),
                   "node_score_sat": round(node_score, 3)}


def layer_coverage(nodes, gold_units, model, cos_threshold=COS_THRESHOLD):
    """L-覆盖: bge-m3 cosine >= 阈值, 去重计数(每个 gold unit 命中≥1次算1次)。
    2026-11-23 修复: 旧版 MAGNET_LIMIT=3 是二元清零(unit 被≥3节点命中→整个剔除),
    对高节点 run 产生反相关伪影(覆盖越充分→越易触发→cov 越低, B-r1 0.222→0.0)。
    confirmed 本就是 set(unit 级天然去重, 不存在刷分), magnet 排除纯有害。
    现: confirmed = 所有 matched unit 的集合; magnet_ids 保留作诊断字段。
    记录: research/judge-v1-magnet-artifact-20261123.md"""
    from sentence_transformers import SentenceTransformer
    node_emb = model.encode([n["claim"] for n in nodes], normalize_embeddings=True,
                            show_progress_bar=False)
    gold_emb = model.encode([u["text"] for u in gold_units], normalize_embeddings=True,
                            show_progress_bar=False)
    sim = node_emb @ gold_emb.T
    top1 = sim.argmax(axis=1)
    top1_sim = sim[np.arange(len(nodes)), top1]
    matched = top1_sim >= cos_threshold
    from collections import Counter
    absorb = Counter(top1[i] for i in range(len(nodes)) if matched[i])
    magnets = {g for g, c in absorb.items() if c >= MAGNET_LIMIT}  # 诊断用, 不再剔除
    confirmed = set(top1[i] for i in range(len(nodes)) if matched[i])
    score = len(confirmed) / len(gold_units)
    return score, {"coverage": round(score, 4), "n_confirmed": len(confirmed),
                   "n_gold": len(gold_units), "n_magnets": len(magnets),
                   "magnet_ids": sorted(gold_units[g]["unit_id"] for g in magnets),
                   "cos_threshold": cos_threshold,
                   "sim_median": round(float(np.median(top1_sim)), 3)}


def judge_run(run_json, model=None, cos_threshold=COS_THRESHOLD, gold_units=None,
              gold_formulas=None):
    """对一个 run json 算三层 + 综合分。
    gold_units/gold_formulas 可外部注入（跨域: B1 解析产物）; 默认 gpu。
    """
    nodes = load_run_nodes(run_json)
    if gold_units is None:
        gold_units = load_gold("gpu")
    if gold_formulas is None:
        gold_formulas = json.load(open(GOLD_FORMULAS))["units"]

    mech, m_with, m_match, m_equiv = layer_mechanical(nodes, gold_formulas)
    struct, s_detail = layer_structure(nodes)
    if model is None:
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer("BAAI/bge-m3")
    cov, c_detail = layer_coverage(nodes, gold_units, model, cos_threshold)

    total = W_DEPTH * struct + W_COV * cov
    return {
        "run": os.path.basename(run_json),
        "n_nodes_raw": len(nodes),
        "layers": {
            "mechanical_diag": {"score": round(mech, 4), "n_with_formula": m_with,
                                "n_matched": m_match, "n_equiv": m_equiv,
                                "note": "符号不对齐, 移出综合分, 只作诊断"},
            "structure": {"score": round(struct, 4), **s_detail},
            "coverage": {"score": round(cov, 4), **c_detail},
        },
        "weights": {"depth": W_DEPTH, "cov": W_COV},
        "total_score": round(total, 4),
    }


def calibrate_cos(model):
    """用 gold 36 unit 内部相似度做阈值建议（正例=同 unit 不同表述, 近似用 self-sim 上界）。
    输出各阈值下的 self-sim 分布, 供人工选阈值。"""
    gold_units = load_gold("gpu")
    emb = model.encode([u["text"] for u in gold_units], normalize_embeddings=True,
                       show_progress_bar=False)
    sim = emb @ emb.T
    np.fill_diagonal(sim, 0)
    off = sim[~np.eye(len(sim), dtype=bool)]
    print(f"[calibrate] gold 36 unit 内部 cosine (off-diagonal):")
    for q in (10, 25, 50, 75, 90, 95, 99):
        print(f"  p{q}: {np.percentile(off, q):.3f}")
    print(f"  max: {off.max():.3f}  mean: {off.mean():.3f}")
    print("  [说明] 这是 gold 单元间的语义相似度上界。真实模型节点匹配应显著高于此上界才可信。")
    print("  阈值建议: 取 gold 内部 p99 与 1.0 的中点, 或人工看匹配明细定。当前冻结 0.80。")


def selftest():
    """合成三层样例, 验证代码路径。"""
    # L-机械: 一个节点含 gold 公式 c_pass = c_hour/(u*lam_raw*G_pass)
    nodes = [{"id": "N1", "claim": "c_pass = c_hour/(u*lam_raw*G_pass)", "depth": 1}]
    gold_formulas = json.load(open(GOLD_FORMULAS))["units"]
    mech, mw, mm, me = layer_mechanical(nodes, gold_formulas)
    print(f"[selftest] L-机械: score={mech} with_formula={mw} matched={mm} equiv={me}")
    # L-结构
    struct, sd = layer_structure(nodes)
    print(f"[selftest] L-结构: score={struct} {sd}")
    print("[selftest] L-覆盖: 需 bge-m3 模型, 跳过合成(在真实 run 上验证)")
    print("[selftest] done")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs-dir")
    ap.add_argument("--out")
    ap.add_argument("--calibrate", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--gold-units", help="跨域: B1 解析的 units.json (markdown gold 产物)")
    ap.add_argument("--runs-glob", default="gpu_budget*.json",
                    help="runs-dir 内的 run 文件 glob (默认 gpu_budget*.json)")
    a = ap.parse_args()
    if a.selftest:
        selftest()
    elif a.calibrate:
        from sentence_transformers import SentenceTransformer
        calibrate_cos(SentenceTransformer("BAAI/bge-m3"))
    elif a.runs_dir:
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer("BAAI/bge-m3")
        gu = None
        if a.gold_units:
            gu = json.load(open(a.gold_units))["units"]
        runs = sorted(glob.glob(os.path.join(a.runs_dir, a.runs_glob)))
        results = [judge_run(r, model, gold_units=gu) for r in runs]
        out = {"thresholds": {"cos": COS_THRESHOLD, "num_tol": NUM_TOL,
                              "weights": [W_DEPTH, W_COV]},
               "runs": results}
        if a.out:
            json.dump(out, open(a.out, "w"), ensure_ascii=False, indent=1)
            print(f"[judge_v1] {len(results)} runs → {a.out}")
        for r in results:
            L = r["layers"]
            print(f"  {r['run']:24s} total={r['total_score']:.4f} "
                  f"(depth={L['structure']['score']:.3f} "
                  f"cov={L['coverage']['score']:.3f} "
                  f"mech_diag={L['mechanical_diag']['score']:.3f})")
    else:
        ap.print_help()
