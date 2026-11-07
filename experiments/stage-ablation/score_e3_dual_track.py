#!/usr/bin/env python3
"""E3: Dual-track scoring — final-only vs process (all rounds concatenated).

Question: In the S5-vs-S0 +0.235 gap, how much is "truly fewer hallucinations"
(final answer more accurate) vs "interception" (errors caught during process)?

Method:
  - final track: M1 on `final` field only (current behavior)
  - process track: M1 on ALL round texts concatenated (r1+r2+...+rn)
  - Δ = process_M1 - final_M1
    Δ > 0 → model made MORE correct claims in process than survived to final
           (self-correction removed good claims, or final is more selective)
    Δ < 0 → model made FEWER correct claims in process; final added accuracy
           (correction/improvement happened between rounds)
    Δ ≈ 0 → no significant difference; accuracy is stable across rounds

Usage:
  python3 score_e3_dual_track.py [--limit N]
Output:
  s10-runs/e3-dual-track.json
"""
import argparse, json, glob, os, sys
from collections import defaultdict
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from score_s10_v2 import judge_m1, GOLD_FILES

HERE = os.path.dirname(os.path.abspath(__file__))


def get_process_text(run):
    """Concatenate all round texts."""
    rounds = run.get("rounds", {})
    if isinstance(rounds, dict):
        parts = [rounds[k].get("text", "") for k in sorted(rounds.keys())]
    elif isinstance(rounds, list):
        parts = [r.get("text", "") or r.get("output", "") for r in rounds]
    else:
        parts = []
    return "\n\n".join(p for p in parts if p)


def score_dual(path, gold_md):
    with open(path) as f:
        run = json.load(f)
    arm = run.get("arm", "?")
    qid = run.get("qid", "?")
    rep = run.get("rep", 0)

    final_text = run.get("final", "")
    process_text = get_process_text(run)

    # Final track M1
    try:
        fm, ft, _ = judge_m1(final_text[:12000], gold_md)
        final_m1 = fm / max(ft, 1) if ft > 0 else None
    except Exception:
        final_m1 = None

    # Process track M1
    try:
        pm, pt, _ = judge_m1(process_text[:24000], gold_md)  # double budget for longer text
        process_m1 = pm / max(pt, 1) if pt > 0 else None
    except Exception:
        process_m1 = None

    delta = None
    if final_m1 is not None and process_m1 is not None:
        delta = process_m1 - final_m1

    return {
        "tag": f"{arm}-{qid}-r{rep}",
        "arm": arm, "qid": qid, "rep": rep,
        "final_m1": round(final_m1, 4) if final_m1 is not None else None,
        "process_m1": round(process_m1, 4) if process_m1 is not None else None,
        "delta": round(delta, 4) if delta is not None else None,
        "final_claims": ft if final_m1 is not None else 0,
        "process_claims": pt if process_m1 is not None else 0,
        "n_rounds": len(run.get("rounds", {})) if isinstance(run.get("rounds"), (dict, list)) else 0,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    files = sorted(glob.glob(os.path.join(HERE, "s10-runs", "S10-*-*.json")))
    if args.limit:
        files = files[:args.limit]

    print(f"E3 dual-track scoring: {len(files)} runs")
    results = []
    for f in files:
        d = json.load(open(f))
        qid = d.get("qid", "?")
        gold_path = GOLD_FILES.get(qid)
        if not gold_path or not os.path.exists(gold_path):
            print(f"  SKIP {os.path.basename(f)}: no gold for {qid}")
            continue
        gold_md = open(gold_path).read()
        r = score_dual(f, gold_md)
        results.append(r)
        delta_str = f"{r['delta']:+.3f}" if r['delta'] is not None else "N/A"
        print(f"  {r['tag']:12s} final={r['final_m1']} proc={r['process_m1']} Δ={delta_str} ({r['n_rounds']}r)")

    # Per-arm aggregation
    by_arm = defaultdict(list)
    for r in results:
        by_arm[r["arm"]].append(r)

    print(f"\n{'Arm':<6} {'n':>3} {'final_M1':>9} {'proc_M1':>8} {'Δ':>8} {'Δ>0':>4} {'Δ<0':>4}")
    for arm in sorted(by_arm):
        rs = by_arm[arm]
        finals = [r["final_m1"] for r in rs if r["final_m1"] is not None]
        procs = [r["process_m1"] for r in rs if r["process_m1"] is not None]
        deltas = [r["delta"] for r in rs if r["delta"] is not None]
        fm = sum(finals) / len(finals) if finals else 0
        pm = sum(procs) / len(procs) if procs else 0
        dm = sum(deltas) / len(deltas) if deltas else 0
        pos = sum(1 for x in deltas if x > 0.02)
        neg = sum(1 for x in deltas if x < -0.02)
        print(f"{arm:<6} {len(rs):>3} {fm:>9.4f} {pm:>8.4f} {dm:>+8.4f} {pos:>4} {neg:>4}")

    out = os.path.join(HERE, "s10-runs", "e3-dual-track.json")
    with open(out, "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nWrote {out} ({len(results)} entries)")


if __name__ == "__main__":
    main()
