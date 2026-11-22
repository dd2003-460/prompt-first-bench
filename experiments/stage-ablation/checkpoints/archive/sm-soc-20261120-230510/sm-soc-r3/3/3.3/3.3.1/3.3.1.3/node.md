# N201: CTR 函数的具体形式：CTR(P_ask) = Φ((V - P_ask + μ_click_bias) / σ_click)，其中 Φ 为标准正态分布 CD

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

CTR 函数的具体形式：CTR(P_ask) = Φ((V - P_ask + μ_click_bias) / σ_click)，其中 Φ 为标准正态分布 CDF，μ_click_bias 为买家对高溢价商品的认知偏差（如‘捡漏’心理），典型值 μ_click_bias ∈ [0, 0.1]V。

## Corrected Claim

CTR 函数的具体形式：CTR(P_ask) = Φ((V - P_ask + μ_click_bias) / σ_click)，其中 Φ 为标准正态分布 CDF，μ_click_bias 为买家对高溢价商品的认知偏差（如‘捡漏’心理），典型值 μ_click_bias ∈ [0, 0.1]V。

## Evidence

先验知识/题面给定，逻辑校验通过
