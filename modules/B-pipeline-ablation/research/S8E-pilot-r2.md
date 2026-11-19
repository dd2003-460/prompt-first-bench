# S8E Pilot Round 2 (2026-11-06)

## Protocol
- s8e_pilot.py, temp=0.1, max_tokens=8000
- Q1 + Q4 × 2 reps = 4 runs
- Judge: qwen3.8-27b local, M1 (assertion-based) + M4 (gap ID), conf≤0.7
- Sources: research_hook (arXiv API multi-query + keyword filter)

## Results

| Run | M1 | M1 detail | M4 | wall_s | tokens_out |
|-----|-----|-----------|-----|--------|-----------|
| S8E-Q1-r1 | 0.333 | 3/9 | 0.90 | 14.1 | 2629 |
| S8E-Q1-r2 | 0.600 | 3/5 | 0.60 | 13.1 | 2527 |
| S8E-Q4-r1 | 0.875 | 7/8 | 0.90 | 165.9 | 3180 |
| S8E-Q4-r2 | 0.400 | 2/5 | 0.60 | 20.7 | 3821 |

**Means**: Q1 M1=0.467, Q4 M1=0.638, overall M4=0.75

## Comparison (paper §5.1 baselines, n=15/arm)

| Arm | Q1 M1 | Q4 M1 | Overall M1 | M4 |
|-----|-------|-------|-----------|-----|
| S7 (no tools) | 0.80 | 0.33 | 0.771 | 0.650 |
| S7F (filtered) | ~0.60 | ~0.60 | 0.605 | 0.360 |
| S7V (two-pass) | 0.55 | 0.93 | 0.762 | 0.520 |
| **S8E (this)** | **0.467** | **0.638** | — | **0.75** |

## Conclusion

1. **M1: S8E ≤ S7V confirmed.** Single-pass embedded verification does not replicate two-pass claim checking. The model cannot simultaneously organize content, verify against sources, and format annotations without attention dilution. Paper §4.3(5) directional finding stands.

2. **M4: S8E > S7V (0.75 vs 0.52).** New nuance: the inline "flag what you can't verify" instruction improves explicit gap identification. The model is more honest about uncertainty when told to check in-line, even though it's less accurate on facts.

3. **High variance** (Q1: 0.333→0.600, Q4: 0.875→0.400). n=2 insufficient for causal claims. The Q4-r1 outlier (0.875, 165s wall time suggesting extended reasoning) shows the approach CAN work when the model allocates sufficient attention to verification.

4. **Practical implication unchanged**: two-pass S7V remains the recommended architecture for fact accuracy. S8E's M4 advantage could be exploited in a hybrid: use S8E-style inline gap-flagging in pass 1, then S7V-style assertion checking in pass 2. But this is speculative (n=2).

## Files
- `runs/S8E-Q{1,4}-r{1,2}.json` — raw outputs
- `s8e-scores.json` — judge scores
