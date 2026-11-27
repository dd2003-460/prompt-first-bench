# N207: 卖家效用函数 U_seller 的随机投影：U_seller = (P - C_holding) * (Q(P) + ε_Q)，其中 ε_Q 为共享随机源，导致

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N56

## Claim

卖家效用函数 U_seller 的随机投影：U_seller = (P - C_holding) * (Q(P) + ε_Q)，其中 ε_Q 为共享随机源，导致 U_seller 的期望值 E[U_seller] = (P - C_holding) * Q(P)，但方差 Var[U_seller] = (P - C_holding)² * σ_Q²。

## Corrected Claim

卖家效用函数 U_seller 的随机投影：U_seller = (P - C_holding) * (Q(P) + ε_Q)，其中 ε_Q 为共享随机源，导致 U_seller 的期望值 E[U_seller] = (P - C_holding) * Q(P)，但方差 Var[U_seller] = (P - C_holding)² * σ_Q²。

## Evidence

先验知识/题面给定，逻辑校验通过：基于期望的线性性质 E[a(X+ε)] = aE[X] 和方差性质 Var(a(X+ε)) = a²Var(X)，推导完全自洽。

## Search Query

seller utility function stochastic projection variance
