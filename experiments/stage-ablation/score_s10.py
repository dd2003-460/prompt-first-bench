#!/usr/bin/env python3
"""score_s10.py: Score S10 composite-arm runs (A-E) × Q1/Q3/Q4 with M1-M6.

Adapts score.py's scoring logic for S10 run format:
- output text is in 'final' field (not 'output_text')
- arms are S10-A through S10-E
- questions are Q1, Q3, Q4 (subset of the full set)

Usage:
  python3 score_s10.py              # score all 90 runs
  python3 score_s10.py --limit 10   # only first 10 (for testing)
"""
import json, os, re, sys, time, statistics, argparse
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from score import judge_m1, judge_m4, check_urls, detect_gold_type
from gates import analyze as gate_analyze

LLM_CONF_CAP = 0.7
S10_RUNS_DIR = os.path.join(HERE, "s10-runs")
OUT_PATH = os.path.join(S10_RUNS_DIR, "s10-scores.json")

# Gold files (same as ablation harness)
GOLD_FILES = {
    "Q1": os.path.join(HERE, "gold", "Q1.md"),
    "Q3": os.path.join(HERE, "gold", "Q3.md"),
    "Q4": os.path.join(HERE, "gold", "Q4.md"),
}

def score_s10_run(path, gold_md):
    """Score a single S10 run. Returns dict or None on error."""
    with open(path) as f:
        run = json.load(f)
    arm = run.get("arm", "?")
    qid = run.get("qid", "?")
    rep = run.get("rep", 0)
    output = run.get("final", "")
    sources = run.get("sources", [])

    if not output:
        return None

    notes = []

    # M2/M3/M5 from gates.py
    ga = gate_analyze(output, sources=sources if sources else None)
    has_structure = bool(re.search(r'\|.*\|', output)) or bool(re.search(r'^\s*[-*]\s+\S', output, re.M)) or output.count('#') >= 3
    m2_norm = ((ga.get("limit_first_third_rate") or 0) * 0.5 + (1.0 if has_structure else 0.0) * 0.5)
    m3_raw = ga.get("hedge_count", 0)
    m3_norm = min(m3_raw / 3.0, 1.0)
    m5_norm = ga.get("anchored_rate_weighted") or 0.0

    # M1 fact accuracy (judge)
    try:
        m1_matched, m1_total, m1_note = judge_m1(output[:12000], gold_md)
        m1_norm = m1_matched / max(m1_total, 1)
        notes.append(f"M1: {m1_note}")
    except Exception as e:
        m1_norm = 0.0
        notes.append(f"M1 error: {str(e)[:100]}")

    # M4 gap coverage (judge)
    try:
        m4_id, m4_total, m4_note = judge_m4(output[:12000], gold_md)
        m4_norm = m4_id / max(m4_total, 1)
        notes.append(f"M4: {m4_note}")
    except Exception as e:
        m4_norm = 0.0
        notes.append(f"M4 error: {str(e)[:100]}")

    # M6 URL alive
    m6_alive, m6_checked, m6_note = check_urls(sources)
    m6_norm = m6_alive / max(m6_checked, 1) if m6_checked > 0 else 0.0
    notes.append(f"M6: {m6_note}")

    total = (m1_norm + m2_norm + m3_norm + m4_norm + m5_norm + m6_norm) / 6.0

    return {
        "tag": f"{arm}-{qid}-r{rep}",
        "arm": arm, "qid": qid, "rep": rep,
        "M1": round(m1_norm, 4), "M2": round(m2_norm, 4),
        "M3": round(m3_norm, 4), "M4": round(m4_norm, 4),
        "M5": round(m5_norm, 4), "M6": round(m6_norm, 4),
        "total": round(total, 4),
        "notes": "; ".join(notes)[:500],
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="Max runs to score (0=all)")
    ap.add_argument("--resume", action="store_true", help="Skip already-scored tags")
    args = ap.parse_args()

    # Load existing scores for resume
    done_tags = set()
    results = []
    if args.resume and os.path.exists(OUT_PATH):
        try:
            results = json.load(open(OUT_PATH))
            done_tags = {r["tag"] for r in results if r.get("total") is not None}
            print(f"Resuming: {len(done_tags)} already scored")
        except (json.JSONDecodeError, KeyError):
            pass

    # Collect tasks
    tasks = []
    for fn in sorted(os.listdir(S10_RUNS_DIR)):
        if not fn.endswith(".json") or fn == "s10-scores.json":
            continue
        path = os.path.join(S10_RUNS_DIR, fn)
        d = json.load(open(path))
        tag = f"{d.get('arm','?')}-{d.get('qid','?')}-r{d.get('rep',0)}"
        if tag in done_tags:
            continue
        qid = d.get("qid", "?")
        gold_path = GOLD_FILES.get(qid)
        if not gold_path or not os.path.exists(gold_path):
            print(f"[skip] {fn}: no gold for {qid}")
            continue
        tasks.append((fn, path, open(gold_path).read()))

    if args.limit:
        tasks = tasks[:args.limit]

    print(f"Scoring {len(tasks)} runs (4 workers)...")
    t0 = time.time()

    def _one(task):
        fn, path, gold_md = task
        try:
            return score_s10_run(path, gold_md)
        except Exception as e:
            print(f"  ERROR {fn}: {str(e)[:100]}", file=sys.stderr)
            return None

    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(_one, t): t[0] for t in tasks}
        for i, fut in enumerate(as_completed(futures)):
            sc = fut.result()
            if sc:
                results.append(sc)
                print(f"  [{i+1}/{len(tasks)}] {sc['tag']} total={sc['total']:.3f}", flush=True)
            # Incremental save every 5
            if (i + 1) % 5 == 0:
                with open(OUT_PATH, "w") as f:
                    json.dump(results, f, ensure_ascii=False, indent=2)

    elapsed = time.time() - t0
    with open(OUT_PATH, "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    # Aggregate by arm
    print(f"\nDone in {elapsed:.0f}s. {len(results)} scored → {OUT_PATH}\n")
    arms = sorted(set(r["arm"] for r in results))
    dims = ["M1", "M2", "M3", "M4", "M5", "M6", "total"]
    header = "| Arm | n | " + " | ".join(dims) + " |"
    sep = "|-----|---|" + "|".join(["------"] * len(dims)) + "|"
    print(header)
    print(sep)
    for arm in arms:
        arm_scores = [r for r in results if r["arm"] == arm]
        n = len(arm_scores)
        means = [statistics.mean(r[d] for r in arm_scores) for d in dims]
        row = f"| {arm} | {n} | " + " | ".join(f"{m:.3f}" for m in means) + " |"
        print(row)


if __name__ == "__main__":
    main()