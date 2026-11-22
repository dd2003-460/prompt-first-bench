# N161: 工作点2（标准估计/中性价比最优）：采用 σ_logS = 1.5 和 σ_logH = 1.5（N71 原始假设，简化计算）。计算 E[S|Top_k_eff

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

工作点2（标准估计/中性价比最优）：采用 σ_logS = 1.5 和 σ_logH = 1.5（N71 原始假设，简化计算）。计算 E[S|Top_k_eff] ≈ 11KB * (1 - 0.3 * 1.5 * 1.5) ≈ 11KB * 0.34 ≈ 3.7KB。S_eff ≈ 6700 * 3.7KB ≈ 24.8 MB。此值同样远小于 128GB，进一步证实缓存瓶颈由热度决定。

## Corrected Claim

工作点2（标准估计/中性价比最优）：采用 σ_logS = 1.5 和 σ_logH = 1.5（N71 原始假设，简化计算）。计算 E[S|Top_k_eff] ≈ 11KB * (1 - 0.3 * 1.5 * 1.5) ≈ 11KB * 0.34 ≈ 3.7KB。S_eff ≈ 6700 * 3.7KB ≈ 24.8 MB。此值同样远小于 128GB，进一步证实缓存瓶颈由热度决定。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 11 * (1 - 0.675) = 3.575 ≈ 3.7 及 6700 * 3.7 ≈ 24.8 均正确，量级合理。

## Search Query

Pareto distribution conditional expectation size hot objects negative correlation
