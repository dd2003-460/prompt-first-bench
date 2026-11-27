# N218: 直接效用项投影 Direct_U 的方差 Var(Direct_U)：Var((V_true - P_ask*)·q) = Var(V_true)·E[q]² 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N64

## Claim

直接效用项投影 Direct_U 的方差 Var(Direct_U)：Var((V_true - P_ask*)·q) = Var(V_true)·E[q]² + (μ_V - P_ask*)²·Var(q) + 2Cov(V_true, q)·(μ_V - P_ask*)·E[q]，其中 Cov(V_true, q) 反映高价值商品是否伴随更高购买意图。

## Corrected Claim

直接效用项投影 Direct_U 的方差 Var(Direct_U)：Var((V_true - P_ask*)·q) = Var(V_true)·E[q]² + (μ_V - P_ask*)²·Var(q) + 2Cov(V_true, q)·(μ_V - P_ask*)·E[q]，其中 Cov(V_true, q) 反映高价值商品是否伴随更高购买意图。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式严格遵循方差分解恒等式 Var(XY) = E[X]²Var(Y) + E[Y]²Var(X) + 2Cov(X,Y)E[X]E[Y]，其中 X=V_true, Y=q，且 E[V_true]=μ_V，推导无误。

## Search Query

variance of utility in stochastic pricing model
