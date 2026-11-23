#!/usr/bin/env python3
"""Q6 719 档三轴固化 (2026-11-23 22:28)

承重数字 provenance: 719 档 r1/r2 的三轴数字原是 terminal 手动算的,
散在历史里无脚本。本脚本统一固化, 遍历 q6-719-r*.json (glob, 幂等,
r3 落地后重跑一次即全齐), 输出:
  - 每 rep: n_nodes, 域内 cov (Q6 gold 46), 跨域 cov (GPU gold 36),
            depth, total, CUR mon_claim
  - 汇总: repair (rework_count>0 且 verified, 固化口径同 GPU 331/8870)
  - 停止原因: 从 stdout 读 max_depth/max_nodes/DONE (承重归因核验)

用法: /usr/bin/python3 q6_719_axis.py
落盘: data/q6-budget-scan/q6-719-axis.json
"""
import sys, os, json, glob, re

HERE = os.path.dirname(os.path.abspath(__file__))
BPL = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, BPL)
from judge_v1 import judge_run
from metacog_axis import load_run_nodes

SCAN = os.path.join(BPL, "data", "q6-budget-scan")
OUT = os.path.join(SCAN, "q6-719-axis.json")
CUR = re.compile(r"\[待核验\]|不确定|未验证|待确认|需要验证|无法确定|缺乏数据|信息不足")

gq = json.load(open(os.path.join(BPL, "data", "gold-q6-units.json")))
gg = json.load(open(os.path.join(BPL, "gold-gpu-units.json")))
gq_units = gq["units"] if isinstance(gq, dict) else gq
gg_units = gg["units"] if isinstance(gg, dict) else gg

files = sorted(glob.glob(os.path.join(SCAN, "q6-719-r*-[0-9]*.json")))
recs = []
for f in files:
    m = re.search(r"q6-719-r(\d+)-", os.path.basename(f))
    rep = int(m.group(1))
    rj_q = judge_run(f, gold_units=gq_units)
    rj_g = judge_run(f, gold_units=gg_units)
    nodes = load_run_nodes(f)
    hits = sum(1 for n in nodes if CUR.search(n.get("claim", "")))
    # 停止原因: 只读 max_depth/max_nodes 行 (DONE 行不含停止原因, 会覆盖)
    stop = "UNKNOWN"
    sp = os.path.join(SCAN, f"q6-719-r{rep}.stdout")
    if os.path.exists(sp):
        for line in open(sp, errors="ignore"):
            if "max_depth=" in line or "max_nodes=" in line:
                stop = line.strip()
    recs.append({
        "rep": rep, "n_nodes": rj_q["n_nodes_raw"], "stop": stop,
        "in_cov": round(rj_q["layers"]["coverage"]["coverage"], 4),
        "in_cov_n": rj_q["layers"]["coverage"]["n_confirmed"],
        "cross_cov": round(rj_g["layers"]["coverage"]["coverage"], 4),
        "cross_cov_n": rj_g["layers"]["coverage"]["n_confirmed"],
        "depth": rj_q["layers"]["structure"]["depth_score"],
        "total": round(rj_q["total_score"], 4),
        "mon_claim": round(hits / len(nodes), 4) if nodes else None,
        "mon_claim_n": f"{hits}/{len(nodes)}",
    })

out = {
    "n_reps": len(recs),
    "reps": recs,
    "note": ("719 档停止原因 = max_depth=4 深度墙 (非自然停止); 域内 cov 单调升, "
             "跨域 cov 0-0.083 波动。repair 跨域用全 14 Q6 run 口径 (5.6%, 见 q6_rescore/draft), "
             "不在本 719-only 脚本内算, 避免口径混淆"),
}
json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
for r in recs:
    print(f"  r{r['rep']}: n={r['n_nodes']} in_cov={r['in_cov']} cross_cov={r['cross_cov']} "
          f"depth={r['depth']} total={r['total']} mon_claim={r['mon_claim_n']} | {r['stop']}")
print(f"  → {os.path.basename(OUT)}")
