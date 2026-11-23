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

out = {
    "n_runs": len(recs),
    "runs": recs,
    "in_cov_monotonic_in_realized": mono,
    "in_cov_by_realized": mono_seq,
    "repair": {"fixed": tot_fix, "rework": tot_rw,
               "rate": round(tot_fix / tot_rw, 4) if tot_rw else None},
    "note": ("第三域验证 (GPU+Q6+Q7)。域内 cov 用 Q7 gold 52 units; 跨域用 GPU gold 36; "
             "mon_claim = CUR 官方 8-pattern; repair 固化口径同 GPU 331/8870。"
             "719 档预期撞 max_depth=4 (深度墙, Q6 同现象) — 停止原因逐 run 核验, 不从'提前停'推断"),
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
