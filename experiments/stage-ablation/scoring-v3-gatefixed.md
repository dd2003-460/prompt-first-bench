# Scoring v3 — Gate-Fixed (2026-11-05)

> **大白话**：修了评分脚本的 bug（之前一个报告里只要出现一个网址，全文所有数字都算有来源），重新跑了全部 90 个 run。结果：H1 方向没变，分解确实比直接答好（+0.129）。S2 略降是因为它的某些数字现在被正确判定为无来源。

## Per-arm totals (same-source 27B judge, gate-fixed, n=90)

| Arm | Old (buggy) | New (fixed) | Δ |
|-----|-------------|-------------|---|
| S0 | 0.391 | 0.397 | +0.006 |
| S1 | 0.509 | 0.526 | +0.017 |
| S2 | 0.570 | 0.552 | -0.018 |
| S3 | 0.550 | 0.546 | -0.004 |
| S4 | 0.569 | 0.569 | +0.000 |
| S5 | 0.580 | 0.579 | -0.001 |

## H1 verdict (gate-fixed)

- S1 - S0: +0.118 (old) → +0.129 (new)
- Direction: UNCHANGED (positive both ways)
- **H1 CONFIRMED under same-source judge after gate fix.**

## Cross-judge comparison

| Judge | S0 | S1 | S1-S0 | H1 |
|-------|-----|-----|-------|-----|
| Same-source 27B (gate-fixed) | 0.397 | 0.526 | +0.129 | CONFIRMED |
| Hetero (arena GPT, Q1 only) | 0.639 | 0.452 | -0.187 | REFUTED |

> **解读**：同族评委说分解有用（+0.129），异族评委说没用甚至有害（-0.187）。这是 judge 依赖性的核心证据——同一组数据，不同评委给出相反结论。论文应该报告两个方向，而不是选一个。
