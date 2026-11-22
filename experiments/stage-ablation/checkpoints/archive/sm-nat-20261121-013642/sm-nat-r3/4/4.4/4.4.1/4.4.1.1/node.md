# N190: 线性近似有效性边界：在 λ_u * T_cold < 0.1 条件下，精确值 C_steady = 1 - exp(-λ_u * T_cold) 与线性近似 λ

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N65

## Claim

线性近似有效性边界：在 λ_u * T_cold < 0.1 条件下，精确值 C_steady = 1 - exp(-λ_u * T_cold) 与线性近似 λ_u * T_cold 的相对误差 < 0.5%，其中 λ_u=0.01/day, T_cold<10 days。

## Corrected Claim

线性近似有效性边界：在 λ_u * T_cold < 0.1 条件下，精确值 C_steady = 1 - exp(-λ_u * T_cold) 与线性近似 λ_u * T_cold 的相对误差 < 0.5%，其中 λ_u=0.01/day, T_cold<10 days。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

exponential approximation relative error bound lambda t small values
