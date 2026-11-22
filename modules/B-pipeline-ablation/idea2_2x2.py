#!/usr/bin/env python3
"""idea2 2x2 分析: A/B 臂 × r1/r2, judge total/depth/cov + metacog + L2。
用法: python3 idea2_2x2.py [--score]
  --score: 若 B-r2 树存在且未评分, 先跑 judge_v1 + metacog + L2 评分 append 到 idea2-scores.json
"""
import sys, os, glob, json, statistics
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
DATA = os.path.join(HERE, "data", "idea2")
SCORES = os.path.join(DATA, "idea2-scores.json")


def score_tree(f, arm, rep):
    from judge_v1 import judge_run
    from metacog_axis import compute_metacog, load_run_nodes
    from tjudge1_formula import l2_check
    rj = judge_run(f)
    rm = compute_metacog(load_run_nodes(f))
    l2, l2det = l2_check(f)
    n_ok = sum(1 for d in l2det["detail"] if d["ok"])
    n_over = sum(1 for d in l2det["detail"] if d["gold_expand"] is False and d["model_expanded"] is True)
    n_under = sum(1 for d in l2det["detail"] if d["gold_expand"] is True and d["model_expanded"] is False)
    return {
        "arm": arm, "rep": rep,
        "n_nodes": rj["n_nodes_raw"],
        "judge": {"total": rj["total_score"],
                  "depth": rj["layers"]["structure"]["depth_score"],
                  "cov": rj["layers"]["coverage"]["coverage"]},
        "metacog": {"total": round(rm["metacog_total"], 4), "gap": round(rm["gap_rate"], 4),
                    "ret": round(rm["retrieval_rate"], 4)},
        "l2": {"score": l2, "matched": l2det["n_matched_units"], "ok": n_ok,
               "over": n_over, "under": n_under},
        "src": os.path.basename(f),
    }


def main():
    if "--score" in sys.argv:
        scores = json.load(open(SCORES)) if os.path.exists(SCORES) else []
        have = {(s["arm"], s["rep"]) for s in scores}
        for arm, rep in [(a, r) for a in "AB" for r in (1, 2, 3)]:
            if (arm, rep) in have:
                continue
            m = sorted(glob.glob(os.path.join(DATA, f"idea2-{arm}-r{rep}-*.json")))
            if not m:
                print(f"[skip] {arm}-r{rep} 树不存在")
                continue
            rec = score_tree(m[-1], arm, rep)
            scores.append(rec)
            json.dump(scores, open(SCORES, "w"), ensure_ascii=False, indent=1)
            print(f"[score] {arm}-r{rep}: total={rec['judge']['total']:.4f} "
                  f"depth={rec['judge']['depth']:.3f} cov={rec['judge']['cov']:.3f} "
                  f"metacog={rec['metacog']['total']:.4f} l2={rec['l2']['score']:.4f} "
                  f"over={rec['l2']['over']} under={rec['l2']['under']}")
    scores = json.load(open(SCORES))
    by = {(s["arm"], s["rep"]): s for s in scores}
    reps = sorted({r for (_, r) in by})
    cells = [(a, r) for a in "AB" for r in reps if (a, r) in by]
    if len(cells) < 2:
        print(f"只有 {len(cells)}/2 格: {cells} — 等")
        return
    print(f"\n{'':6s} {'total':>7s} {'depth':>6s} {'cov':>7s} {'metacog':>8s} {'l2':>7s} {'over':>4s} {'under':>5s} {'n_nodes':>7s}")
    for a in "AB":
        for r in reps:
            if (a, r) not in by:
                continue
            s = by[(a, r)]
            print(f"{a}-r{r}  {s['judge']['total']:>7.4f} {s['judge']['depth']:>6.3f} "
                  f"{s['judge']['cov']:>7.4f} {s['metacog']['total']:>8.4f} "
                  f"{s['l2']['score']:>7.4f} {s['l2']['over']:>4d} {s['l2']['under']:>5d} {s['n_nodes']:>7d}")
    # 臂差 (A-B) 按 rep 配对
    diffs = []
    for r in reps:
        if ("A", r) not in by or ("B", r) not in by:
            continue
        a, b = by[("A", r)], by[("B", r)]
        d = a['judge']['total'] - b['judge']['total']
        diffs.append(d)
        print(f"\nrep{r} 臂差 A-B: total={d:+.4f} "
              f"depth={a['judge']['depth']-b['judge']['depth']:+.3f} "
              f"cov={a['judge']['cov']-b['judge']['cov']:+.4f} "
              f"metacog={a['metacog']['total']-b['metacog']['total']:+.4f} "
              f"l2={a['l2']['score']-b['l2']['score']:+.4f} "
              f"n_nodes={a['n_nodes']-b['n_nodes']:+d}")
    # 一致性: 各 rep 臂差方向
    signs = {1 if d > 0 else -1 for d in diffs}
    print(f"\n臂差方向一致性: " + " ".join(f"rep{r}={d:+.4f}" for r, d in zip(reps, diffs))
          + f" → {'同向(A>B)' if len(signs) == 1 and diffs[0] > 0 else '同向(B>A)' if len(signs) == 1 else '反向(不稳定)'}")


if __name__ == "__main__":
    main()
