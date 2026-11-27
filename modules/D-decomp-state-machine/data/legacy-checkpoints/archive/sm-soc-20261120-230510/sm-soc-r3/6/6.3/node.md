# N96: 统一假设的边界条件：当 P_ask > V + 3σ 时，P_silent ≈ 0.005，此时 T_shorten 公式失效，因为市场进入“无交易”区间而非“

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

统一假设的边界条件：当 P_ask > V + 3σ 时，P_silent ≈ 0.005，此时 T_shorten 公式失效，因为市场进入“无交易”区间而非“加速成交”区间，需引入流动性枯竭修正项 δ_liquidity。

## Corrected Claim

统一假设的边界条件：当 P_ask > V + 3σ 时，P_silent ≈ 0.005，此时 T_shorten 公式失效，因为市场进入“无交易”区间而非“加速成交”区间，需引入流动性枯竭修正项 δ_liquidity。

## Evidence

先验知识/题面给定，逻辑校验通过：在极端价格偏离（>3σ）下，市场流动性枯竭导致成交概率趋近于零，原有基于正常流动性的加速成交公式失效，需引入修正项，符合微观市场结构基本逻辑。
