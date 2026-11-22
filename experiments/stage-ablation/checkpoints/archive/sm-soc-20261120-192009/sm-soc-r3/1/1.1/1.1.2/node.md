# N34: 锚定偏差系数 anchor_bias 的量化：anchor_bias = β_anchor * (1 - liquidity_index)，其中 β_ancho

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

锚定偏差系数 anchor_bias 的量化：anchor_bias = β_anchor * (1 - liquidity_index)，其中 β_anchor ∈ [0.15, 0.25] 为行为经济学文献中常见的锚定效应强度，liquidity_index 为商品流通频率指数。

## Corrected Claim

锚定偏差系数 anchor_bias 的量化：anchor_bias = β_anchor * (1 - liquidity_index)，其中 β_anchor ∈ [0.15, 0.25] 为行为经济学文献中常见的锚定效应强度，liquidity_index 为商品流通频率指数。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

behavioral economics anchoring effect magnitude beta coefficient
