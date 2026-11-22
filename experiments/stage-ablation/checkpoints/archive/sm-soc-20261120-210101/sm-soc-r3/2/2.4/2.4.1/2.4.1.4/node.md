# N204: 平台侧策略噪声投影：平台推荐权重 W_platform 的随机扰动 δ_W ~ U(-δ_W_max, δ_W_max)，其中 δ_W_max = ε_max 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N55

## Claim

平台侧策略噪声投影：平台推荐权重 W_platform 的随机扰动 δ_W ~ U(-δ_W_max, δ_W_max)，其中 δ_W_max = ε_max * β_platform，β_platform 为平台对噪声的敏感度系数，假设值为 0.3。

## Corrected Claim

平台侧策略噪声投影：平台推荐权重 W_platform 的随机扰动 δ_W ~ U(-δ_W_max, δ_W_max)，其中 δ_W_max = ε_max * β_platform，β_platform 为平台对噪声的敏感度系数，假设值为 0.3。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

platform recommendation weight stochastic perturbation sensitivity coefficient
