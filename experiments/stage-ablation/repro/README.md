# Reproducibility Package

This directory contains everything needed to reproduce the T17-full stage-ablation experiment.

## Contents

| Path | Description |
|------|-------------|
| `prompts/` | 40 prompt variants (8 arms × 5 questions), exported via `build_prompt()` from `ablation_harness.py` |
| `gold/` | Gold assertion sets for all 5 questions (source-of-truth files from workspace) |
| `../score.py` | Primary scorer: LLM-based M1/M2/M3/M4/M5/M6 extraction + weighted total |
| `../score_m7.py` | Rule-based M7 (contradiction reasoning) scorer |
| `../ablation_harness.py` | Experiment harness: arm definitions, prompt construction, vLLM API calls, run metadata |
| `../runs/` | Raw run outputs (210 JSON files: 11 arms × 5Q × 3 reps + hetero-judge results) |
| `../bootstrap-cis.json` | Pre-computed bootstrap CIs (B=1000, percentile, seed=42) |

## How to Re-run

### Prerequisites
- Python 3.10+, `openai` package
- vLLM server with Qwen3.8-27B at `http://localhost:8787/v1` (or set `VLLM_BASE_URL`)
- Gold files must be accessible (see `QUESTIONS` dict in `ablation_harness.py` for paths)

### Step 1: Generate runs
```bash
cd experiments/stage-ablation
python ablation_harness.py --arms S0,S1,S2,S3,S4,S5,S6,S7 --reps 3
# Tool arms (require web access):
python ablation_harness.py --arms S7T,S7F,S7V --reps 3
```

### Step 2: Score
```bash
python score.py aggregate runs/ gold/ --judge-url http://localhost:8787/v1
python score_m7.py runs/  # rule-based, no LLM needed
```

### Step 3: Statistics
```python
import json, numpy as np
data = json.load(open('raw-data-full-perdim.json'))['local_gatefixed_per_run']
# Per-arm×dim means + bootstrap CI (B=1000, percentile, seed=42)
```

## Key Parameters

| Parameter | Value | Source |
|-----------|-------|--------|
| Model | Qwen3.8-27B (vLLM) | `ablation_harness.py` |
| Temperature (S0–S5) | 0 | §3.6 |
| Temperature (S6/S7/S7T/S7F/S7V) | 0.1 + per-rep seed | §3.6 |
| Max tokens | 4096 | harness default |
| Scoring weights | M1×0.25 + M2×0.20 + M3×0.15 + M4×0.20 + M5×0.10 + M6×0.10 | `score.py` |
| Bootstrap | B=1000, percentile, seed=42 | `bootstrap-cis.json` |

## Known Limitations
- S6/S7 full 6-dim per-run scores were not retained (only M1+M4 from hetero-judge). Re-scoring required for full CI coverage on these arms.
- S7T/S7F/S7V per-run scores from a single scoring pass; re-scoring yields different values (LLM judge non-determinism).
- Gold answers are single-authored; no IRR computed.