#!/usr/bin/env python3
"""Q6 rep 独立重跑批 vs 原批 方差对照 (2026-11-23 23:42)

判据轴: metacog total (gold-free, 细粒度, 有真实 rep 方差)。
cov 轴不可用: 300 节点下 46-unit 分辨率饱和 (sd=0 是分辨率产物, 非 cache 效应)。
judge total 轴: 300/719 两档跨域 cov 逐位相同 (0.0/0.0833/0.0556, 已核验为
通用硬件成本概念真实收敛, query/claim 重叠 0%), 方差被 cov 离散化压低, 次选。

★ 统计功效修正 (外部会话 085a53014): n=3 sd 的 df=2, "重跑 sd > 原批 sd × 1.3"
阈值 power 极低 — "持平"只能读作"未支持压低假设", 不能读作"排除"。
本脚本用 bootstrap ratio CI (重跑 sd / 原批 sd 的分布) 替代单点 1.3x 阈值:
  - CI 下界 > 1.0 → 方差回升 (cache 共享压低假设支持)
  - CI 含 1.0 → 无结论 (power 不足, 需 n>=5)
  - CI 上界 < 1.0 → 方差降低 (反常, 需查)

原批基线 (本脚本实算, 非 prose):
  300 档 metacog total = [0.1703, 0.1698, 0.2227] sd=0.0304
  719 档 metacog total = [0.2304, 0.2676, 0.2104] sd=0.0290

用法: /usr/bin/python3 q6_rerun_variance_check.py (重跑批 6 runs 落地后)
落盘: data/q6-budget-scan-rerun/q6-rerun-variance.json
"""
import sys, os, json, glob, random, statistics as st

HERE = os.path.dirname(os.path.abspath(__file__))
BPL = os.path.abspath(os.path.join(HERE, ".."))
ORIG = os.path.join(BPL, "data", "q6-budget-scan")
RERUN = os.path.join(BPL, "data", "q6-budget-scan-rerun")
OUT = os.path.join(RERUN, "q6-rerun-variance.json")
random.seed(42)

orig = json.load(open(os.path.join(ORIG, "q6-scan-scores.json")))
rerun_f = os.path.join(RERUN, "q6-rerun-scores.json")
rerun = json.load(open(rerun_f)) if os.path.exists(rerun_f) else []

def bootstrap_sd_ratio(a, b, n_boot=10000):
    """sd(b)/sd(a) 的 bootstrap 分布 (resample b, a 固定为基线)。"""
    ratios = []
    for _ in range(n_boot):
        bs = [b[random.randrange(len(b))] for _ in range(len(b))]
        sa, sb = st.stdev(a), st.stdev(bs)
        if sa > 0:
            ratios.append(sb / sa)
    ratios.sort()
    return ratios[int(0.025 * len(ratios))], ratios[int(0.975 * len(ratios))], st.mean(ratios)

def stop_reason(b, rep):
    """读 run 的 stdout 停止原因 (max_nodes/max_depth/DONE)。
    stdout 文件名 = q6-{b}-r{rep}.stdout (无时间戳), json 名带时间戳 — 不能从 json 名推。"""
    sp = os.path.join(RERUN, f"q6-{b}-r{rep}.stdout")
    if os.path.exists(sp):
        for line in open(sp, errors="ignore"):
            if "max_depth=" in line or "max_nodes=" in line:
                return line.strip()[-30:]
    return "?"

results = {}
for b in [300, 719]:
    oa = [r["metacog"]["total"] for r in orig if r.get("budget") == b]
    ra = [r["metacog"]["total"] for r in rerun if r.get("budget") == b]
    # 停止机制 (★ 300-r1 重跑撞 max_depth=4, 原批 300 全 max_nodes=300 — 机制不同, 对照需标注)
    r_stops = []
    for r in rerun:
        if r.get("budget") == b:
            r_stops.append(stop_reason(b, r.get("rep")))
    entry = {"orig_n": len(oa), "rerun_n": len(ra),
             "orig_sd": round(st.stdev(oa), 4) if len(oa) >= 2 else None,
             "rerun_sd": round(st.stdev(ra), 4) if len(ra) >= 2 else None,
             "orig_vals": oa, "rerun_vals": ra,
             "rerun_stops": r_stops,
             "stop_mechanism_note": ("原批 300 档全 max_nodes=300 (预算约束); 重跑 300-r1 撞 max_depth=4 (252 节点, 深度约束) — "
                                     "停止机制不同, 树大小不同, metacog 分对照需标注此混杂")}
    if len(oa) >= 2 and len(ra) >= 2:
        lo, hi, mean = bootstrap_sd_ratio(oa, ra)
        entry["sd_ratio_mean"] = round(mean, 3)
        entry["sd_ratio_ci95"] = [round(lo, 3), round(hi, 3)]
        if lo > 1.0:
            entry["verdict"] = "↑ 方差回升 — cache 共享压低假设支持 (CI 下界>1)"
        elif hi < 1.0:
            entry["verdict"] = "↓ 方差降低 — 反常, 需查"
        else:
            entry["verdict"] = "≈ CI 含 1.0 — 无结论 (n=3 power 不足, 需 n>=5 或延长重跑)"
    else:
        entry["verdict"] = f"数据不足 (orig n={len(oa)}, rerun n={len(ra)})"
    results[b] = entry

out = {"axis": "metacog total (gold-free)",
       "note": ("cov 轴不可用 (300 节点 46-unit 分辨率饱和); judge total 次选 "
                "(跨域 cov 离散化)。n=3 df=2, 单点 1.3x 阈值 power 极低, "
                "bootstrap ratio CI 替代。'无结论' ≠ '排除压低'。"),
       "tiers": results}
json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
for b, e in results.items():
    print(f"  b{b}: orig sd={e['orig_sd']} (n={e['orig_n']}) vs rerun sd={e['rerun_sd']} (n={e['rerun_n']}) "
          f"ratio CI95={e.get('sd_ratio_ci95')} → {e['verdict']}")
print(f"  → {os.path.basename(OUT)}")
