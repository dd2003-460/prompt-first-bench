#!/usr/bin/env python3
"""Q9 逐级机械 judge v1: leaf = 概念×实例化×溯源, 沿维度卷起, 与 LLM-judge 逐门对账。
输入: q9-*-r*.json (10 run) + llm-judge-coverage-20261127.json。
输出: hierarchical-judge-v1-20261127.json + stdout 三表 (a)(b)(c)。
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from q9_gold_signatures import SIG, DIM, TRACE

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "q9-budget-scan")
DATA = os.path.normpath(DATA)
RUN_RE = re.compile(r"^q9-(\d+)-r(\d+)-\d{8}-\d{6}\.json$")
JUDGE_GATES = ["J1", "J2", "J3", "J4", "J5", "J9", "J10", "J11", "J12", "J13", "J14"]

def score_run(text):
    lines = text.split("\n")
    per_j = {}
    for jid, cre, ire in SIG:
        c = re.compile(cre); i = re.compile(ire)
        concept = any(c.search(l) for l in lines)
        inst = any(c.search(l) and i.search(l) for l in lines)
        trace = any(c.search(l) and TRACE.search(l) for l in lines)
        leaf = 1 if (concept and inst and trace) else 0
        per_j[jid] = {"concept": int(concept), "inst": int(inst),
                      "trace": int(trace), "leaf_score": leaf}
    dim = {d: round(sum(per_j[j]["leaf_score"] for j in js) / len(js), 4)
           for d, js in DIM.items()}
    total = sum(v["leaf_score"] for v in per_j.values())
    return per_j, dim, total

def main():
    runs = sorted(f for f in os.listdir(DATA) if RUN_RE.match(f))
    assert len(runs) == 10, f"expect 10 runs, got {len(runs)}: {runs}"
    judge = json.load(open(os.path.join(DATA, "llm-judge-coverage-20261127.json")))["detail"]
    per_run = []
    for f in runs:
        m = RUN_RE.match(f)
        budget, rep = m.group(1), m.group(2)
        nodes = json.load(open(os.path.join(DATA, f)))["nodes"]
        text = "\n".join(n.get("claim", "") for n in nodes)
        per_j, dim, total = score_run(text)
        per_run.append({"file": f, "budget": budget, "rep": rep,
                        "per_j": per_j, "dim_score": dim, "total": total})
    # (a)+(b) 逐门对比
    gate_cmp = {}
    for jid in JUDGE_GATES:
        jh = mh = leak = 0
        for r in per_run:
            jd = judge[r["budget"]][f"r{r['rep']}"]["gate_hit"].get(jid, False)
            ml = r["per_j"][jid]["leaf_score"]
            jh += int(bool(jd)); mh += ml
            if bool(jd) and not ml:
                leak += 1
        gate_cmp[jid] = {"judge_hits": jh, "mech_hits": mh, "leak_cells": leak}
    # (c) 预算轴
    budget_axis = []
    for b in ["50", "100", "150", "300"]:
        rs = [r for r in per_run if r["budget"] == b]
        mech = round(sum(r["total"] for r in rs) / len(rs), 3)
        jh = [judge[b][f"r{r['rep']}"]["n_gates_hit"] for r in rs]
        budget_axis.append({"budget": b, "mech_total_mean": mech,
                            "judge_hits_mean": round(sum(jh) / len(jh), 3)})
    out = {"per_run": per_run, "gate_comparison": gate_cmp, "budget_axis": budget_axis}
    out_path = os.path.join(DATA, "hierarchical-judge-v1-20261127.json")
    json.dump(out, open(out_path, "w"), ensure_ascii=False, indent=1)

    print("(a) 逐门: judge hit run 数 vs 机械 grounded run 数 (10 run)")
    print(f"{'Jid':<5}{'judge_hits':>12}{'mech_hits':>12}{'leak':>8}")
    for jid in JUDGE_GATES:
        g = gate_cmp[jid]
        print(f"{jid:<5}{g['judge_hits']:>12}{g['mech_hits']:>12}{g['leak_cells']:>8}")
    n3 = [j for j in JUDGE_GATES if j in DIM["N-3_reliability"]]
    leak_n3 = sum(gate_cmp[j]["leak_cells"] for j in n3)
    print(f"\n(b) N-3_reliability ({'/'.join(n3)}) judge hit 但机械 0 的格子数 = {leak_n3}")
    print("\n(c) 预算轴: 机械 total 均值 (0-21) vs judge n_gates_hit 均值 (0-11)")
    print(f"{'budget':<8}{'mech_total_mean':>16}{'judge_hits_mean':>16}")
    for row in budget_axis:
        print(f"{row['budget']:<8}{row['mech_total_mean']:>16}{row['judge_hits_mean']:>16}")
    print(f"\nwrote {out_path}; per_run={len(per_run)}")

if __name__ == "__main__":
    main()
