# V3 Full Rescore — All 61 Runs (2026-11-06)

## What changed vs V2
1. **Q4 fix**: token equivalent added to question stem (was missing, caused M1=0 for S1/S5)
2. **Judge v2→v3**: full gold text (no [:6000] truncation), type-aware assertion extraction
3. **Smart truncation** (new): two-pass outputs with numbers in second half no longer lose all assertions to naive [:12000]
4. **--multi N flag**: judge sampling (verified unnecessary — judge is deterministic at temp=0)

## Method
- 61 runs scored: 45 main-arm (S0/S1/S5 × Q1-Q5 × r1-r3) + 16 secondary-arm (Arena×3, S8A-F×13)
- Judge: qwen3.8-27b @ localhost:8787, temp=0, deterministic (verified: 5 consecutive calls → identical)
- Main arms: full M1+M4 scoring (4 workers, 409s)
- Secondary arms: M1 re-scored with smart truncation, M4 reused from prior pass
- M6: URL declaration heuristic (no network check for secondary arms)

## Results (per-run mean, n=15/arm unless noted)

### Main Arms
| Arm | N   | Total | M1    | M2    | M3    | M4    | M5    | M6    |
|-----|-----|-------|-------|-------|-------|-------|-------|-------|
| S0  | 15  | 0.615 | 0.904 | 0.520 | 0.844 | 0.830 | 0.010 | 0.000 |
| S1  | 15  | 0.630 | 0.863 | 0.580 | 0.933 | 0.793 | 0.000 | 0.000 |
| S5  | 15  | 0.805 | 0.968 | 0.598 | 0.956 | 0.890 | 0.289 | 0.000 |

Δ(S5-S0) = +0.190 · Δ(S1-S0) = +0.014 · Δ(S5-S1) = +0.176

### Secondary Arms
| Arm   | N | Total | M1    | Note                        |
|-------|---|-------|-------|-----------------------------|
| Arena | 3 | 0.713 | 1.000 | LMArena agent mode          |
| S8A   | 1 | 0.553 | 0.692 | structured quant            |
| S8B   | 1 | 0.530 | 1.000 |                             |
| S8C   | 1 | 0.710 | 1.000 |                             |
| S8D   | 7 | 0.722 | 0.960 | decomposition arm           |
| S8E   | 3 | 0.615 | 0.875 | two-pass (smart trunc fixed)|

## Key Findings

1. **Arm ordering preserved**: S5 > S1 > S0 (same as V2). The memory hook (S5) adds +0.19 over baseline.
2. **Q4 fix validated**: all 9 Q4 runs now M1≥0.933 (was 0.000 for S1/S5 in V2).
3. **S8E smart truncation fix**: M1 went 0.000 → 0.875. Two-pass output had all numbers in chars 12000-19072; naive truncation sliced them off.
4. **Judge determinism confirmed**: temp=0 + same weights = bit-for-bit reproducible. --multi N provides no variance reduction.
5. **S1-Q5-r1 negative shift accepted**: M1 0.571→0.000. V3 judge correctly identified missing methodological steps. Legitimate strictness improvement.

## Files
- `scores-v3.json` — 45 main-arm entries (full M1+M4)
- `scores-v3-secondary.json` — 16 secondary-arm entries (M1 re-scored, M4 from prior)
- `score.py` — commit: _smart_truncate() + --multi N flag
