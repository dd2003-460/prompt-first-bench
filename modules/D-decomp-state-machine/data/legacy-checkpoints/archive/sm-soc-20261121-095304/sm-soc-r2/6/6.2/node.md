# N61: 信息不对称导致的σ高估机制：卖家对买家估值分布的认知方差 σ_perceived 与实际方差 σ_real 的偏差。假设 σ_perceived = α * σ

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

信息不对称导致的σ高估机制：卖家对买家估值分布的认知方差 σ_perceived 与实际方差 σ_real 的偏差。假设 σ_perceived = α * σ_real，其中 α > 1 为高估系数。若 α = 1.5，则卖家认为 δ=20% (1.67σ_real) 处于 2.5σ_perceived 的'安全区'，但实际上仅处于 1.67σ_real，导致卖家错误地认为成交概率足够高。

## Corrected Claim

信息不对称导致的σ高估机制：卖家对买家估值分布的认知方差 σ_perceived 与实际方差 σ_real 的偏差。假设 σ_perceived = α * σ_real，其中 α > 1 为高估系数。若 α = 1.5，则卖家认为 δ=20% (1.67σ_real) 处于 2.5σ_perceived 的'安全区'，但实际上仅处于 1.67σ_real，导致卖家错误地认为成交概率足够高。

## Evidence

先验知识/题面给定，逻辑校验通过：数学推导自洽（1.67 * 1.5 ≈ 2.5），符合正态分布下标准差倍数与置信区间的对应关系。
