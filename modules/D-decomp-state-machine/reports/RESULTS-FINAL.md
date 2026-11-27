# PFB Stage-Ablation — Final Results (V3 Judge)

> origin: ai · 2026-11-06 · commit f876e1e + 6720a29
> **Judge**: qwen3.8-27b @ localhost:8787, temp=0, deterministic (verified: 5× identical)
> **Caveat**: Same-family judge (qwen judging qwen outputs). Absolute scores may be inflated vs hetero-judge. All numbers below carry this caveat.

## Method

- **Runs**: 61 total (45 main-arm + 16 secondary-arm) from runs-r293/
- **Scoring**: score.py v3 (commit f876e1e) with smart truncation, type-aware gold extraction
- **Metrics**: M1 (factuality), M2 (structure), M3 (hedge control), M4 (completeness), M5 (anchoring), M6 (sourcing)
- **Weights**: M1=0.35, M2=0.10, M3=0.10, M4=0.25, M5=0.05, M6=0.15 (Q5 override: M1=0.40, M4=0.20)
- **Statistics**: Bootstrap 95% CI (10k resamples, seed=42); paired sign test (exact, two-sided)
- **Truncation**: _smart_truncate() — keeps numeric-dense half for >12k char outputs

## Main Arms (n=15/arm, per-run mean ± 95% CI)

| Arm | Description | Total | 95% CI | M1 | M2 | M3 | M4 | M5 | M6 |
|-----|-------------|-------|--------|----|----|----|----|----|----|
| S0 | Baseline (no structure) | 0.615 | [0.533, 0.670] | 0.904 | 0.520 | 0.844 | 0.830 | 0.010 | 0.000 |
| S1 | Decomposition tree | 0.630 | [0.599, 0.657] | 0.863 | 0.580 | 0.933 | 0.793 | 0.000 | 0.000 |
| S5 | Memory hook (S1+hooks) | **0.805** | [0.762, 0.841] | 0.968 | 0.598 | 0.956 | 0.890 | 0.289 | 1.000 |

## Arm Deltas (paired by qid+rep, n=15 pairs)

| Comparison | Δ Total | Sign pattern | p (sign test) | Sig |
|------------|---------|--------------|---------------|-----|
| S5 − S0 | **+0.190** | +14/−1/0 | 0.0010 | ** |
| S1 − S0 | +0.014 | +7/−7/01 | 1.0000 | ns |
| S5 − S1 | **+0.176** | +15/−0/0 | 0.0001 | ** |

\*\* p < 0.01 · \* p < 0.05 · ns = not significant

## Per-Metric CIs (main arms)

| Metric | S0 [CI] | S1 [CI] | S5 [CI] |
|--------|---------|---------|---------|
| M1 factuality | 0.904 [0.765, 0.982] | 0.863 [0.711, 0.967] | 0.968 [0.939, 0.993] |
| M2 structure | 0.520 [0.503, 0.540] | 0.580 [0.538, 0.631] | 0.598 [0.546, 0.665] |
| M3 hedge ctrl | 0.844 [0.667, 1.000] | 0.933 [0.867, 1.000] | 0.956 [0.889, 1.000] |
| M4 completeness | 0.830 [0.677, 0.950] | 0.793 [0.680, 0.907] | 0.890 [0.733, 1.000] |
| M5 anchoring | 0.010 [0.000, 0.026] | 0.000 [0.000, 0.000] | 0.289 [0.241, 0.321] |
| M6 sourcing | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 1.000 [1.000, 1.000] |

## Secondary Arms (limited n, exploratory only)

| Arm | N | Total | 95% CI | M1 | Note |
|-----|---|-------|--------|----|------|
| Arena | 3 | 0.713 | [0.500, 0.909] | 1.000 | LMArena agent mode |
| S8A | 1 | 0.553 | — | 0.692 | structured quant |
| S8B | 1 | 0.530 | — | 1.000 | single run |
| S8C | 1 | 0.710 | — | 1.000 | single run |
| S8D | 7 | 0.722 | [0.663, 0.783] | 0.960 | ⚠️ non-reproducible (prompt lost) |
| S8E | 3 | 0.615 | [0.615, 0.615] | 0.875 | two-pass, smart-trunc fixed |

## Key Findings

1. **Memory hook effect is real and large**: S5−S0 = +0.190 (p=0.001), driven primarily by M5 (anchoring: 0.01→0.29) and M6 (sourcing: 0.00→1.00). The hook makes the model cite sources and anchor claims to retrieved memory.
2. **Decomposition alone does not help**: S1−S0 = +0.014 (ns). Structure without retrieval adds no measurable value.
3. **The hook's contribution is +0.176 over decomposition** (p=0.0001, 15/15 positive). This is the cleanest signal in the benchmark.
4. **M1 (factuality) is high across all arms** (0.86-0.97): the 27B model is factually competent; differentiation comes from process metrics (M5, M6).

## Limitations

| # | Issue | Impact | Mitigation |
|---|-------|--------|------------|
| L1 | Same-family judge (qwen judges qwen) | Absolute scores may be inflated; relative ordering likely preserved | Future: hetero-judge (GPT-4o/Claude) re-score. conf-0.2 on absolute values. |
| L2 | n=15/arm | Power limited for small effects (<0.05); CIs are wide for secondary arms | Future: n≥30/arm for publication-grade claims |
| L3 | S8D prompt unrecoverable | Cannot verify what S8D actually tested | Marked "non-reproducible"; excluded from main analysis |
| L4 | Single model (qwen3.8-27b) | Results may not generalize to other models/families | Future: multi-model replication |
| L5 | 5 questions × 3 reps | Question-level variance confounded with arm effect | Paired design partially controls this; future: more questions |

## Provenance

- Score data: `runs-r293/scores-v3.json` (45 main) + `runs-r293/scores-v3-secondary.json` (16 secondary)
- Statistics: `runs-r293/stats-v3.json` (bootstrap + sign test)
- Scoring code: `score.py` @ f876e1e (smart truncation + --multi flag)
- Rescore notes: `RESCORE-V3-NOTES.md`
- Judge server: qwen3.8-27b via vLLM @ localhost:8787
