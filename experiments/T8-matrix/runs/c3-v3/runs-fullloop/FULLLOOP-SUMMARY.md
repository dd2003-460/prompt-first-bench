# T8-C3 Fullloop Matrix — Final Summary

## Status: COMPLETE (generation) / PENDING (proper judge)

## Matrix Coverage
- 9 configs × 2 domains × 2 seeds = 36 planned cells
- + B-2del-fo (degenerate, valid finding) = 37 total
- 24 valid 4-stage outputs (S01→S04 complete, S02 > 500c)
- 10 degenerate (S02 execution-mode collapse, < 500c)
- 1 S01 degenerate (B-2del-fo)
- 2 pilot cells (3-stage only, no S04)

## Key Findings

### F1: Evidence Component → S02 Execution-Mode Degeneration (38%)
Configs WITH evidence component (A-full, B-nofreeze, B-noowner, B-sham): 10/26 cells degenerate.
Configs WITHOUT evidence component (B-none, B-noevidence, B-2del-fe, B-2del-eo): 0/16.
Root cause: ralph/ego-browser tool instructions in evidence.md trigger "execution mode" in no-tool vLLM env.
**This is a protocol-environment interaction effect, not a component content causal effect.**

### F2: S04 Quality Robust to Component Removal
Keyword coverage of opportunity items: 66-80% across ALL configs (no significant difference).
The final report quality does NOT depend on which pipeline components are present.
Implication: the value of structured pipeline is in PROCESS (S01-S03), not FINAL OUTPUT.

### F3: B-2del-fo S01 Degeneration (Structural Scaffolding Effect)
Removing freeze+owner while keeping evidence → model echoes tool instruction instead of decomposing.
Shows that goal decomposition (S01) requires structural framing; without it, the model defaults to action mode.

## Judge Status
- Local 27B same-family judge: ALL 10/10 (useless, self-bias confirmed)
- Keyword coverage: 66-80% (discriminative but crude, n=16)
- **Proper arena hetero-judge: PENDING** (arena unavailable as of 2026-11-06)
- **Publication-grade scoring requires arena GPT-5.5/Claude re-judgment**

## Files
- `receipt-fullloop-batch1.json` — seed-a batch (10/12 cells)
- `receipt-fullloop-batch2-seedb.json` — seed-b batch (16 cells) + key finding
- `judge-results-fullloop.json` — local judge (all 10/10, documented as self-bias)
- `B-*/{D1,D2}/seed{a,b}/stage01-04.{md,json}` — raw outputs

## Next Steps (blocked-on-arena)
1. Arena hetero-judge on 24 valid S04 outputs (M1+M4 dimensions, per T17 protocol)
2. Proper per-dimension scoring with frontier model
3. Integrate into paper §5 (fullloop section) or supplementary
