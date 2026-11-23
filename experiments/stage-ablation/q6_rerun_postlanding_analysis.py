#!/usr/bin/env python3
# origin: ai · 2026-11-23 23:45 · Q6 重跑批落地后一条命令出全部判据
# 三个可检验预测 (TL;DR 终态块):
#   P1 rep 独立性: 重跑批 rep 间 claim 级节点重叠率 < 原批 (id 伪影已证, 必须按 claim 内容算)
#   P2 rep sd 回升: 重跑 sd > 原批 sd × 1.3 (脚本内置, 此处重算 + bootstrap CI 补 power)
#   P3 域内 gold 后评: 重跑批换 Q6 gold 重评 coverage (消除跨域噪声, 绝对分才可信)
# 用法: /usr/bin/python3 q6_rerun_postlanding_analysis.py
import sys, json, os, glob, statistics as st, re
sys.path.insert(0, '/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation')

ORIG = "/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/q6-budget-scan"
RERUN = "/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/q6-budget-scan-rerun"
Q6_GOLD = "/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/gold-q6-units.json"

def load_scores(d):
    p = os.path.join(d, "q6-rerun-scores.json") if "rerun" in d else os.path.join(d, "q6-scan-scores.json")
    try: return json.load(open(p))
    except Exception: return []

def load_runs(d, budget):
    """最新 ts 的 run json 每 rep 一个"""
    files = sorted(glob.glob(os.path.join(d, f"q6-{budget}-r*-*.json")))
    by_rep = {}
    for f in files:
        m = re.search(rf"q6-{budget}-r(\d+)-\d{{8}}-\d{{6}}\.json$", f)
        if m: by_rep[int(m.group(1))] = f  # sorted → 最新 ts 覆盖
    return {rep: json.load(open(f))["nodes"] for rep, f in by_rep.items()}

def claim_sets(nodes):
    """claim 内容级集合 (normalized)"""
    return {re.sub(r"\s+", "", n.get("claim", "")) for n in nodes if n.get("claim")}

def overlap_rate(nodes_a, nodes_b):
    """claim 级重叠率: A 中有多少 claim 在 B 里 (embedding 余弦 ≥0.85 视为同 claim)"""
    from sentence_transformers import SentenceTransformer
    import numpy as np
    ca, cb = claim_sets(nodes_a), claim_sets(nodes_b)
    if not ca or not cb: return 0.0
    model = SentenceTransformer("all-MiniLM-L6-v2")
    ea = model.encode(list(ca), normalize_embeddings=True)
    eb = model.encode(list(cb), normalize_embeddings=True)
    sim = ea @ eb.T
    return float((sim.max(axis=1) >= 0.85).mean())

def bootstrap_sd_ratio(x, y, n_boot=2000, seed=42):
    """两样本 sd 比值的 bootstrap 95% CI (补 n=3 power 缺口)"""
    import random
    random.seed(seed)
    ratios = []
    for _ in range(n_boot):
        bx = [random.choice(x) for _ in x]
        by = [random.choice(y) for _ in y]
        sx, sy = st.stdev(bx), st.stdev(by)
        if sy > 0: ratios.append(sx / sy)
    ratios.sort()
    return ratios[int(0.025 * n_boot)], ratios[int(0.975 * n_boot)], st.mean(ratios)

print("=" * 70)
print("P1: rep 间 claim 级节点重叠率 (原批 vs 重跑批)")
print("=" * 70)
for budget in [300, 719]:
    for label, d in [("原批", ORIG), ("重跑批", RERUN)]:
        runs = load_runs(d, budget)
        reps = sorted(runs)
        if len(reps) < 2:
            print(f"  {budget} {label}: 仅 {len(reps)} rep, 不可算")
            continue
        ov = overlap_rate(runs[reps[0]], runs[reps[1]])
        print(f"  {budget} {label} r{reps[0]}×r{reps[1]}: {ov*100:.1f}%")

print()
print("=" * 70)
print("P2: rep sd 回升 (重跑/原批 比值 + bootstrap 95% CI)")
print("=" * 70)
orig_s, rerun_s = load_scores(ORIG), load_scores(RERUN)
for budget in [300, 719]:
    for axis in ["judge", "metacog"]:
        ov = [r[axis]["total"] for r in orig_s if r.get("budget") == budget]
        rv = [r[axis]["total"] for r in rerun_s if r.get("budget") == budget]
        if len(ov) < 2 or len(rv) < 2:
            print(f"  {budget} {axis}: n 不足 (orig={len(ov)}, rerun={len(rv)})")
            continue
        so, sr = st.stdev(ov), st.stdev(rv)
        lo, hi, mean = bootstrap_sd_ratio(rv, ov)
        verdict = "↑ 回升(支持)" if sr > so * 1.3 else "≈ 持平(未支持,未排除)"
        print(f"  {budget} {axis:<8} orig_sd={so:.4f} rerun_sd={sr:.4f} ratio={sr/so:.2f} "
              f"CI95=[{lo:.2f},{hi:.2f}] → {verdict}")

print()
print("=" * 70)
print("P3: 域内 gold 后评 (Q6 gold, 消除跨域噪声)")
print("=" * 70)
from judge_v1 import judge_run
_gu = json.load(open(Q6_GOLD))
for label, d in [("原批", ORIG), ("重跑批", RERUN)]:
    for budget in [300, 719]:
        files = sorted(glob.glob(os.path.join(d, f"q6-{budget}-r1-*.json")))
        if not files:
            print(f"  {label} {budget}-r1: 无文件")
            continue
        f = files[-1]
        try:
            rj = judge_run(f, gold_units=_gu)
            print(f"  {label} {budget}-r1: cov={rj['layers']['coverage']['coverage']:.3f} "
                  f"total={rj['total_score']:.3f} (Q6 gold)")
        except Exception as e:
            print(f"  {label} {budget}-r1: 失败 {type(e).__name__}: {e}")
        # 每档只评 r1 (后评是口径修正, 不是 rep 判据)
print()
print("DONE — 判据解读: P1 重跑<原批 + P2 ratio>1.3 且 CI 下界>1 → rep 独立性成立;")
print("  若 P2 持平但 P1 显著低 → cache 共享主要锁内容而非方差 (见混杂节: source 新鲜度)")
