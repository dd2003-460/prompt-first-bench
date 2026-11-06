# D1 Baseline Scoring (GPT Researcher pipeline)

> generated: 2026-11-07 · D1 = GPT Researcher default pipeline, local 27b + duckduckgo
> scored via S0-labeled temp dir (runs-d1score/); arm label relabeled to D1 here
> judge: local 27b (self-judge, conf cap 0.7) — same caveat as main scoring.md
> runs scored: 5 (one rep per question)

| Arm | Q | Rep | M1 | M2 | M3 | M4 | M5 | M6 | **Total** | Wall(s) |
|-----|---|-----|----|----|----|----|----|----|-------|---------|
| D1 | Q1 | r1 | 0.75 | 0.60 | 1.00 | 0.00 | 0.66 | 0.33 | **0.557** | 90.2 |
| D1 | Q2 | r1 | 1.00 | 0.67 | 1.00 | 0.60 | 0.43 | 0.33 | **0.729** | 153.9 |
| D1 | Q3 | r1 | 1.00 | 0.50 | 1.00 | 0.50 | 0.73 | 0.67 | **0.739** | 45.8 |
| D1 | Q4 | r1 | 0.00 | 0.70 | 1.00 | 0.40 | 0.46 | 0.00 | **0.416** | 115.9 |
| D1 | Q5 | r1 | 1.00 | 0.62 | 1.00 | 0.00 | 0.30 | 0.67 | **0.568** | 171.6 |

**D1 mean Total: 0.602** (n=5, one rep per Q)

## vs S-arm means (from scoring.md n=30/arm, self-judge)

| Arm | Mean Total | Δ vs D1 |
|-----|-----------|---------|
| S0 | 0.5558 | -0.046 |
| S1 | 0.5746 | -0.027 |
| S5 | 0.7907 | +0.189 |

## Caveats

- D1 has only 1 rep per question; S-arms have 30 total (6 per Q). Variance comparison not possible yet.
- Self-judge bias applies equally to both sides (same 27b scores both), so relative ordering is the usable signal; absolute values capped at conf 0.7.
- D1 run used duckduckgo retriever with no API key; retrieval quality may be below GR's normal Tavily/SerpAPI config → this is a floor, not GR's best case.
- HBM systemic error (PCIe=HBM3 claim) present in D1-Q1 output — same failure mode as S arms, see fault-index.
