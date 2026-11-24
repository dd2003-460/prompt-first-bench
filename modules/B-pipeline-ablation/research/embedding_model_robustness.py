#!/usr/bin/env python3
"""跨 embedding 模型重评 — 防御审稿人"为什么是 bge-m3"（K7 15 树, GPU gold 36 units）

口径: 与 judge_objectivity_perturbation.py 同一批 15 树 + 官方阈值 0.70。
两个模型: BAAI/bge-m3 (生产) vs sentence-transformers/all-MiniLM-L6-v2 (对照, 已缓存)。
输出: 逐树 cov 对比 + 均值/sd + 模型间 cor + cor(cov, n_nodes) 双模型 + 阈值敏感性对照。
落盘: data/embedding-model-robustness-20261124.json
"""
import sys, os, json, glob, statistics

def pearson(x, y):
    n = len(x)
    mx, my = statistics.mean(x), statistics.mean(y)
    sx = sum((a - mx) ** 2 for a in x) ** 0.5
    sy = sum((b - my) ** 2 for b in y) ** 0.5
    if sx == 0 or sy == 0:
        return 0.0
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / (sx * sy)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "modules", "B-pipeline-ablation"))
from sentence_transformers import SentenceTransformer
from judge_v1 import layer_coverage, load_gold
from metacog_axis import load_run_nodes

ARCH = os.path.join(ROOT, "experiments", "stage-ablation", "checkpoints", "archive")
OUT = os.path.join(ROOT, "modules", "B-pipeline-ablation", "data", "embedding-model-robustness-20261124.json")

gold = load_gold("gpu")
runs = sorted(glob.glob(os.path.join(ARCH, "budget-*-r*", "runs-s5-sm-gpu.json")))
runs = [r for r in runs if "rerun" not in r and "nodepth" not in r][:15]
nodes_list = [load_run_nodes(r) for r in runs]
n_nodes_list = [len(n) for n in nodes_list]
print(f"gold units: {len(gold)}, trees: {len(runs)}")

MODELS = ["BAAI/bge-m3", "sentence-transformers/all-MiniLM-L6-v2"]
THR = 0.70
per_model = {}
for mname in MODELS:
    m = SentenceTransformer(mname)
    covs = []
    for nodes in nodes_list:
        s, _ = layer_coverage(nodes, gold, m, THR)
        covs.append(round(s, 4))
    per_model[mname] = {
        "thr": THR,
        "per_tree": covs,
        "mean": round(statistics.mean(covs), 4),
        "sd": round(statistics.stdev(covs), 4),
        "cor_cov_nnodes": round(pearson(covs, n_nodes_list), 4),
        # 阈值敏感性对照 (同口径: 0.65/0.80)
        "cov_at_0.65": round(statistics.mean([layer_coverage(n, gold, m, 0.65)[0] for n in nodes_list]), 4),
        "cov_at_0.80": round(statistics.mean([layer_coverage(n, gold, m, 0.80)[0] for n in nodes_list]), 4),
    }
    print(f"  {mname}: mean={per_model[mname]['mean']} sd={per_model[mname]['sd']} "
          f"cor(cov,n)={per_model[mname]['cor_cov_nnodes']} "
          f"thr 0.65→{per_model[mname]['cov_at_0.65']} 0.80→{per_model[mname]['cov_at_0.80']}")

a, b = per_model[MODELS[0]]["per_tree"], per_model[MODELS[1]]["per_tree"]
inter = round(pearson(a, b), 4)
print(f"  模型间 cor (逐树 cov): {inter}")

result = {
    "n_trees": len(runs),
    "gold_units": len(gold),
    "per_model": per_model,
    "inter_model_cor_per_tree": inter,
    "verdict": (
        "shape-robust: cor(cov,n_nodes) 跨模型同向同量级 "
        f"(bge-m3 {per_model[MODELS[0]]['cor_cov_nnodes']} vs MiniLM {per_model[MODELS[1]]['cor_cov_nnodes']}), "
        f"budget–coverage 相关性结论对 embedding 模型选择稳健; "
        f"level 跨模型敏感 (mean {per_model[MODELS[0]]['mean']} vs {per_model[MODELS[1]]['mean']}), "
        "绝对覆盖值仍是 bge-m3-scoped, 需跨模型重评才能跨模型比较"
        if (per_model[MODELS[0]]["cor_cov_nnodes"] > 0.4 and per_model[MODELS[1]]["cor_cov_nnodes"] > 0.4
            and abs(per_model[MODELS[0]]["cor_cov_nnodes"] - per_model[MODELS[1]]["cor_cov_nnodes"]) < 0.3)
        else "model-sensitive: cor(cov,n_nodes) 跨模型漂移 ≥ 0.3 或某模型 < 0.4 — 承重 shape 结论对 embedding 模型敏感, 需降级"
    ),
}
json.dump(result, open(OUT, "w"), ensure_ascii=False, indent=1)
print(f"verdict: {result['verdict']}")
print(f"→ {OUT}")
