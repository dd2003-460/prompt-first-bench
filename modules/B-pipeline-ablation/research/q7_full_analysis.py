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
# 平台检测: 最高两箱均值差 (参照 GPU 0.361/0.361 判平台)
filled = [b for b in q7_bins if b["mean"] is not None]
plateau = None
if len(filled) >= 2:
    top2 = filled[-2:]
    plateau = round(abs(top2[0]["mean"] - top2[1]["mean"]), 4)
xs = [r["n_nodes"] for r in recs]; ys = [r["in_cov"] for r in recs]
if len(xs) >= 3:
    import math
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    den = math.sqrt(sum((x - mx) ** 2 for x in xs)) * math.sqrt(sum((y - my) ** 2 for y in ys))
    q7_cor = round(sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / den, 4) if den else None
else:
    q7_cor = None
print(f"\n=== Q7 realized-node-count 轴 (第三域) ===")
print(f"  分箱: " + " / ".join(f"{b['bin']}: {b['mean']} (n={b['n']})" for b in q7_bins))
print(f"  最高两箱差 = {plateau}  (GPU 参照: 0.361/0.361 → 差 0 = 平台)")
print(f"  cor(in_cov, realized) = {q7_cor}  (GPU 参照: 0.563)")
print(f"  三域 realized 轴: GPU 平台 ~400 / Q6 ≤379 仍升 / Q7 见上")

out = {
    "n_runs": len(recs),
    "runs": recs,
    "in_cov_monotonic_in_realized": mono,
    "in_cov_by_realized": mono_seq,
    "realized_axis": {
        "q7_bins_by_realized": q7_bins,
        "top2_bin_gap": plateau,
        "cor_in_cov_realized": q7_cor,
        "three_domain_reference": "GPU 平台 ~400 realized 节点 (30 树分箱 0.250/0.325/0.361/0.361, cor=0.563); "
                                  "Q6 ≤379 realized 仍升 (tier 0.058→0.167); Q7 见 q7_bins_by_realized",
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
