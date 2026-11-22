# N314: 探索概率对成交周期的传导机制：T_close = T_base / (1 + ε_explore × δ_price_sensitivity)，其中 T_bas

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N107

## Claim

探索概率对成交周期的传导机制：T_close = T_base / (1 + ε_explore × δ_price_sensitivity)，其中 T_base 为无探索加成时的平均成交周期，δ_price_sensitivity 为价格敏感度对探索行为的放大系数（假设 δ=0.3）；需量化 ε_explore 从 0.05 升至 0.2 时 T_close 的缩短幅度。

## Corrected Claim

探索概率对成交周期的传导机制：T_close = T_base / (1 + ε_explore × δ_price_sensitivity)，其中 T_base 为无探索加成时的平均成交周期，δ_price_sensitivity 为价格敏感度对探索行为的放大系数（假设 δ=0.3）；需量化 ε_explore 从 0.05 升至 0.2 时 T_close 的缩短幅度。

## Evidence

先验知识/题面给定，逻辑校验通过
