# Minimal reproducible demo (Q1: H100 PCIe vs SXM)

One question, two arms, six scoring dimensions. Runs offline in seconds — no model needed for the bundled data.

```bash
python3 run_demo.py
```

## What you'll see

| Arm | Prompt | Mean total |
|-----|--------|-----------|
| S0 | bare question only | ~0.58 |
| S5 | full 6-stage research pipeline (decompose → research → cross-check → plan → verify → review) | ~0.83 |

The gap is driven by **M5 source anchoring** (per-number citation density: 0.05 → 0.35) and **M6 real-URL verification** (0.00 → 1.00), not by factual accuracy (M1 stays ~0.94 both ways). The structured pipeline's value is making the model *actually search and cite*, not making it *think better*.

## Scoring rubric (weights sum to 1.0)

| Dim | Weight | Measures | Method |
|-----|--------|----------|--------|
| M1 | 0.25 | Factual accuracy vs gold facts | LLM judge extracts assertions, checks each against `gold/Q1-gold.md` |
| M2 | 0.20 | Structure + limit statements upfront | Regex: tables/lists/headers + "limitation" sentences in first third |
| M3 | 0.15 | Uncertainty marking | Count of hedge phrases ("uncertain / needs verification / ...") |
| M4 | 0.20 | Known-gap coverage | LLM judge: did the output flag the gaps listed in gold? |
| M5 | 0.10 | Per-number source anchoring | Fraction of numeric claims with an inline citation anchor |
| M6 | 0.10 | Cited URLs are real | HTTP liveness check on declared sources |

**Known limitation**: M1/M4 use the same 27B model as judge (temp=0, deterministic). Same-family judge bias is tracked separately in the full study (hetero-judge calibration, κ reported there). Treat absolute scores as conf ≤ 0.7; relative ordering across arms is robust.

## Files

```
prompts/S0-bare.txt           # the exact prompt sent to the model (S0 arm)
prompts/S5-full-pipeline.txt  # the exact prompt (S5 arm, ~9KB, all 6 stage files inlined)
outputs/S0-Q1-r1.json         # raw model output + metadata (one rep)
outputs/S5-Q1-r1.json         # raw model output + cited sources (one rep)
gold/Q1-gold.md               # human-curated fact sheet used as scoring anchor
run_demo.py                   # this demo: loads pre-computed scores from runs-r293/
```

Scores shown come from `experiments/stage-ablation/runs-r293/scores-v3.json` (n=3 reps/arm for Q1; full study is n=15/arm across 5 questions × 5 arms).

## Regenerating outputs (optional, needs local model)

The full harness (`experiments/stage-ablation/ablation_harness.py`) calls a local 27B endpoint at `http://127.0.0.1:8787`. To reproduce from scratch:

```bash
cd experiments/stage-ablation
python3 ablation_harness.py run --arms S0,S5 --qs Q1 --n 3
python3 score.py aggregate runs/ gold/
```

Requires: Qwen3.8-27B served via vLLM or compatible OpenAI-compatible API on port 8787.