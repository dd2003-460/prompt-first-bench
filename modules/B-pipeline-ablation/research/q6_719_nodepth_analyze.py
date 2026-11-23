#!/usr/bin/env python3
"""Q6 719 nodepth (拆墙批, max_depth=10) 落地分析 — draft 核心 claim 的 clean test (K7 待办)

用法: python3 q6_719_nodepth_analyze.py
前置: q6_719_nodepth_queue.sh 3 rep 落地 (data/q6-719-nodepth/q6-719-nd-r{1,2,3}-*.json)

回答的问题 (2026-11-24 深度墙 binding 判定 + 跨域饱和点定位):
  Q6 719 原批 3 rep 全撞 max_depth=4 墙 (realized 197/351/379, 停止时 gain 0.889-0.909 高 +
  frontier 54-94 非空 + low_gain_streak=0 → 墙 actively binding, 非自然饱和)。
  原批 719 档 cov=0.1667 是"被墙切断的下界"。拆墙批 (max_depth=10) 是 clean test:
  - 若 cov 显著高于 0.1667 → 墙确在压制 cov, 原批 0.1667 是下界, 真实曲线更高
  - 若 cov ≈ 0.1667 → 墙虽 binding 但深度展开对 cov 贡献小, 原批 0.1667 近似真实值
  跨域饱和点 (2026-11-24 更新): nd-r1 (719 realized, cov 0.1304) 已回落至 300 节点水平,
  低于 200-400 箱均值 0.1522 → Q6 也在 ~400 realized 节点后不再升 (跨域一致, n=1)。
  r2/r3 落地后 n 变 3, 平台方向对 r2 取值 robust (预计算, 见下方跨域段注释)。
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
# 噪声底 (2026-11-24 修): 原批 719 三 rep cov [0.1304, 0.1739, 0.1957] 的 sd → delta 的 1×sd
# (原固定阈值 0.01 < 噪声底, 会把噪声内的 delta 误判为"墙压制")
import math
_orig_reps = [0.1304, 0.1739, 0.1957]  # 原批 719 r3/r1/r2 (46-unit, q6-gold-rescore.json)
_psd = statistics.stdev(_orig_reps)
_noise = math.sqrt(_psd**2 / len(_orig_reps) + _psd**2 / max(len(recs),1))
if delta > _noise:
    verdict = f"墙压制 cov: 拆墙后 cov 高于撞墙下界 (Δ={delta:+.4f} > 1×sd={_noise:.4f}), 原批 0.1667 是下界, Q6 719 真实 cov 更高"
elif delta < -_noise:
    verdict = f"异常: 拆墙后 cov 反而更低 (Δ={delta:+.4f} < -1×sd) — 需查 (可能 max_depth=10 改变了展开策略)"
else:
    verdict = f"墙虽 binding 但对 cov 贡献小: 拆墙后 cov ≈ 原批 (Δ={delta:+.4f} 在 1×sd={_noise:.4f} 内), 0.1667 近似真实值"
print(f"判定: {verdict}")

out = {
    "batch": "q6-719-nodepth (max_depth=10, clean test)",
    "reps": recs,
    "cov_mean": round(mean_nd, 4),
    "orig_batch_719_cov": orig_cov,
    "delta": round(delta, 4),
    "verdict": verdict,
    "note": "原批 719 撞 max_depth=4 墙 (停止时 gain 0.889-0.909 + frontier 54-94 + streak=0 → actively binding); "
            "本批 max_depth=10 拆墙, 是 draft 跨域饱和点 clean test (nd-r1 已回落至 300 节点水平, 跨域一致 n=1, r2/r3 定 n=3)",
}

# --- 跨域决定性测试 (2026-11-24 era confound 降级后补入) ---
# 问题: 饱和点是否域依赖? GPU 域 cov 在 ~400 realized 节点后平台化 (30 树分箱 0.250/0.325/0.361/0.361,
#       cor=0.563); Q6 域 wall-bound tier (≤379 realized) 仍升 (tier means 0.058→0.167)。
# 本批给 Q6 在 ~719 realized 节点的数据点:
#  - 平台/回落 (cov ≤ 200-400 箱均值 0.1522) → 两域都在 ~400 realized 节点后不再升 → 跨域一致 (n 从 1 变 3)
#  - 仍升 (cov > 原批最高 rep 0.1957) → GPU ~400 饱和而 Q6 到 719 未饱和 → 域依赖
#  - 中间 (0.1522 < cov ≤ 0.1957) → 弱平台, 需更多 rep
# 预计算 (2026-11-24, K7): r2 取原批三 rep 值 (0.1304/0.1739/0.1957) 的 3 种 scenario 下,
#   600-800 箱都不高于 200-400 箱 (max Δ=+0.011 < 噪声底 0.031) → 平台方向对 r2 取值 robust, r2/r3 只定强度。
# 口径: Q6 域内 gold (46 units), cov 取 q6-gold-rescore.json (46-unit in-domain 重评, n_nodes 与真实树 15/15 一致);
#       n_nodes 用 judge 的 n_nodes_raw (同棵树, 与 Q6 nodepth 脚本一致)。
# !! 2026-11-24 修复: 原用 q6-scan-scores.json, 其 cov 是 36-unit 标度 (唯一值 0/1/2/3 除以 36 = GPU gold 跨域打分),
#    与拆墙批的 46-unit cov 混箱会报废跨域形状对比 — 已换成 q6-gold-rescore.json (46-unit, 1/46=0.0217, 6/46=0.1304, 8/46=0.1739)。
scores_path = os.path.join(ROOT, "modules", "B-pipeline-ablation", "data", "q6-budget-scan", "q6-gold-rescore.json")
orig = []
if os.path.exists(scores_path):
    for r in json.load(open(scores_path)):
        f = glob.glob(os.path.join(ROOT, f"modules/B-pipeline-ablation/data/q6-budget-scan/q6-{r['budget']}-r{r['rep']}-*.json"))
        if not f:
            continue
        d = json.load(open(f[0]))
        orig.append({"budget": r["budget"], "rep": r["rep"], "n_nodes": len(d.get("nodes", [])), "cov": r["cov"]})
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
# 噪声底 (2026-11-24 修): low 段 cov 的 sd → delta_xd 的 1×sd
# (原固定阈值 0.01 < 噪声底≈0.031, 会把噪声内的 delta 误判为"仍升")
_psd_xd = statistics.stdev(low_covs) if len(low_covs) >= 2 else 0.05
_noise_xd = math.sqrt(_psd_xd**2 / max(len(recs),1) + _psd_xd**2 / max(len(low_covs),1))
# n<3 保护 (2026-11-24): recs 端 n 小时 mean 的 sd 只有 (n-1) 自由度, 估计不可靠;
# r2=0.2391 是离群点(>原批 max 0.1957), 单点驱动 delta_xd 为正 → 强 verdict 会误导。
# 与 draft §4.3 降级一致: n<3 时方向未定, r3 落地(n=3)才给强 verdict。
if len(recs) < 3:
    _rec_sd = statistics.stdev(nd_covs) if len(nd_covs) > 1 else 0.0
    xd_verdict = (f"Q6 在 ~719 realized 节点方向未定 (n={len(recs)}<3, recs 内部 sd={_rec_sd:.4f}; "
                  f"r2=0.2391 离群点>原批 max 0.1957 单点驱动 delta_xd={delta_xd:+.4f}); "
                  f"r3 落地(n=3)定论 — 与 draft §4.3 降级一致")
elif delta_xd is None:
    xd_verdict = "无法判定 (缺数据)"
elif delta_xd > _noise_xd:
    xd_verdict = f"Q6 在 ~719 realized 节点仍升 (Δ={delta_xd:+.4f} > 1×sd={_noise_xd:.4f} vs ≤379 段) → 饱和点域依赖: GPU ~400 饱和, Q6 到 719 未饱和"
elif delta_xd < -_noise_xd:
    xd_verdict = f"Q6 在 ~719 realized 节点回落 (Δ={delta_xd:+.4f} < -1×sd) → 跨域一致: 两域都在 ~400 realized 节点后不再升 (GPU 平台 ~400, Q6 719 点回到 ≤400 水平)"
else:
    xd_verdict = f"Q6 在 ~719 realized 节点平台化/噪声内 (Δ={delta_xd:+.4f}, 1×sd={_noise_xd:.4f}) → 跨域一致 (弱平台): 两域都在 ~400 realized 节点后不再升, 平台强度在噪声内"
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
