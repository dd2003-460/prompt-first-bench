# N191: 期望收益项 (V - P_new) 的不确定性量化：由于 P_new 是随机变量，该项应表示为 E[V - P_new] = V - E[P_new]，其方差 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

期望收益项 (V - P_new) 的不确定性量化：由于 P_new 是随机变量，该项应表示为 E[V - P_new] = V - E[P_new]，其方差 Var(V - P_new) = Var(P_new) 取决于卖家定价策略的离散程度，若 Var(P_new) > (0.1 * V)^2，则风险厌恶买家需增加风险溢价。

## Corrected Claim

期望收益项 (V - P_new) 的不确定性量化：由于 P_new 是随机变量，该项应表示为 E[V - P_new] = V - E[P_new]，其方差 Var(V - P_new) = Var(P_new) 取决于卖家定价策略的离散程度，若 Var(P_new) > (0.1 * V)^2，则风险厌恶买家需增加风险溢价。

## Evidence

先验知识/题面给定，逻辑校验通过：期望的线性性质 E[V-P]=V-E[P] 及方差性质 Var(V-P)=Var(P)（V为常数）符合概率论基本定理；风险溢价与方差正相关的结论符合标准经济学直觉。

## Search Query

variance of future price risk premium consumer utility
