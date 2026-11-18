# N161: 基于 Copula 修正后的 K_eff 增量：使用 E[S|F∈CachedSet] ≈ 8.2 KB（来自 N89），K_eff = 1.374e11 / 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N71

## Claim

基于 Copula 修正后的 K_eff 增量：使用 E[S|F∈CachedSet] ≈ 8.2 KB（来自 N89），K_eff = 1.374e11 / 8.2e3 ≈ 16.756e6，相比独立假设 K_base = 12.494e6，增量为 (16.756/12.494 - 1) * 100% ≈ 34.1%，远高于线性近似的 17.6%。

## Corrected Claim

基于 Copula 修正后的 K_eff 增量：使用 E[S|F∈CachedSet] ≈ 8.2 KB（来自 N89），K_eff = 1.374e11 / 8.2e3 ≈ 16.756e6，相比独立假设 K_base = 12.494e6，增量为 (16.756/12.494 - 1) * 100% ≈ 34.1%，远高于线性近似的 17.6%。

## Evidence

先验知识/题面给定，逻辑校验通过：1.374e11 / 8.2e3 ≈ 16.756e6，(16.756/12.494 - 1) ≈ 34.1%，计算无误且量级合理。
