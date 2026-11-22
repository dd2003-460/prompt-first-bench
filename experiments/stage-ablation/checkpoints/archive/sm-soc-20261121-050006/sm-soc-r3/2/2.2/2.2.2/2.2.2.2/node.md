# N185: 流动性风险溢价 λ_liquidity 的量化公式：λ_liquidity = β_liquidity * σ_illiquidity，其中 β_liquidi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N57, N58, N59

## Claim

流动性风险溢价 λ_liquidity 的量化公式：λ_liquidity = β_liquidity * σ_illiquidity，其中 β_liquidity 为二手市场流动性敏感系数（估计 0.8-1.2），σ_illiquidity 为商品非标准化程度导致的预期变现时间方差（年化等效值 2.0-7.0%）；当商品为高非标（如定制家具）时，σ_illiquidity 取上限，λ_liquidity ≈ 7.0%。

## Corrected Claim

流动性风险溢价 λ_liquidity 的量化公式：λ_liquidity = β_liquidity * σ_illiquidity，其中 β_liquidity 为二手市场流动性敏感系数（估计 0.8-1.2），σ_illiquidity 为商品非标准化程度导致的预期变现时间方差（年化等效值 2.0-7.0%）；当商品为高非标（如定制家具）时，σ_illiquidity 取上限，λ_liquidity ≈ 7.0%。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

second hand market illiquidity premium beta coefficient
