# N169: 成交概率对价格偏差 δ 的敏感度修正：考虑到价格离散性，实际成交概率 P(deal) 应修正为 ∫[P_list, ∞) φ((x-μ)/σ) dx * (1 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

成交概率对价格偏差 δ 的敏感度修正：考虑到价格离散性，实际成交概率 P(deal) 应修正为 ∫[P_list, ∞) φ((x-μ)/σ) dx * (1 - λ_discrete)，其中 λ_discrete 为离散价格导致的有效供给减少系数，需根据商品库存密度估算。

## Corrected Claim

成交概率对价格偏差 δ 的敏感度修正：考虑到价格离散性，实际成交概率 P(deal) 应修正为 ∫[P_list, ∞) φ((x-μ)/σ) dx * (1 - λ_discrete)，其中 λ_discrete 为离散价格导致的有效供给减少系数，需根据商品库存密度估算。

## Evidence

先验知识/题面给定，逻辑校验通过
