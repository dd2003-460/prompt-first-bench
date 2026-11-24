#!/usr/bin/env python3
"""Q7 budget scan 全曲线分析 (2026-11-23 23:00)

Q7 扫描 (15 runs) 落地后一键出数 — 与 q6_full_curve.py / q6_719_axis.py 同模式,
第三域 (GPU + Q6 + Q7) 验证 general methodology。幂等: glob q7-*.json, 跑几次都行。

输出 (stdout + 落盘 data/q7-budget-scan/q7-full-analysis.json):
  1. 每档 (50/100/150/300/719) × 3 rep: n_nodes (realized), 停止原因
     (stdout max_depth/max_nodes 行 — 承重归因核验, 不能从"提前停"推断)
  2. 域内 cov (Q7 gold 52 units, judge_v1 官方口径 n_confirmed)
  3. 跨域 cov (GPU gold 36, 同 Q6 扫描口径)
  4. mon_claim (CUR 官方 8-pattern 中文口径, 与 q6_full_curve.py 一致)
  5. repair 跨域 (固化口径: rework_count>0 且最终 verified, 同 GPU 331/8870)
  6. realized node count 排序后的域内 cov 单调性检查 (Q6 关键发现的复现)

用法: /usr/bin/python3 q7_full_analysis.py
前置: q7 扫描 15/15 落地 (q7-scan-scores.json 15 条)
"""
import sys, os, json, glob, re, statistics as st

HERE = os.path.dirname(os.path.abspath(__file__))
BPL = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, BPL)
from judge_v1 import judge_run
from metacog_axis import load_run_nodes

SCAN = os.path.join(BPL, "data", "q7-budget-scan")
OUT = os.path.join(SCAN, "q7-full-analysis.json")
CUR = re.compile(r"\[待核验\]|不确定|未验证|待确认|需要验证|无法确定|缺乏数据|信息不足")

gq7 = json.load(open(os.path.join(BPL, "data", "gold-q7-units.json")))
gg = json.load(open(os.path.join(BPL, "gold-gpu-units.json")))
gq7_units = gq7["units"] if isinstance(gq7, dict) else gq7
gg_units = gg["units"] if isinstance(gg, dict) else gg

files = sorted(glob.glob(os.path.join(SCAN, "q7-*-r*-[0-9]*.json")))
if not files:
    print(f"no q7 run files in {SCAN} — scan not landed yet")
    sys.exit(0)

recs = []
tot_rw = tot_fix = 0
for f in files:
    m = re.search(r"q7-(\d+)-r(\d+)-", os.path.basename(f))
    budget, rep = int(m.group(1)), int(m.group(2))
    rj_q = judge_run(f, gold_units=gq7_units)
    rj_g = judge_run(f, gold_units=gg_units)
    nodes = load_run_nodes(f)
    hits = sum(1 for n in nodes if CUR.search(n.get("claim", "")))
    stop = "UNKNOWN"
    sp = os.path.join(SCAN, f"q7-{budget}-r{rep}.stdout")
    if os.path.exists(sp):
        for line in open(sp, errors="ignore"):
            if "max_depth=" in line or "max_nodes=" in line:
                stop = line.strip()
    for n in json.load(open(f)).get("nodes", []):
        try: rc = int(n.get("rework_count", 0) or 0)
        except Exception: rc = 0
        if rc > 0:
            tot_rw += 1
            if n.get("status") == "verified": tot_fix += 1
    recs.append({
        "budget": budget, "rep": rep, "n_nodes": rj_q["n_nodes_raw"], "stop": stop,
        "in_cov": round(rj_q["layers"]["coverage"]["coverage"], 4),
        "in_cov_n": f"{rj_q['layers']['coverage']['n_confirmed']}/52",
        "cross_cov": round(rj_g["layers"]["coverage"]["coverage"], 4),
        "cross_cov_n": rj_g["layers"]["coverage"]["n_confirmed"],
        "depth": rj_q["layers"]["structure"]["depth_score"],
        "total": round(rj_q["total_score"], 4),
        "mon_claim": round(hits / len(nodes), 4) if nodes else None,
        "mon_claim_n": f"{hits}/{len(nodes)}",
    })

# 按 realized node count 排序的域内 cov 单调性 (Q6 关键发现复现)
by_realized = sorted(recs, key=lambda r: r["n_nodes"])
mono = all(by_realized[i]["in_cov"] <= by_realized[i+1]["in_cov"] + 1e-9
           for i in range(len(by_realized)-1))
mono_seq = " ".join(f"{r['n_nodes']}→{r['in_cov']}" for r in by_realized)

# --- realized-node-count 轴分箱 + 平台检测 (2026-11-24 era confound 降级后补入) ---
# 核心 claim 现口径在 realized 节点数轴上 (GPU 30 树平台 ~400, cor=0.563)。Q7 是第三域,
# 落地后必须直接出三域 realized 轴对比, 不能只给单调性。
# 口径: 域内 cov (Q7 gold 52 units), n_nodes 用 judge 的 n_nodes_raw (同棵树, 与 Q6 nodepth 脚本一致)。
q7_bins = []
for lo, hi in [(0, 100), (100, 200), (200, 400), (400, 800)]:
    sel = [r["in_cov"] for r in recs if lo <= r["n_nodes"] < hi]
    q7_bins.append({"bin": f"{lo}-{hi}", "n": len(sel),
                    "mean": round(sum(sel) / len(sel), 4) if sel else None})
# 平台检测: 最高两箱均值差 + 噪声底 (2026-11-24 修: 只报 gap 数值不够 — GPU 的 0.0000 差就在
# 噪声底 sd≈0.078 内, "gap≈0=平台" 的判读会把噪声当平台; 必须报 gap vs 1×sd 的比值)
filled = [b for b in q7_bins if b["mean"] is not None]
plateau = None
plateau_vs_noise = None
if len(filled) >= 2:
    top2 = filled[-2:]
    plateau = round(abs(top2[0]["mean"] - top2[1]["mean"]), 4)
    # 噪声底: 全部 run 的 cov sd → 两箱均值差的 1×sd = sd*sqrt(1/n1 + 1/n2)
    import math as _m
    _sds = st.stdev([r["in_cov"] for r in recs]) if len(recs) >= 2 else 0.05
    plateau_vs_noise = round(plateau / (_sds * _m.sqrt(1/top2[0]["n"] + 1/top2[1]["n"])), 2)
xs = [r["n_nodes"] for r in recs]; ys = [r["in_cov"] for r in recs]
if len(xs) >= 3:
    import math
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    den = math.sqrt(sum((x - mx) ** 2 for x in xs)) * math.sqrt(sum((y - my) ** 2 for y in ys))
    q7_cor = round(sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / den, 4) if den else None
else:
    q7_cor = None

# --- 机制锚 v4: 分段线性断点扫描 (model-agnostic, 2026-11-24 补入) ---
# v3 只测 log + 饱和 (都失败) 是单边的; v4 用断点扫描直接测"断点在哪最优"。
# GPU 最优断点 425 / Q6 325, 断点位置跨域一致 (~300-425) 是机制锚 v4 的核心发现。
# Q7 落地后第三域断点: 若也在 ~300-425 → 三域一致, 机制锚从 n=2 变 n=3。
def _linreg_ss(p):
    n = len(p); mx = sum(x for x, _ in p) / n; my = sum(y for _, y in p) / n
    sxy = sum((x - mx) * (y - my) for x, y in p); sxx = sum((x - mx) ** 2 for x, _ in p)
    a = sxy / sxx if sxx else 0.0; b = my - a * mx
    return a, b, sum((y - (a * x + b)) ** 2 for x, y in p)
q7_bp = None
if len(xs) >= 8:
    pts_sorted = sorted(zip(xs, ys))
    _ss1 = _linreg_ss(pts_sorted)[2]
    _best = None
    for _bp in range(150, 700, 25):
        _L = [(x, y) for x, y in pts_sorted if x < _bp]
        _R = [(x, y) for x, y in pts_sorted if x >= _bp]
        if len(_L) < 3 or len(_R) < 3:
            continue
        if len(set(x for x, _ in _L)) < 2 or len(set(x for x, _ in _R)) < 2:
            continue  # 退化段: distinct x < 2 → ss=0 是假象 (2026-11-24 补, 同 18pt 脚本)
        _a1, _b1, _s1 = _linreg_ss(_L); _a2, _b2, _s2 = _linreg_ss(_R)
        if _best is None or _s1 + _s2 < _best[0]:
            _best = (_s1 + _s2, _bp, _a1, _a2)
    if _best:
        # F 检验 (与 18pt/GPU v4 同口径): F = ((ss1-ss2)/2) / (ss2/(n-4)), p 用 F(2,n-4) sf
        _n_pts = len(pts_sorted)
        _F = ((_ss1 - _best[0]) / 2) / (_best[0] / (_n_pts - 4)) if _best[0] > 0 else float('inf')
        try:
            from scipy import stats as _st
            _p = float(_st.f.sf(_F, 2, _n_pts - 4))
        except ImportError:
            _p = ((_n_pts - 4) / ((_n_pts - 4) + 2 * _F)) ** ((_n_pts - 4) / 2)  # 闭式 (df1=2), 与 scipy 一致 (11-24 验证)
        q7_bp = {"ss_single": round(_ss1, 5), "ss_two_seg": round(_best[0], 5),
                 "optimal_bp": _best[1], "slope_left": round(_best[2], 5),
                 "slope_right": round(_best[3], 5),
                 "F": round(_F, 3), "df": [2, _n_pts - 4], "p": round(_p, 4),
                 "improvement": round((_ss1 - _best[0]) / _ss1, 4) if _ss1 else None}
# --- 机制锚 v2: 停止状态通用签名检查 (2026-11-24 补入) ---
# 全 30 树 (GPU+Q6) 每档都 高 gain + 非空 frontier + streak=0 → 停止状态是通用签名,
# 平台是 cov 现象不是停止状态现象。Q7 落地后第三域验证: 若 Q7 也全档同型 → 三域一致。
q7_stop = []
for f in files:
    _d = json.load(open(f))
    _rounds = _d.get("rounds", [])
    if _rounds:
        _lr = _rounds[-1]
        _fr = _lr.get("frontier", 0)
        if isinstance(_fr, list): _fr = len(_fr)
        q7_stop.append({"gain": _lr.get("gain"), "frontier": _fr,
                        "streak": _lr.get("low_gain_streak"),
                        "final_state": _d.get("final_state")})
q7_stop_universal = all(s.get("streak") == 0 and (s.get("frontier") or 0) > 0
                        and (s.get("gain") or 0) > 0.8 for s in q7_stop) if q7_stop else None

print(f"\n=== Q7 realized-node-count 轴 (第三域) ===")
print(f"  分箱: " + " / ".join(f"{b['bin']}: {b['mean']} (n={b['n']})" for b in q7_bins))
print(f"  最高两箱差 = {plateau}  (vs 噪声底 1×sd = {plateau_vs_noise}×; <1 = 差在噪声内, 平台判读不 robust; GPU 参照: 0.0000/0.078 差, 已标 n=5 caveat)")
print(f"  cor(in_cov, realized) = {q7_cor}  (GPU 参照: 0.563)")
if q7_bp:
    print(f"  断点扫描 (机制锚 v4): 单段 ss={q7_bp['ss_single']} → 两段 ss={q7_bp['ss_two_seg']} "
          f"(改善 {q7_bp['improvement']*100:.0f}%), 最优断点={q7_bp['optimal_bp']} "
          f"(斜率 {q7_bp['slope_left']}→{q7_bp['slope_right']}), F={q7_bp['F']} p={q7_bp['p']}")
    # 2026-11-24 修: "三域一致" 必须带 p 值条件 — Q6 p=0.100 / GPU p=0.074 都不显著,
    # draft 口径是 "cannot confirm or refute"; 若 Q7 p 也不显著, 输出 "三域一致" 会
    # 比 draft 强, 违反 verdict 与 draft 降级一致约束。
    _pos_ok = 300 <= q7_bp["optimal_bp"] <= 425
    if _pos_ok and q7_bp["p"] < 0.05:
        _verdict = "三域一致 (~300-425) 且显著"
    elif _pos_ok:
        _verdict = f"位置在 ~300-425 区间但 p={q7_bp['p']} 不显著 — 位置一致, 强度不可确认 (同 Q6/GPU 降级口径)"
    else:
        _verdict = f"Q7 断点 {q7_bp['optimal_bp']} 偏离 ~300-425, 需查"
    print(f"    三域断点: GPU 425 (p=0.074) / Q6 325 (p=0.100) / Q7 {q7_bp['optimal_bp']} (p={q7_bp['p']}) → {_verdict}")
if q7_stop is not None:
    print(f"  停止状态 (机制锚 v2): {len(q7_stop)} runs, 全档 高gain+非空frontier+streak=0: {q7_stop_universal}")
print(f"  三域 realized 轴: GPU 平台 ~400 / Q6 ~400 后不再升 (nd-r1 719 回落 0.1304, n=1, r2/r3 定 n=3) / Q7 见上")

out = {
    "n_runs": len(recs),
    "runs": recs,
    "in_cov_monotonic_in_realized": mono,
    "in_cov_by_realized": mono_seq,
    "realized_axis": {
        "q7_bins_by_realized": q7_bins,
        "top2_bin_gap": plateau,
        "cor_in_cov_realized": q7_cor,
        "breakpoint_scan_v4": q7_bp,
        "stop_state_universal_v2": q7_stop_universal,
        "stop_states": q7_stop,
        "three_domain_reference": "GPU 平台 ~400 realized 节点 (30 树分箱 0.250/0.325/0.361/0.361, cor=0.563, 断点扫描最优 425); "
                                  "Q6 ~400 后不再升 (16 点分箱 0.078/0.152/0.130, 断点扫描最优 325; nd-r1 719 回落 0.1304, n=1, r2/r3 定 n=3); "
                                  "Q7 见 q7_bins_by_realized + breakpoint_scan_v4",
        "caveat": "跨域绝对 cov 不可比 (gold 不同: Q7 52 / Q6 46 / GPU 36 units), 只比形状 (平台 vs 上升)",
    },
    "repair": {"fixed": tot_fix, "rework": tot_rw,
               "rate": round(tot_fix / tot_rw, 4) if tot_rw else None},
    "note": ("第三域验证 (GPU+Q6+Q7)。域内 cov 用 Q7 gold 52 units; 跨域用 GPU gold 36; "
             "mon_claim = CUR 官方 8-pattern; repair 固化口径同 GPU 331/8870。"
             "realized 轴分箱 + 平台检测为 2026-11-24 era confound 降级后补入 (核心 claim 现口径在 realized 节点数轴)。"
             "719 档 max_depth=10 (D 2026-11-23 指令'不要限制深度'), 停止原因逐 run 核验, 不从'提前停'推断"),
}
json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
for r in sorted(recs, key=lambda x: (x["budget"], x["rep"])):
    print(f"  b{r['budget']} r{r['rep']}: n={r['n_nodes']} in_cov={r['in_cov']}({r['in_cov_n']}) "
          f"cross={r['cross_cov']} mon={r['mon_claim_n']} | {r['stop'][-40:]}")
print(f"  in_cov 按 realized 单调非降: {mono}")
print(f"  seq: {mono_seq}")
print(f"  repair: {out['repair']['fixed']}/{out['repair']['rework']} = "
      f"{(out['repair']['rate'] or 0)*100:.1f}%")
print(f"  → {os.path.basename(OUT)}")
