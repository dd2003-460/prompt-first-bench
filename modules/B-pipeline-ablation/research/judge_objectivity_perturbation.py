#!/usr/bin/env python3
"""Judge 客观性扰动测试 (2026-11-24, D 方法论三问 Q1 的实证回答)

问题: 机械 judge 域特定 (gold 人工构建), 怎么保证客观?
本脚本不回答"gold 对不对"(那是独立 gold 对照, 需另建 gold), 而是回答
"给定 gold, 分数对 gold 的微小扰动 / 阈值选择是否稳健" — 即测量误差带。
若 cov 在扰动下漂移 < 噪声底, 则承重结论 (平台/上升/域依赖) 对 gold 构建细节不敏感。

两个扰动轴:
  A. gold 扰动: 随机删 10% gold units (5 seeds) → 重算 cov, 看 |Δcov|
     解读: 模拟"gold 少建了 10% unit" — 若 Δ 小, cov 对 gold 完备性不敏感
  B. 阈值扰动: cos_threshold 0.70±0.05 (官方基线) → 重算 cov, 看 |Δcov|
     解读: 匹配阈值是超参, 若 Δ 小, cov 对阈值不敏感

对象: GPU K7 15 棵 archive 树 (承重数字 cor=0.563 的语料)。
落盘: data/judge-perturbation-20261124.json
"""
import sys, os, json, glob, random, statistics, math
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "modules", "B-pipeline-ablation"))
from judge_v1 import load_gold, load_run_nodes, layer_coverage
from sentence_transformers import SentenceTransformer

ARCH = os.path.join(ROOT, "experiments", "stage-ablation", "checkpoints", "archive")
OUT = os.path.join(ROOT, "modules", "B-pipeline-ablation", "data", "judge-perturbation-20261124.json")

model = SentenceTransformer("BAAI/bge-m3")
gold = load_gold("gpu")
print(f"gold units: {len(gold)}")

# 15 棵 K7 archive 树 (GPU, pre-clamp)
runs = sorted(glob.glob(os.path.join(ARCH, "budget-*-r*", "runs-s5-sm-gpu.json")))
runs = [r for r in runs if "rerun" not in r and "nodepth" not in r][:15]
print(f"archive 树: {len(runs)} 棵")
nodes_list = [load_run_nodes(r) for r in runs]

def covs(nodes_list, gold_units, thr):
    out = []
    for nodes in nodes_list:
        s, _ = layer_coverage(nodes, gold_units, model, thr)
        out.append(s)
    return out

# !! 2026-11-24 修正: 基线必须用官方阈值 0.70 (judge_v1 COS_THRESHOLD, 标定: 0.80 塌 0.015,
#    0.70 覆盖 0.350 且区分度好)。首版误用 0.75 → 基线 0.0981 比官方口径 0.3185 低 3.2 倍, A 段结论作废。
base = covs(nodes_list, gold, 0.70)
base_mean = statistics.mean(base)
base_sd = statistics.stdev(base)
print(f"\n基线 (thr=0.70 官方, 全 gold): mean cov = {base_mean:.4f} (sd={base_sd:.4f})")

# A. gold 扰动: 删 10% (5 seeds)
print("\n=== A. gold 扰动 (随机删 10% units, 5 seeds) ===")
gold_pert = []
for seed in [1, 2, 3, 4, 5]:
    rng = random.Random(seed)
    n_drop = max(1, int(len(gold) * 0.10))
    keep = set(rng.sample(range(len(gold)), len(gold) - n_drop))
    g = [gold[i] for i in sorted(keep)]
    c = covs(nodes_list, g, 0.70)
    d = statistics.mean(c) - base_mean
    gold_pert.append({"seed": seed, "n_gold": len(g), "mean_cov": round(statistics.mean(c), 4),
                      "delta_mean": round(d, 4)})
    print(f"  seed={seed}: n_gold={len(g)} mean={statistics.mean(c):.4f} Δ={d:+.4f}")
max_dA = max(abs(p["delta_mean"]) for p in gold_pert)
print(f"  max|Δ| = {max_dA:.4f}  vs 噪声底 {base_sd:.4f} → {'< 1×sd: 对 gold 完备性不敏感' if max_dA < base_sd else '>= 1×sd: 对 gold 构建细节敏感, 承重结论需带误差带'}")

# B. 阈值扰动
print("\n=== B. cos 阈值扰动 (0.70 ± 0.05, 官方基线) ===")
thr_pert = []
for thr in [0.65, 0.75, 0.80, 0.85]:
    c = covs(nodes_list, gold, thr)
    d = statistics.mean(c) - base_mean
    thr_pert.append({"thr": thr, "mean_cov": round(statistics.mean(c), 4), "delta_mean": round(d, 4)})
    print(f"  thr={thr}: mean={statistics.mean(c):.4f} Δ={d:+.4f}")
max_dB = max(abs(p["delta_mean"]) for p in thr_pert)
print(f"  max|Δ| = {max_dB:.4f}  vs 噪声底 {base_sd:.4f} → {'< 1×sd: 对阈值不敏感' if max_dB < base_sd else '>= 1×sd: 阈值是承重超参, 必须报告敏感性'}")

# C. 对承重结论的影响: cor(cov, n_nodes) 在扰动下是否保持
print("\n=== C. 承重结论 robustness: cor(cov, n_nodes) 在 gold 扰动下 ===")
nn = [len(n) for n in nodes_list]
def cor(x, y):
    mx, my = statistics.mean(x), statistics.mean(y)
    den = math.sqrt(sum((a-mx)**2 for a in x)) * math.sqrt(sum((b-my)**2 for b in y))
    return sum((a-mx)*(b-my) for a, b in zip(x, y)) / den if den else None
base_cor = cor(nn, base)
print(f"  基线 cor = {base_cor:.4f} (draft 承重: 0.563, 30 树口径; 此处 15 树 K7)")
cors = [base_cor]
for p in gold_pert:
    pass  # 重算需要 covs, 上面没存 per-run; 用 seed 1 重算一次
rng = random.Random(1)
keep = set(rng.sample(range(len(gold)), len(gold) - max(1, int(len(gold)*0.10))))
g1 = [gold[i] for i in sorted(keep)]
c1 = covs(nodes_list, g1, 0.70)
pert_cor = cor(nn, c1)
print(f"  gold 扰动 (seed=1, 删 10%) cor = {pert_cor:.4f}  Δ={pert_cor-base_cor:+.4f}")
print(f"  判定: {'cor 方向与量级保持 → 平台/上升结论对 gold 扰动 robust' if abs(pert_cor - base_cor) < 0.15 else 'cor 漂移大 → 承重结论对 gold 构建敏感'}")

out = {"base": {"mean_cov": round(base_mean, 4), "sd": round(base_sd, 4), "n_trees": len(runs)},
       "gold_perturbation_10pct": gold_pert, "max_abs_delta_gold": round(max_dA, 4),
       "threshold_perturbation": thr_pert, "max_abs_delta_thr": round(max_dB, 4),
       "cor_baseline": round(base_cor, 4), "cor_gold_pert_seed1": round(pert_cor, 4),
       "verdict": (f"gold 扰动 max|Δ|={max_dA:.4f} ({'<' if max_dA < base_sd else '>='} 1×sd={base_sd:.4f}); "
                   f"阈值扰动 max|Δ|={max_dB:.4f} ({'<' if max_dB < base_sd else '>='} 1×sd); "
                   f"cor {base_cor:.3f}→{pert_cor:.3f}")}
json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
print(f"\n落盘 {OUT}")
