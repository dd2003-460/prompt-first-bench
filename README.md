# pfb (prompt-first-bench)

**Research question**: Does a structured 1-loop research pipeline (decompose → research → cross-check → plan → verify → review) improve LLM answer quality, and by how much per stage?

This repo contains the full experimental apparatus, raw data, scoring harness, and paper draft for a systematic stage-ablation study on a 27B open-weight model (Qwen3.8-27B) with no tool access.

**New here?** Start with [`demo/`](demo/) — one question, two arms, runs offline in seconds: `python3 demo/run_demo.py`.

## Key Results (TL;DR)

| Finding | Evidence |
|---------|----------|
| Full pipeline (S5) > bare (S0): +0.182 mean total | §4.1 of paper |
| Largest single-stage gain: decomposition (S1): +0.129 | §4.1 |
| Fuzzy prompt (S6) > bare (S0) with zero structure: +0.065 | §4.3 |
| Hybrid prompt (S7) best on data-intensive Qs: Q1=0.717, Q2=0.700 | §4.2 |
| Contradiction reasoning (M7) *degraded* by mechanical prompts | §4.4 |
| Hetero-judge confirms all orderings; local bias ≈0.15 conservative | §4.5 |

## Directory Structure

```
pfb/
├── README.md                    ← you are here
├── CLAUDE.md                    ← agent instructions (for arena/Claude sessions)
├── APPROVALS.md                 ← pending human decisions
├── BRIDGE-REPORT.md             ← cross-project status bridge
├── experiments/
│   └── stage-ablation/          ← ★ MAIN EXPERIMENT (T17)
│       ├── paper-draft.md       ← paper v2.0 (submission-ready draft)
│       ├── T17-stage-ablation-final-report.md  ← full internal report (341 lines)
│       ├── ablation_harness.py  ← experiment runner (S0-S7 arms × Q1-Q5 × r1-r3)
│       ├── score.py             ← M1-M6 LLM judge scorer
│       ├── score_m7.py          ← M7 rule-based contradiction-reasoning scorer
│       ├── scoring-v4-m7.md     ← M7 methodology + full per-arm table
│       ├── scientisttwo-comparison.md  ← positioning vs. ScientistTwo
│       ├── competitor-survey.md ← DREAM/GPT-Researcher/STORM comparison
│       ├── gold/                ← gold answers (Q1-Q5, assertion-annotated)
│       ├── runs/                ← raw run artifacts (JSON per arm×Q×rep)
│       │   ├── S{0-7}-Q{1-5}-r{1-3}.json
│       │   ├── hetero-judge-s6s7-results.json  ← T26 arena GPT-5.5 scores
│       │   └── receipt-t26-hetero-judge.md
│       ├── raw-data-full-perdim.json  ← consolidated 90-run dataset (S0-S5)
│       └── tasks/               ← task books (T26, T27 decompositions)
├── bench/
│   └── rubric-v3/               ← rubric v3.1 (frozen @ a843890)
│       ├── DRAFT-rubric-v3.1-s01-fix.md
│       └── ablation/            ← rubric ablation experiments
├── loop/                        ← 1-loop stage definitions (00..04.5)
├── sop/                         ← operational SOPs (arena pipeline, etc.)
├── arena-prompts/               ← arena task cards (batches 9-11)
├── src/                         ← pixel video rendering (legacy deliverables)
├── scripts/                     ← build/render/audio scripts
└── outputs/                     ← rendered videos (legacy)
```

## Quick Start: Reproduce Core Experiment

### Prerequisites

- Python 3.10+
- A 27B model served via vLLM at `localhost:8787` (or modify endpoint in harness)
- ~10 GB VRAM minimum for inference

### Run the Ablation

```bash
cd experiments/stage-ablation

# Run all arms (S0-S7) × 5 questions × 3 reps = 120 runs (~45 min)
python ablation_harness.py --all

# Or run a single arm
python ablation_harness.py --arm S7 --questions Q1,Q2

# Score results (requires judge endpoint)
python score.py --input runs/ --output /tmp/scores.json

# Score M7 (rule-based, no API needed)
python score_m7.py --input runs/
```

### Read the Results

- **Paper**: `experiments/stage-ablation/paper-draft.md` (v2.0, 28KB)
- **Internal report**: `experiments/stage-ablation/T17-stage-ablation-final-report.md` (341 lines, includes all intermediate findings)
- **Raw data**: `experiments/stage-ablation/raw-data-full-perdim.json` (90 runs, per-dimension scores)

## Experimental Design Summary

**8 arms** (cumulative S0-S5 + non-cumulative S6/S7) × **5 questions** (GPU, distributed systems, SLO, memory hierarchy, epistemology) × **3 reps** = 120 runs.

**7 scoring dimensions**: M1 fact accuracy (0.25), M2 self-assessment calibration (0.10), M3 structure (0.10), M4 gap identification (0.20), M5 source quality (0.10), M6 citation verifiability (0.10), M7 contradiction reasoning (0.15).

**Judges**: Primary = same-model (27B, confidence-capped 0.7). Hetero = arena-hosted frontier model (T26 validation).

## Status

| Component | State |
|-----------|-------|
| Paper draft | ✅ v2.0 ready (needs submission) |
| Rubric | ✅ v3.1 frozen |
| S0-S5 data | ✅ 90 runs complete |
| S6-S7 data | ✅ 30 runs complete |
| M7 scoring | ✅ rule-based, validated |
| Hetero validation | ✅ T26 complete (arena GPT-5.5) |
| arXiv upload | ⏳ pending manual login |

## Legacy Content

The `src/`, `scripts/`, `outputs/` directories contain pixel-art video rendering code (Clawd story series, 2026-10). These are completed deliverables preserved for reference; they are not part of the current research line. The `arena-prompts/batch{9,10,11}/` directories contain episode task cards from the same period.

## License

MIT (research use). Data and code released for reproducibility.