#!/usr/bin/env python3
"""Q6 719 nodepth (拆墙批, max_depth=10) 落地分析 — draft 核心 claim 的 clean test (K7 待办)

用法: python3 q6_719_nodepth_analyze.py
前置: q6_719_nodepth_queue.sh 3 rep 落地 (data/q6-719-nodepth/q6-719-nd-r{1,2,3}-*.json)

回答的问题 (2026-11-24 深度墙 binding 判定):
  Q6 719 原批 3 rep 全撞 max_depth=4 墙 (realized 197/351/379, 停止时 gain 0.889-0.909 高 +
  frontier 54-94 非空 + low_gain_streak=0 → 墙 actively binding, 非自然饱和)。
  原批 719 档 cov=0.1667 是"被墙切断的下界"。拆墙批 (max_depth=10) 是 clean test:
  - 若 cov 显著高于 0.1667 → 墙确在压制 cov, draft 跨域段"Q6 到 719 仍升"是下界, 真实曲线更高
  - 若 cov ≈ 0.1667 → 墙虽 binding 但深度展开对 cov 贡献小, 原批 0.1667 近似真实值
输出:
  1. 拆墙批 3 rep 的 cov/struct/total/realized n_nodes/max_depth/停止状态
  2. 与原批 719 (cov 0.1667, realized 197/351/379) 的对照
  3. 判定: 墙是否压制 cov (Δ 及方向)
  4. 落盘 data/q6-719-nodepth/q6-719-nodepth-analysis.json
"""
import sys, os, json, glob, re, statistics

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "modules", "B-pipeline-ablation"))
from judge_v1 import judge_run

ND = os.path.join(ROOT, "modules", "B-pipeline-ablation", "data", "q6-719-nodepth")
GOLD = os.path.join(ROOT, "modules", "B-pipeline-ablation", "data", "gold-q6-units.json")
OUT = os.path.join(ND, "q6-719-nodepth-analysis.json")

gold = json.load(open(GOLD))
gu = gold["units"] if isinstance(gold, dict) and "units" in gold else gold
print(f"Q6 gold units: {len(gu)}")

recs = []
for f in sorted(glob.glob(os.path.join(ND, "q6-719-nd-r*.json"))):
    m = re.search(r"q6-719-nd-r(\d+)-", os.path.basename(f))
    if not m:
        continue
    rep = int(m.group(1))
    try:
        rj = judge_run(f, gold_units=gu)
        d = json.load(open(f))
        last = d["rounds"][-1]
        recs.append({
            "rep": rep, "n_nodes": rj["n_nodes_raw"],
            "cov": round(rj["layers"]["coverage"]["coverage"], 4),
            "struct": round(rj["layers"]["structure"]["depth_score"], 4),
            "total": round(rj["total_score"], 4),
            "stop_gain": last.get("gain"), "stop_frontier": last.get("frontier"),
            "stop_streak": last.get("low_gain_streak"),
        })
        print(f"  [nd-r{rep}] n={rj['n_nodes_raw']} cov={rj['layers']['coverage']['coverage']:.4f} "
              f"total={rj['total_score']:.4f} stop_gain={last.get('gain')} frontier={last.get('frontier')}")
    except Exception as e:
        print(f"  [nd-r{rep}-err] {e}")

if not recs:
    print("!! 无落地 run — relay 还没跑到 nodepth 批, 退出")
    sys.exit(0)

cows = [r["cov"] for r in recs]
nn = [r["n_nodes"] for r in recs]
orig_cov = 0.1667  # 原批 719 三 rep 池化 (realized 197/351/379, 撞墙)
orig_nn = [197, 351, 379]
mean_nd = statistics.mean(cows)
delta = mean_nd - orig_cov
print(f"\n拆墙批 cov mean = {mean_nd:.4f} (n={len(recs)}, sd={statistics.stdev(cows) if len(cows)>1 else 0:.4f})")
print(f"原批 719 cov = {orig_cov:.4f} (撞墙, realized {min(orig_nn)}/{max(orig_nn)})")
print(f"Δ = {delta:+.4f}  realized n_nodes: 拆墙 {min(nn)}/{max(nn)} vs 原批 {min(orig_nn)}/{max(orig_nn)}")
if delta > 0.01:
    verdict = "墙压制 cov: 拆墙后 cov 显著高于撞墙下界, 原批 0.1667 是下界, Q6 719 真实 cov 更高"
elif delta < -0.01:
    verdict = "异常: 拆墙后 cov 反而更低 — 需查 (可能 max_depth=10 改变了展开策略)"
else:
    verdict = "墙虽 binding 但对 cov 贡献小: 拆墙后 cov ≈ 原批, 0.1667 近似真实值"
print(f"判定: {verdict}")

out = {
    "batch": "q6-719-nodepth (max_depth=10, clean test)",
    "reps": recs,
    "cov_mean": round(mean_nd, 4),
    "orig_batch_719_cov": orig_cov,
    "delta": round(delta, 4),
    "verdict": verdict,
    "note": "原批 719 撞 max_depth=4 墙 (停止时 gain 0.889-0.909 + frontier 54-94 + streak=0 → actively binding); "
            "本批 max_depth=10 拆墙, 是 draft 跨域段'Q6 到 719 仍升'是下界还是真实值的 clean test",
}

# --- 跨域决定性测试 (2026-11-24 era confound 降级后补入) ---
# 问题: 饱和点是否域依赖? GPU 域 cov 在 ~400 realized 节点后平台化 (30 树分箱 0.250/0.325/0.361/0.361,
#       cor=0.563); Q6 域在 ≤379 realized 节点仍升 (tier means 0.058→0.167)。
# 本批给 Q6 在 ~719 realized 节点的数据点: 平台 → 两域都平台但位置不同 (GPU ~400 < Q6 ~719, 仍域依赖);
# 继续升 → GPU ~400 饱和而 Q6 到 719 未饱和 (强域依赖)。
# 口径: Q6 域内 gold (46 units), cov 取 q6-scan-scores.json (同 judge 同 gold), n_nodes 用真实树 len(nodes)。
# 注意: 跨域绝对 cov 不可比 (gold 不同), 只比形状 (平台 vs 上升)。
scores_path = os.path.join(ROOT, "modules", "B-pipeline-ablation", "data", "q6-budget-scan", "q6-scan-scores.json")
orig = []
if os.path.exists(scores_path):
    for r in json.load(open(scores_path)):
        f = glob.glob(os.path.join(ROOT, f"modules/B-pipeline-ablation/data/q6-budget-scan/q6-{r['budget']}-r{r['rep']}-*.json"))
        if not f:
            continue
        d = json.load(open(f[0]))
        orig.append({"budget": r["budget"], "rep": r["rep"], "n_nodes": len(d.get("nodes", [])), "cov": r["judge"]["cov"]})
allq6 = sorted(orig + [{"budget": "nd719", "rep": r["rep"], "n_nodes": r["n_nodes"], "cov": r["cov"]} for r in recs],
               key=lambda x: x["n_nodes"])
bins = []
for lo, hi in [(0, 100), (100, 200), (200, 300), (300, 400), (400, 800)]:
    sel = [r["cov"] for r in allq6 if lo <= r["n_nodes"] < hi]
    bins.append({"bin": f"{lo}-{hi}", "n": len(sel), "mean": round(sum(sel) / len(sel), 4) if sel else None})
nd_covs = [r["cov"] for r in recs]
low_covs = [r["cov"] for r in allq6 if r["n_nodes"] < 400]
delta_xd = (statistics.mean(nd_covs) - statistics.mean(low_covs)) if nd_covs and low_covs else None
if max(r["n_nodes"] for r in recs) < 700:
    budget_note = f"注意: 拆墙批最大 realized={max(r['n_nodes'] for r in recs)} < 700 — run 在预算前停止 (自然收敛或 depth-10 墙), 不是干净的 ~719 预算测试"
else:
    budget_note = f"拆墙批 realized {min(r['n_nodes'] for r in recs)}/{max(r['n_nodes'] for r in recs)}, 预算 719 为 binding 约束"
if delta_xd is None:
    xd_verdict = "无法判定 (缺数据)"
elif delta_xd > 0.01:
    xd_verdict = f"Q6 在 ~719 realized 节点仍升 (Δ={delta_xd:+.4f} vs ≤379 段) → 饱和点域依赖: GPU ~400 饱和, Q6 到 719 未饱和"
elif delta_xd < -0.01:
    xd_verdict = f"异常: Q6 在 ~719 realized 节点反降 (Δ={delta_xd:+.4f}) — 需查 (max_depth=10 改变展开策略?)"
else:
    xd_verdict = f"Q6 在 ~719 realized 节点平台化 (Δ={delta_xd:+.4f}) → 两域都平台但位置不同 (GPU ~400 < Q6 ~719), 位置仍域依赖"
print(f"\n=== 跨域决定性测试 (realized-node-count 轴) ===")
print(f"Q6 全曲线分箱 (原批 15 + 拆墙 {len(recs)}): " + " / ".join(f"{b['bin']}: {b['mean']} (n={b['n']})" for b in bins))
print(f"{budget_note}")
print(f"跨域判定: {xd_verdict}")

out["cross_domain"] = {
    "q6_bins_by_realized": bins,
    "delta_nd_vs_low": round(delta_xd, 4) if delta_xd is not None else None,
    "budget_binding_note": budget_note,
    "verdict": xd_verdict,
    "gpu_reference": "GPU 30 树分箱 0.250/0.325/0.361/0.361 (0-200/200-400/400-600/600-800), 平台 ~400 realized 节点, cor=0.563 (K7 2026-11-24)",
    "caveat": "跨域绝对 cov 不可比 (Q6 46-unit gold vs GPU 36-unit gold), 只比形状",
}
json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
print(f"\n落盘 {OUT}")
