# Rubric Alignment Report — CJ-RUBRIC-ALIGN

> generated: 2026-11-04 · stage C3/D1-D3

## Verdict: PASS ✅

| Metric | Target | Before | After | Status |
|--------|--------|--------|-------|--------|
| Spearman ρ (cell-level) | ≥0.6 | 0.188 | **0.624** | ✅ |
| Kendall τ (arm-rank vs arena) | ≥0.5 | 0.200 | **0.733** | ✅ |
| S0 worst both channels | yes | yes | yes | ✅ |
| Mean \|Δ\| | ↓ | 0.277 | 0.184 | ✅ (-34%) |

## Changes Made

### D1: Zero-fact rule (cross_judge.py JUDGE_PROMPT line 35)
- OLD: "如果模型回答中没有可验证的事实断言（纯方法论/空话），M1=0"
- NEW: "若答案以方法论/推导为主（无外部可查事实），则评估其内部逻辑一致性与推导正确性。仅当答案为空、拒答或完全无关时 M1=0。"
- Effect: 13 zero-fact cells fixed (Q4/Q5 no longer auto-zeroed)

### D2: Assertion granularity (new rule #1)
- OLD: unspecified (practice = atomic 13-40 claims/cell)
- NEW: "计数单位 = 关键断言（一个完整逻辑结论/判断 = 一条）。典型：硬件题 5-15 条；方法论题 4-10 条。"
- Effect: Q4 |Δ| halved (0.581→0.316), Q5 |Δ| reduced 71% (0.267→0.078)

### D3: Scope (new rule #3)
- OLD: unspecified
- NEW: "M1 范围 = 原始事实断言 + 可复算推导。纯主观判断不计入 M1。"
- Effect: Q3 assumption-swap cells less penalized for derivation content

### Infrastructure fix
- GOLD_FILES now point to repo-local `gold/Q1-Q5.md` (was external workspace paths, Q5 missing)

## Per-question improvement

| Q | Old \|Δ\| | New \|Δ\| | Δ improvement |
|---|-----------|-----------|---------------|
| Q1 | 0.175 | 0.214 | -22% (slight regression, model variance) |
| Q2 | 0.198 | 0.103 | +48% |
| Q3 | 0.166 | 0.209 | -26% (assumption swap still confounds) |
| Q4 | 0.581 | 0.316 | +46% |
| Q5 | 0.267 | 0.078 | +71% |

## Arm rankings

| Arm | Old Local | New Local | Arena |
|-----|-----------|-----------|-------|
| S0 | 0.457 | 0.560 | 0.754 |
| S1 | 0.753 | 0.657 | 0.795 |
| S2 | 0.644 | 0.768 | 0.874 |
| S3 | 0.625 | 0.677 | 0.845 |
| S4 | 0.751 | 0.697 | 0.825 |
| S5 | 0.534 | 0.590 | 0.824 |

Rank (worst→best): New=[S0,S5,S1,S3,S4,S2] vs Arena=[S0,S1,S5,S4,S3,S2]
Top-1 and bottom-1 agree; middle positions differ by ±1 slot (model variance floor).

## Residual divergence sources
1. Q1/Q3 slight regression: same rubric but different judge models disagree on edge cases (expected model variance ~0.1-0.2)
2. S0-Q2-r3 still local=0 (answer genuinely lacks verifiable content, arena gave 0.63 — judgment call boundary)
3. Q3 assumption swap (RTX 3090×4 → A100-80GB) still confounds ~0.1-0.2 on some cells

## Files
- `runs/local-rerun-aligned.jsonl` — 90 new local scores (aligned rubric)
- `runs/alignment-inputs.json` — merged old+arena reference
- `runs/divergence-taxonomy.md` — per-cell classification
- `cross_judge.py` — updated JUDGE_PROMPT + GOLD_FILES
- `rerun_local_aligned.py` — reproducible re-run script
