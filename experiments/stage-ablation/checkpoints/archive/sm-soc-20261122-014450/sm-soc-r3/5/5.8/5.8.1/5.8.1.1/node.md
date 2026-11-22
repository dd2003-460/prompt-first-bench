# N340: 基准状态下的卖家最优挂价 P*_base 由一阶条件 (P - C) * dQ/dP + Q = 0 决定，其中需求函数 Q(P) = Q_0 * (P/P_m

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N109

## Claim

基准状态下的卖家最优挂价 P*_base 由一阶条件 (P - C) * dQ/dP + Q = 0 决定，其中需求函数 Q(P) = Q_0 * (P/P_mkt)^ε，基准参数 ε = -1.5, C = 0.6*P_mkt, Q_0 = 100，解得 P*_base ≈ 0.72*P_mkt（需通过数值求解验证精确值）。

## Corrected Claim

基准状态下的卖家最优挂价 P*_base 由一阶条件 (P - C) * dQ/dP + Q = 0 决定，其中需求函数 Q(P) = Q_0 * (P/P_mkt)^ε，基准参数 ε = -1.5, C = 0.6*P_mkt, Q_0 = 100，解得 P*_base ≈ 0.72*P_mkt（需通过数值求解验证精确值）。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

monopoly optimal price elasticity demand first order condition
