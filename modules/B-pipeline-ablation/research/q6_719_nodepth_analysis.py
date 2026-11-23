#!/usr/bin/env python3
"""Q6 719 无深度墙批分析 (2026-11-23 23:36)

D 指令"不要限制深度"落地批: --max-nodes 719 --max-depth 10 (实质无深度墙)。
draft 缺的"预算超饱和点"干净测试 — 预算成为唯一约束。

承重核验 (停止原因规则):
  本批停止原因必须是 max_nodes=719 hit 或 DONE (自然完成), 不能是 max_depth hit。
  若出现 max_depth=10 hit → 模型真需要 >10 层深度, 需再提上限 (预期不会, gold 主干 5 层)。

输出 (stdout + data/q6-719-nodepth/q6-719-nodepth-analysis.json):
  每 rep: n_nodes (realized), 停止原因, 域内 cov (Q6 gold 46), 跨域 cov (GPU gold 36),
          depth 组件, total, CUR mon_claim
  对照: 原批 719 档 (max_depth=4, realized 197/351/379) vs 本批 (max_depth=10)
        — 分离"深度墙效应" vs "预算效应"

用法: /usr/bin/python3 q6_719_nodepth_analysis.py (幂等, 3 rep 落地后跑)
"""
import sys, os, json, glob, re

HERE = os.path.dirname(os.path.abspath(__file__))
BPL = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, BPL)
from judge_v1 import judge_run
from metacog_axis import load_run_nodes

NODEPTH = os.path.join(BPL, "data", "q6-719-nodepth")
ORIG = os.path.join(BPL, "data", "q6-budget-scan")
OUT = os.path.join(NODEPTH, "q6-719-nodepth-analysis.json")
CUR = re.compile(r"\[待核验\]|不确定|未验证|待确认|需要验证|无法确定|缺乏数据|信息不足")

gq = json.load(open(os.path.join(BPL, "data", "gold-q6-units.json")))
gg = json.load(open(os.path.join(BPL, "gold-gpu-units.json")))
gq_units = gq["units"] if isinstance(gq, dict) else gq
gg_units = gg["units"] if isinstance(gg, dict) else gg

files = sorted(glob.glob(os.path.join(NODEPTH, "q6-719-nd-r*-[0-9]*.json")))
if not files:
    print(f"no nodepth run files in {NODEPTH} — batch not landed yet")
    sys.exit(0)

recs = []
for f in files:
    m = re.search(r"q6-719-nd-r(\d+)-", os.path.basename(f))
    rep = int(m.group(1))
    rj_q = judge_run(f, gold_units=gq_units)
    rj_g = judge_run(f, gold_units=gg_units)
    nodes = load_run_nodes(f)
    hits = sum(1 for n in nodes if CUR.search(n.get("claim", "")))
    stop = "UNKNOWN"
    sp = os.path.join(NODEPTH, f"q6-719-nd-r{rep}.stdout")
    if os.path.exists(sp):
        for line in open(sp, errors="ignore"):
            if "max_depth=" in line or "max_nodes=" in line or "DONE" in line:
                stop = line.strip()
    recs.append({
        "rep": rep, "n_nodes": rj_q["n_nodes_raw"], "stop": stop,
        "in_cov": round(rj_q["layers"]["coverage"]["coverage"], 4),
        "in_cov_n": f"{rj_q['layers']['coverage']['n_confirmed']}/46",
        "cross_cov": round(rj_g["layers"]["coverage"]["coverage"], 4),
        "depth": rj_q["layers"]["structure"]["depth_score"],
        "total": round(rj_q["total_score"], 4),
        "mon_claim": round(hits / len(nodes), 4) if nodes else None,
        "mon_claim_n": f"{hits}/{len(nodes)}",
    })

# 承重核验: 停止原因
depth_hits = [r for r in recs if "max_depth=" in r["stop"]]
budget_hits = [r for r in recs if "max_nodes=" in r["stop"]]
done = [r for r in recs if "DONE" in r["stop"]]

# 对照: 原批 719 档
orig = []
of = json.load(open(os.path.join(ORIG, "q6-719-axis.json")))
for r in of["reps"]:
    orig.append({"rep": r["rep"], "n_nodes": r["n_nodes"], "in_cov": r["in_cov"],
                 "stop": r["stop"]})

out = {
    "n_reps": len(recs),
    "reps": recs,
    "stop_check": {"depth_hits": len(depth_hits), "budget_hits": len(budget_hits),
                   "done": len(done),
                   "verdict": ("PASS — 无深度墙" if not depth_hits else
                               "FAIL — 出现 max_depth=10 hit, 模型需更深, 需提上限")},
    "orig_719_depth4": orig,
    "note": ("D 指令'不要限制深度'落地批。对照: 原批 719 (max_depth=4, realized 197/351/379, "
             "深度墙) vs 本批 (max_depth=10, 预算唯一约束)。分离深度墙效应 vs 预算效应。"
             "预期: 本批 realized 接近 719 (或 DONE 自然停止), 域内 cov > 原批 719 档 (0.130-0.196)"),
}
json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
for r in recs:
    print(f"  nd-r{r['rep']}: n={r['n_nodes']} in_cov={r['in_cov']}({r['in_cov_n']}) "
          f"cross={r['cross_cov']} depth={r['depth']} total={r['total']} mon={r['mon_claim_n']} | {r['stop'][-45:]}")
print(f"  停止原因核验: depth_hits={len(depth_hits)} budget_hits={len(budget_hits)} done={len(done)} → {out['stop_check']['verdict']}")
print(f"  对照原批 719 (max_depth=4): {[(r['rep'], r['n_nodes'], r['in_cov']) for r in orig]}")
print(f"  → {os.path.basename(OUT)}")
