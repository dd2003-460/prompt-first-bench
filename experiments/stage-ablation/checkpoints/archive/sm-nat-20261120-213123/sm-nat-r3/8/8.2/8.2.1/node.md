# N160: 工作点1（保守估计/高性低成）：采用 σ_logS = 0.909 和 σ_logH = 1.425（修正自 N76/N77 矛盾，取更保守的方差值）。计算 E

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

工作点1（保守估计/高性低成）：采用 σ_logS = 0.909 和 σ_logH = 1.425（修正自 N76/N77 矛盾，取更保守的方差值）。计算 E[S|Top_k_eff] ≈ 11KB * (1 - 0.3 * 0.909 * 1.425) ≈ 11KB * 0.60 ≈ 6.6KB。S_eff ≈ 6700 * 6.6KB ≈ 44.2 MB。此值远小于 128GB，证实缓存容量过剩。

## Corrected Claim

工作点1（保守估计/高性低成）：采用 σ_logS = 0.909 和 σ_logH = 1.425（修正自 N76/N77 矛盾，取更保守的方差值）。计算 E[S|Top_k_eff] ≈ 11KB * (1 - 0.3 * 0.909 * 1.425) ≈ 11KB * 0.60 ≈ 6.6KB。S_eff ≈ 6700 * 6.6KB ≈ 44.2 MB。此值远小于 128GB，证实缓存容量过剩。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Pareto distribution conditional expectation size hot objects negative correlation
