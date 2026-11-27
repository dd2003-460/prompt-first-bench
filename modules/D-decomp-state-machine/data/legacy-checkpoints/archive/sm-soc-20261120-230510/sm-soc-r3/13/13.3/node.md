# N323: 震荡幅度 σ_seller 的确定机制：σ_seller = √(Var(ε_seller_feedback) + Var(ε_market_shock))，其

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N114

## Claim

震荡幅度 σ_seller 的确定机制：σ_seller = √(Var(ε_seller_feedback) + Var(ε_market_shock))，其中 Var(ε_seller_feedback) 为卖家对历史咨询/成交数据的误读方差，Var(ε_market_shock) 为外部市场波动（如节假日）引入的噪声方差。

## Corrected Claim

震荡幅度 σ_seller 的确定机制：σ_seller = √(Var(ε_seller_feedback) + Var(ε_market_shock))，其中 Var(ε_seller_feedback) 为卖家对历史咨询/成交数据的误读方差，Var(ε_market_shock) 为外部市场波动（如节假日）引入的噪声方差。

## Evidence

先验知识/题面给定，逻辑校验通过：方差的可加性在独立噪声源假设下成立，量纲一致，符合随机过程基本定义。
