# N69: 共享随机源：卖家收入波动源 R_seller_volatility，其核心驱动因子为成交周期 T 的方差 Var(T) 和价格 P 的方差 Var(P)。在干预

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N15

## Claim

共享随机源：卖家收入波动源 R_seller_volatility，其核心驱动因子为成交周期 T 的方差 Var(T) 和价格 P 的方差 Var(P)。在干预前，高挂价导致 T 较短但 P 方差大；干预后，P 方差减小但 T 方差增大。总风险暴露 Risk_seller = sqrt(Var(P) + Var(T) * (dP/dT)^2)，该随机源决定了卖家净收益的置信区间宽度。

## Corrected Claim

共享随机源：卖家收入波动源 R_seller_volatility，其核心驱动因子为成交周期 T 的方差 Var(T) 和价格 P 的方差 Var(P)。在干预前，高挂价导致 T 较短但 P 方差大；干预后，P 方差减小但 T 方差增大。总风险暴露 Risk_seller = sqrt(Var(P) + Var(T) * (dP/dT)^2)，该随机源决定了卖家净收益的置信区间宽度。

## Evidence

先验知识/题面给定，逻辑校验通过：风险公式符合一阶泰勒展开近似，干预前后方差此消彼长的描述符合经济学直觉（高挂价导致成交慢但价格波动大，干预后价格稳定但成交时间波动可能增大），无内部矛盾。
