# N254: 下游投影1：干预前风险暴露 Risk_seller_old。Risk_old = sqrt(Var(P_old) + Var(T_old) * (dP/dT_o

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N69

## Claim

下游投影1：干预前风险暴露 Risk_seller_old。Risk_old = sqrt(Var(P_old) + Var(T_old) * (dP/dT_old)^2)。假设 Var(P_old) = (0.15)^2, Var(T_old) = 5^2, dP/dT_old = -0.02，计算具体数值。

## Corrected Claim

下游投影1：干预前风险暴露 Risk_seller_old。Risk_old = sqrt(Var(P_old) + Var(T_old) * (dP/dT_old)^2)。假设 Var(P_old) = (0.15)^2, Var(T_old) = 5^2, dP/dT_old = -0.02，计算具体数值。

## Evidence

先验知识/题面给定，逻辑校验通过：Risk_old = sqrt(0.15^2 + 5^2 * (-0.02)^2) = sqrt(0.0225 + 25 * 0.0004) = sqrt(0.0225 + 0.01) = sqrt(0.0325) ≈ 0.1803。计算过程符合误差传播公式（一阶近似），数值量级合理。
