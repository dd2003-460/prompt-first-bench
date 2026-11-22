# N238: P_current 的量化基准值为 P_market，假设卖家在考虑降价时会将价格调整至市场均价以消除信息不对称，因此心理账户效应项变为 λ * (1.25 *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N75

## Claim

P_current 的量化基准值为 P_market，假设卖家在考虑降价时会将价格调整至市场均价以消除信息不对称，因此心理账户效应项变为 λ * (1.25 * P_market - P_market) = 2.25 * 0.25 * P_market ≈ 0.5625 * P_market，需结合 N106 中 H2 的分布计算其方差。

## Corrected Claim

P_current 的量化基准值为 P_market，假设卖家在考虑降价时会将价格调整至市场均价以消除信息不对称，因此心理账户效应项变为 λ * (1.25 * P_market - P_market) = 2.25 * 0.25 * P_market ≈ 0.5625 * P_market，需结合 N106 中 H2 的分布计算其方差。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 2.25 * 0.25 = 0.5625 正确，且符合心理账户效应中参考点（市场均价）与当前价格差异的建模逻辑。
