#!/usr/bin/env python3
"""Q9E-Scan 分析: per-gate 命中矩阵 + 主/次端点 + 阈值诊断.
只读 run json + gold-q9-units.json, 不调 SM、不重跑、不写 run json.
输出 data/q9-budget-scan/analysis.json (schema 见 q9e-analyze-taskcard.md)."""
import glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from judge_v1 import load_run_nodes, layer_coverage, judge_run

SCAN_DIR = os.path.join(HERE, "data", "q9-budget-scan")
GOLD = os.path.join(HERE, "data", "gold-q9-units.json")
OUT = os.path.join(SCAN_DIR, "analysis.json")
BUDGETS = [50, 100, 150, 300, 719]


def load_model():
    """bge-m3 加载一次; 失败直接退出(分析脚本没数据就没意义, 不 fail-open)."""
    try:
        from sentence_transformers import SentenceTransformer
        return SentenceTransformer("BAAI/bge-m3")
    except Exception as e:
        print(f"[analyze_q9e_scan] FATAL: bge-m3 加载失败: {e}", file=sys.stderr)
        sys.exit(1)


def parse_runs():
    """glob q9-*.json, 按文件名解析 (budget, rep, path). 返回 list."""
    out = []
    for p in sorted(glob.glob(os.path.join(SCAN_DIR, "q9-*.json"))):
        m = re.match(r"q9-(\d+)-r(\d+)-", os.path.basename(p))
        if m:
            out.append((int(m.group(1)), int(m.group(2)), p))
    return out


def score_runs(runs, model, units):
    """对每个 run: layer_coverage 拿 confirmed_ids/sim_median + judge_run 拿 total_score.
    返回 {(budget, rep): {confirmed:set, sim_median:float, total:float}}."""
    per_run = {}
    for b, r, p in runs:
        nodes = load_run_nodes(p)
        _, c_detail = layer_coverage(nodes, units, model)
        jr = judge_run(p, model=model, gold_units=units)
        per_run[(b, r)] = {"confirmed": set(c_detail["confirmed_ids"]),
                           "sim_median": c_detail["sim_median"],
                           "total": jr["total_score"]}
        print(f"  scored q9-{b}-r{r}: n_confirmed={c_detail['n_confirmed']}"
              f"/{c_detail['n_gold']} total={jr['total_score']:.4f}")
    return per_run


def build_result(per_run, gate_ids):
    """矩阵 + 主/次端点 + 阈值诊断. gate 命中率 = 该 budget 下 reps 中命中该 gate 的比例."""
    n_gates = len(gate_ids)
    gate_matrix = {g: {} for g in gate_ids}
    gate_hit_rate = {}
    n_per_budget = {}
    for b in BUDGETS:
        reps = [(b, r) for (bb, r) in per_run if bb == b]
        n_per_budget[b] = len(reps)
        if not reps:
            for g in gate_ids:
                gate_matrix[g][b] = None
            gate_hit_rate[b] = None
            continue
        for g in gate_ids:
            hit = sum(1 for kr in reps if g in per_run[kr]["confirmed"])
            gate_matrix[g][b] = round(hit / len(reps), 4)
        frac = sum(1 for g in gate_ids if gate_matrix[g][b] == 1.0) / n_gates
        gate_hit_rate[b] = round(frac, 4)
    # 主端点: gate 命中率(11 gate 全命中)首次 = 1.0 的最小 budget
    first = next((b for b in BUDGETS if gate_hit_rate.get(b) == 1.0), None)
    main_ep = {"first_100pct_budget": first,
               "note": (f"budget={first} 处 11/11 gate 全命中(跨 rep 平均)" if first is not None
                        else "未达 100%: 所有 budget 档 gate 命中率 < 1.0")}
    # 次端点: gate 全过 run 子集内 judge_total 随 budget + N-2/N-4(cost/time) 命中情况
    secondary = {}
    for b in BUDGETS:
        reps = [(b, r) for (bb, r) in per_run if bb == b]
        full = [kr for kr in reps if all(g in per_run[kr]["confirmed"] for g in gate_ids)]
        ct = {u: (round(sum(1 for kr in full if u in per_run[kr]["confirmed"]) / len(full), 4)
                  if full else None) for u in ("N-2", "N-4")}
        secondary[b] = {"n_gate_full_runs": len(full),
                        "judge_totals": [per_run[kr]["total"] for kr in full],
                        "cost_time_hits": ct}
    # 阈值诊断: sim_median 汇总 + 极端判定
    sim_medians = {b: [per_run[kr]["sim_median"] for kr in
                       [(b, r) for (bb, r) in per_run if bb == b]] for b in BUDGETS}
    rates = [v for v in gate_hit_rate.values() if v is not None]
    if rates and (all(v < 0.1 for v in rates) or all(v > 0.9 for v in rates)):
        verdict = ("gate 命中率全档≈0(<0.1)或≈1(>0.9): 建议按 Q9 域 sim 分布重标定 "
                   "COS_THRESHOLD=0.70 (gpu 域标定, Q9 域未重校; 只重算 embedding 不重跑 SM)")
    else:
        verdict = "gate 命中率有跨档区分度, 暂不需重标定 COS_THRESHOLD"
    return {"budgets": BUDGETS,
            "gate_matrix": gate_matrix,
            "gate_hit_rate_by_budget": gate_hit_rate,
            "main_endpoint": main_ep,
            "secondary_endpoint": secondary,
            "threshold_diag": {"sim_medians": sim_medians, "verdict": verdict},
            "n_runs_per_budget": n_per_budget}


def main():
    gold = json.load(open(GOLD))
    units, gate_ids = gold["units"], gold["gate_units"]
    assert len(gate_ids) == 11, f"expect 11 gates, got {len(gate_ids)}"
    runs = parse_runs()
    if not runs:
        print("[analyze_q9e_scan] FATAL: 无 q9-*.json run", file=sys.stderr)
        sys.exit(1)
    print(f"[analyze_q9e_scan] {len(runs)} runs, 加载 bge-m3 ...")
    model = load_model()
    per_run = score_runs(runs, model, units)
    result = build_result(per_run, gate_ids)
    json.dump(result, open(OUT, "w"), ensure_ascii=False, indent=1)
    print(f"[analyze_q9e_scan] → {OUT}")
    rates = result["gate_hit_rate_by_budget"]
    print(f"[summary] 主端点 first_100pct_budget="
          f"{result['main_endpoint']['first_100pct_budget']} | "
          + " ".join(f"b{b}:{rates[b]}" for b in BUDGETS))


if __name__ == "__main__":
    main()
