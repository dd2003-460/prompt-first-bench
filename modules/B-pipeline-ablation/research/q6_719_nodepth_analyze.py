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
json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
print(f"\n落盘 {OUT}")
