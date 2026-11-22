# N162: 工作点3（悲观估计/高成本低性）：采用 σ_logS = 2.856 和 σ_logH = 3.491（修正自 N39/N40 矛盾，取更激进的方差值）。计算 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

工作点3（悲观估计/高成本低性）：采用 σ_logS = 2.856 和 σ_logH = 3.491（修正自 N39/N40 矛盾，取更激进的方差值）。计算 E[S|Top_k_eff] ≈ 11KB * (1 - 0.3 * 2.856 * 3.491) ≈ 11KB * (1 - 2.99) ≈ 负值。这表明线性修正模型在强负相关下失效，需使用 Copula 模型。若使用截断修正，E[S|Top_k_eff] 至少为 1KB，S_eff ≈ 6700 * 1KB ≈ 6.7 MB。

## Corrected Claim

工作点3（悲观估计/高成本低性）：采用 σ_logS = 2.856 和 σ_logH = 3.491（修正自 N39/N40 矛盾，取更激进的方差值）。计算 E[S|Top_k_eff] ≈ 11KB * (1 - 0.3 * 2.856 * 3.491) ≈ 11KB * (1 - 2.99) ≈ 负值。这表明线性修正模型在强负相关下失效，需使用 Copula 模型。若使用截断修正，E[S|Top_k_eff] 至少为 1KB，S_eff ≈ 6700 * 1KB ≈ 6.7 MB。

## Evidence

先验知识/题面给定，逻辑校验通过：线性修正项 0.3*2.856*3.491≈2.99>1 导致负值，逻辑上确实表明该线性模型在此参数下失效，推导自洽。

## Search Query

Pareto distribution conditional expectation size hot objects negative correlation
