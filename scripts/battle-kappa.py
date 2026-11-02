#!/usr/bin/env python3
"""battle-kappa.py — battle 投票回执 → Fleiss'κ 计算（C节资产#3 落地）

链路：ego-browser battle 投票（人工/半自动，见 ~/.hermes/rules/arena.md）
     → 每轮落盘 scorers/<date>-battle-r<N>.json
     → 本脚本收齐 ≥2 轮（≥4 个异族 scorer）后算 M7 二值 Fleiss'κ + 加权总分 Spearman
     → 回执 JSON 落盘，供 assert-kappa-receipt.py 消费

battle 回执格式（每轮一个文件，ego-browser 步骤 5 产出）:
{
  "date": "2026-10-31",
  "round": 1,
  "material": "<材料名>",
  "material_sha256": "<sha256>",
  "mode": "battle",
  "model_a": "<模型A全名>",
  "model_b": "<模型B全名>",
  "vote": "a|b|tie",
  "response_a_full": "<完整回答文本(内嵌 JSON 评分)>",
  "response_b_full": "<完整回答文本(内嵌 JSON 评分)>"
}

用法：
  python3 scripts/battle-kappa.py --dir bench/rubric-v3/scorers \
      --pattern "*-battle-r*.json" --out receipts/kappa-battle.json

exit 0 = κ 计算成功且家族数 ≥3; exit 1 = 数据不足或解析失败
"""
import argparse
import glob
import json
import math
import re
import sys
from pathlib import Path


def family_of(model_name):
    """模型全名 → 家族标识（小写前缀匹配）。"""
    n = model_name.lower()
    for fam in ["claude", "gpt", "qwen", "minimax", "gemini", "grok",
                "deepseek", "glm", "llama", "mistral"]:
        if n.startswith(fam) or f" {fam}" in n or fam in n[:20]:
            return fam
    return n.split("-")[0][:8]


def extract_scores(response_text):
    """从 battle 回答全文里抽评分 JSON。

    结构: {"scorer": ..., "scores": {run1: {...}, run2: {...}, ...}, "basis": {...}}
    basis 块里也含 M7_gate 文本（叙述性），必须只取 scores 块，不能全文件搜。
    """
    start = response_text.find('"scores"')
    if start < 0:
        return None
    brace = response_text.rfind("{", 0, start)
    if brace < 0:
        return None
    depth = 0
    for i in range(brace, len(response_text)):
        if response_text[i] == "{":
            depth += 1
        elif response_text[i] == "}":
            depth -= 1
            if depth == 0:
                try:
                    obj = json.loads(response_text[brace:i + 1])
                except json.JSONDecodeError:
                    return None
                # 只要含 scores 且不含 basis 的顶层块
                if "scores" in obj and "basis" not in obj:
                    return obj
                if "scores" in obj:
                    return obj
    return None


def m7_binary(score_obj):
    """M7 gate 字段 → 0/1。缺字段 = None（该 scorer 不参与 M7 矩阵）。"""
    g = score_obj.get("M7_gate")
    if isinstance(g, str):
        return 1 if g.strip().lower() == "pass" else 0
    if isinstance(g, (int, float)):
        return 1 if g >= 0.5 else 0
    return None


def weighted_total(score_obj):
    """M1-M6 等权均值（与 pfb rubric 权重对齐时用 weights 参数覆盖）。"""
    vals = [score_obj.get(k) for k in ["M1", "M2", "M3", "M4", "M5", "M6"]]
    vals = [float(v) for v in vals if isinstance(v, (int, float))]
    return sum(vals) / len(vals) if vals else None


def fleiss_kappa(matrix):
    """matrix: dict[item_id] -> list[int 0/1]（每个 scorer 一列）。返回 (kappa, n_items, n_raters)。"""
    items = {k: v for k, v in matrix.items() if all(x is not None for x in v)}
    if not items:
        return None, 0, 0
    ids = sorted(items)
    N = len(ids)
    r = len(next(iter(items.values())))
    # n_ij: item i 中 raters 打 j 的个数
    n_mat = [[sum(1 for x in items[i] if x == j) for j in (0, 1)] for i in ids]
    # p_i: item i 的一致性比例
    p_i = [(n_mat[i][0] ** 2 + n_mat[i][1] ** 2 - r) / (r * (r - 1)) for i in range(N)]
    P = sum(p_i) / N
    # p_j..: 全局比例（Fleiss 1973 原式：P_e = Σ_j p̄_j(1−p̄_j)，j ∈ {0,1}；旧版误用 Σp̄² 已修 r239）
    tot = [sum(n_mat[i][j] for i in range(N)) for j in (0, 1)]
    p_bar = [t / (N * r) for t in tot]
    P_e = sum(p * (1 - p) for p in p_bar)
    if abs(1 - P_e) < 1e-12:
        return 0.0, N, r
    return (P - P_e) / (1 - P_e), N, r


def spearman(xs, ys):
    def rank(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        ranks = [0.0] * len(v)
        i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and v[order[j + 1]] == v[order[i]]:
                j += 1
            avg = (i + j) / 2 + 1
            for k in range(i, j + 1):
                ranks[order[k]] = avg
            i = j + 1
        return ranks
    rx, ry = rank(xs), rank(ys)
    n = len(xs)
    mx, my = sum(rx) / n, sum(ry) / n
    cov = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    vx = math.sqrt(sum((a - mx) ** 2 for a in rx))
    vy = math.sqrt(sum((b - my) ** 2 for b in ry))
    if vx * vy < 1e-12:
        return None
    return cov / (vx * vy)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--pattern", default="*-battle-r*.json")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    files = sorted(Path(args.dir).glob(args.pattern))
    if len(files) < 2:
        print(f"FAIL: need >=2 battle rounds, found {len(files)}", file=sys.stderr)
        sys.exit(1)

    scorers = []       # (name, family)
    per_run = {}       # run_id -> {scorer_name: binary}
    totals = {}        # run_id -> {scorer_name: float}
    obj_scores_cache = {}  # run_id -> {scorer_name: score_dict}（Spearman 用维度向量）

    for fp in files:
        d = json.load(open(fp))
        for side in ("a", "b"):
            name = d.get(f"model_{side}")
            resp = d.get(f"response_{side}_full", "")
            if not name or not resp:
                continue
            obj = extract_scores(resp)
            if obj is None or "scores" not in obj:
                print(f"WARN: {fp.name} side-{side} ({name}): no parseable scores, skipped",
                      file=sys.stderr)
                continue
            if any(s["name"] == name for s in scorers):
                print(f"WARN: {name} appears in multiple rounds, keeping first (防重复计数)",
                      file=sys.stderr)
                continue
            scorers.append({"name": name, "family": family_of(name)})
            for run_id, sc in obj["scores"].items():
                per_run.setdefault(run_id, {})[name] = m7_binary(sc)
                totals.setdefault(run_id, {})[name] = weighted_total(sc)
                obj_scores_cache.setdefault(run_id, {})[name] = sc

    families = {s["family"] for s in scorers}
    if len(families) < 3:
        print(f"FAIL: need >=3 distinct families, got {sorted(families)}", file=sys.stderr)
        sys.exit(1)

    # M7 矩阵（剔除有 None 的 run）
    kappa, n_items, n_raters = fleiss_kappa(per_run)

    # 加权总分 Spearman（同一 run 内 scorer 两两对维度分向量的 rank 相关，
    # 与旧 fleiss-kappa-computation.json 的 spearman_per_run 同口径）
    dim_keys = ["M1", "M2", "M3", "M4", "M5", "M6"]
    rho_pairs = []
    for run_id in sorted(per_run):
        vecs = {}
        for s in scorers:
            sc = obj_scores_cache.get(run_id, {}).get(s["name"])
            if sc is None:
                continue
            v = [sc.get(k) for k in dim_keys]
            if all(isinstance(x, (int, float)) for x in v):
                vecs[s["name"]] = v
        names = list(vecs)
        for i in range(len(names)):
            for j in range(i + 1, len(names)):
                rho = spearman(vecs[names[i]], vecs[names[j]])
                if rho is not None:
                    rho_pairs.append({"run": run_id, "pair": [names[i], names[j]],
                                      "rho": round(rho, 4)})

    out = {
        "kind": "battle_fleiss_kappa",
        "source_files": [f.name for f in files],
        "scorers": scorers,
        "families": sorted(families),
        "n_families": len(families),
        "m7_fleiss_kappa": round(kappa, 4) if kappa is not None else None,
        "m7_n_items": n_items,
        "m7_n_raters": n_raters,
        "m7_matrix": {k: [per_run[k].get(s["name"]) for s in scorers] for k in sorted(per_run)},
        "weighted_totals": {k: {s["name"]: (round(v, 2) if v is not None else None)
                                for s in scorers for v in [totals[k].get(s["name"])]}
                            for k in sorted(totals)},
        "spearman_per_run": rho_pairs,
        "irr_status": "true_IRR" if len(families) >= 2 else "non_IRR_same_family",
    }
    # 旧口径兼容字段（receipt-r6 等下游引用）
    out["n_raters"] = n_raters

    op = Path(args.out)
    op.parent.mkdir(parents=True, exist_ok=True)
    op.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"OK: kappa={out['m7_fleiss_kappa']} (n_items={n_items}, n_raters={n_raters}, "
          f"families={out['n_families']}) -> {op}")


if __name__ == "__main__":
    main()