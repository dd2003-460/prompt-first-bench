#!/usr/bin/env python3
"""Q9 逐级机械 judge v1: leaf = 概念×实例化 (D 原话两因子), 溯源为独立诊断字段。
沿维度卷起, 与 LLM-judge 逐门对账。
输入: q9-*-r*.json (10 run) + llm-judge-coverage-20261127.json。
输出: hierarchical-judge-v1-20261127.json + stdout 三表 (a)(b)(c)。

设计注 (v1.1 修正): 初版 leaf=概念×实例化×溯源 三重积, 实测塌成 1/210 —
溯源同行要求过严, 把 22/210 的双重积信号清零 (ablation 证实: 去 TRACE 回升)。
按奥卡姆砍实体: 溯源不乘进主分 (D 原话就是"概念-公式"两因子), 降为独立
trace 字段 + grounded=leaf×trace 次级计数, 供诊断"实例化是否有来源支撑"。
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
        leaf = 1 if (concept and inst) else 0
        grounded = 1 if (leaf and trace) else 0
        per_j[jid] = {"concept": int(concept), "inst": int(inst),
                      "trace": int(trace), "leaf_score": leaf, "grounded": grounded}
    dim = {d: round(sum(per_j[j]["leaf_score"] for j in js) / len(js), 4)
           for d, js in DIM.items()}
    total = sum(v["leaf_score"] for v in per_j.values())
    grounded_total = sum(v["grounded"] for v in per_j.values())
    return per_j, dim, total, grounded_total

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
        per_j, dim, total, grounded_total = score_run(text)
        per_run.append({"file": f, "budget": budget, "rep": rep,
                        "per_j": per_j, "dim_score": dim, "total": total,
                        "grounded_total": grounded_total})
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
    for b in ["50", "100", "150", "300", "719"]:
        rs = [r for r in per_run if r["budget"] == b]
        if not rs:
            budget_axis.append({"budget": b, "mech_total_mean": None,
                                "grounded_mean": None, "judge_hits_mean": None, "n_runs": 0})
            continue
        mech = round(sum(r["total"] for r in rs) / len(rs), 3)
        gr = round(sum(r["grounded_total"] for r in rs) / len(rs), 3)
        jh = [judge.get(b, {}).get(f"r{r['rep']}", {}).get("n_gates_hit") for r in rs]
        jh = [x for x in jh if x is not None]
        budget_axis.append({"budget": b, "mech_total_mean": mech,
                            "grounded_mean": gr,
                            "judge_hits_mean": round(sum(jh) / len(jh), 3) if jh else None,
                            "n_runs": len(rs)})
    out = {"per_run": per_run, "gate_comparison": gate_cmp, "budget_axis": budget_axis}
    out_path = os.path.join(DATA, "hierarchical-judge-v1-20261127.json")

    print("(a) 逐门: judge hit run 数 vs 机械 grounded run 数 (10 run)")
    print(f"{'Jid':<5}{'judge_hits':>12}{'mech_hits':>12}{'leak':>8}")
    for jid in JUDGE_GATES:
        g = gate_cmp[jid]
        print(f"{jid:<5}{g['judge_hits']:>12}{g['mech_hits']:>12}{g['leak_cells']:>8}")
    n3 = [j for j in JUDGE_GATES if j in DIM["N-3_reliability"]]
    leak_n3 = sum(gate_cmp[j]["leak_cells"] for j in n3)
    print(f"\n(b) N-3_reliability ({'/'.join(n3)}) judge hit 但机械 0 的格子数 = {leak_n3}")
    print("\n(c) 预算轴: 机械 total 均值 (0-21) / grounded 均值 / judge n_gates_hit 均值 (0-11)")
    print(f"{'budget':<8}{'mech_total':>14}{'grounded':>12}{'judge_hits':>14}")
    for row in budget_axis:
        def _f(v):
            return f"{v:>14}" if v is not None else f"{'n/a':>14}"
        print(f"{row['budget']:<8}{_f(row['mech_total_mean'])}{_f(row['grounded_mean'])}{_f(row['judge_hits_mean'])}")

    # (d) reliability 维 2x2 拆分: 硬放水(未提及却 hit) vs 软放水(提未实例化却 hit)
    probe = json.load(open(os.path.join(DATA, "formula-instantiation-probe-20261127.json")))
    pmap = {r["file"]: r for r in probe["per_run"]}
    cell = {}
    for r in per_run:
        jb = judge.get(r["budget"])
        if jb is None or f"r{r['rep']}" not in jb:
            continue  # LLM-judge 未覆盖该档 (如 719)
        gh = jb[f"r{r['rep']}"]["gate_hit"]
        pj = pmap.get(r["file"])
        if pj is None:
            continue  # 探针未覆盖该 run (新补跑档)
        pj = pj["per_j"]
        for j in DIM["N-3_reliability"]:
            ms = ("提+实例化" if (pj[j]["mention"] and pj[j]["instantiated"])
                  else ("提未实例化" if pj[j]["mention"] else "未提及"))
            hit = bool(gh.get(j, False))
            cell[(ms, hit)] = cell.get((ms, hit), 0) + 1
    print("\n(d) reliability 维 (J9-J14) 60 格 2x2 拆分:")
    print(f"{'模型侧':<12}{'judge hit':>10}{'judge miss':>12}")
    for ms in ["提+实例化", "提未实例化", "未提及"]:
        print(f"{ms:<12}{cell.get((ms, True), 0):>10}{cell.get((ms, False), 0):>12}")
    hard = cell.get(("未提及", True), 0); soft = cell.get(("提未实例化", True), 0)
    print(f"  硬放水(未提及却hit)={hard}  软放水(提未实例化却hit)={soft}")
    out["reliability_2x2"] = {f"{k[0]}|hit={k[1]}": v for k, v in cell.items()}
    json.dump(out, open(out_path, "w"), ensure_ascii=False, indent=1)

    print(f"\nwrote {out_path}; per_run={len(per_run)}")

if __name__ == "__main__":
    main()
