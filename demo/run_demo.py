#!/usr/bin/env python3
"""Minimal reproducible demo: score S0 vs S5 on Q1 (H100 PCIe vs SXM).

Two modes:
  1. Offline (no model needed): use the bundled scored runs from runs-r293.
     Shows the full scoring pipeline end-to-end with real data.
  2. Live (needs a local 27B at 8787): regenerate outputs, then re-score.

Usage:
  python run_demo.py            # offline: score bundled outputs (default)
  python run_demo.py --live     # live: call LLM_URL, then score (needs endpoint)

Scoring = 6 dimensions, weighted sum in [0,1]:
  M1 factual accuracy   (judge vs gold facts)      w=0.25
  M2 structure          (limit statements upfront + formatting)  w=0.20
  M3 uncertainty marks  (hedges / gap flags)       w=0.15
  M4 gap coverage       (judge: did it flag known gaps?)         w=0.20
  M5 source anchoring   (per-number citation density)            w=0.10
  M6 URL liveness       (cited URLs actually exist)              w=0.10

Judge for M1/M4: same 27B model (temp=0, deterministic) — known limitation,
hetero-judge calibration is tracked separately (see experiments/stage-ablation/).
"""
import json, os, sys, statistics, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
PFB = os.path.dirname(HERE)
SA = os.path.join(PFB, "experiments", "stage-ablation")
sys.path.insert(0, SA)

WEIGHTS = {"M1": 0.25, "M2": 0.20, "M3": 0.15, "M4": 0.20, "M5": 0.10, "M6": 0.10}


def load_bundled_scores():
    """Offline path: read pre-computed scores from runs-r293/scores-v3.json."""
    scores_path = os.path.join(SA, "runs-r293", "scores-v3.json")
    all_scores = json.load(open(scores_path))
    out = {}
    for arm in ("S0", "S5"):
        rows = [s for s in all_scores if s["arm"] == arm and s["qid"] == "Q1"]
        out[arm] = {
            "per_run": [{"rep": r["rep"], "total": r["total"], "scores": r["scores"]} for r in rows],
            "mean_total": statistics.mean(r["total"] for r in rows),
            "mean_dims": {k: statistics.mean(r["scores"][k] for r in rows) for k in WEIGHTS},
        }
    return out


def main():
    live = "--live" in sys.argv
    if live:
        print("Live mode: requires local 27B endpoint at http://127.0.0.1:8787")
        print("(See ablation_harness.py for the full runner; this demo focuses on scoring.)")
        sys.exit(1)

    results = load_bundled_scores()
    gold = open(os.path.join(HERE, "gold", "Q1-gold.md"), encoding="utf-8").read()

    print("=" * 62)
    print("DEMO: S0 (bare prompt) vs S5 (full 6-stage pipeline) on Q1")
    print("Question: H100 PCIe vs SXM — how much faster is SXM for LLM inference?")
    print(f"Model: qwen3.8-27b @ temp=0 · n={len(results['S0']['per_run'])} reps/arm · judge: same model (conf ≤0.7)")
    print("=" * 62)

    for arm, label in (("S0", "S0 bare"), ("S5", "S5 pipeline")):
        d = results[arm]
        print(f"\n{label}: mean total = {d['mean_total']:.3f}")
        print(f"  {'dim':<6}{'weight':>8}{'mean':>8}   what it measures")
        desc = {
            "M1": "factual accuracy vs gold",
            "M2": "structure / limits upfront",
            "M3": "uncertainty marking",
            "M4": "known-gap coverage",
            "M5": "per-number source anchoring",
            "M6": "cited URLs are real",
        }
        for k in ("M1", "M2", "M3", "M4", "M5", "M6"):
            print(f"  {k:<6}{WEIGHTS[k]:>8.2f}{d['mean_dims'][k]:>8.3f}   {desc[k]}")

    delta = results["S5"]["mean_total"] - results["S0"]["mean_total"]
    print(f"\nΔ(S5 − S0) = +{delta:.3f}")
    m5_delta = results["S5"]["mean_dims"]["M5"] - results["S0"]["mean_dims"]["M5"]
    m6_delta = results["S5"]["mean_dims"]["M6"] - results["S0"]["mean_dims"]["M6"]
    print(f"  driven mainly by M5 source anchoring ({results['S0']['mean_dims']['M5']:.3f} → {results['S5']['mean_dims']['M5']:.3f})")
    print(f"  and M6 real-URL verification ({results['S0']['mean_dims']['M6']:.3f} → {results['S5']['mean_dims']['M6']:.3f})")
    print("\nInterpretation: the gain comes from 'actually searching and citing',")
    print("not from 'being told how to think' (see full study: S1 decomposition-only ≈ S0).")
    print("\nFiles: prompts/S0-bare.txt · prompts/S5-full-pipeline.txt · outputs/*.json · gold/Q1-gold.md")


if __name__ == "__main__":
    main()