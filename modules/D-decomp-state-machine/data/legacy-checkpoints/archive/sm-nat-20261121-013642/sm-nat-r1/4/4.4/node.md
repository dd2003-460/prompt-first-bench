# N18: 边界条件：当 λ_u * T_cold << 1 时，C_steady ≈ λ_u * T_cold，惩罚因子 δ ≈ 1 - λ_u * T_cold；当 λ

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

边界条件：当 λ_u * T_cold << 1 时，C_steady ≈ λ_u * T_cold，惩罚因子 δ ≈ 1 - λ_u * T_cold；当 λ_u * T_cold >> 1 时，C_steady → 1，δ → P_hit_cold

## Corrected Claim

边界条件：当 λ_u * T_cold << 1 时，C_steady ≈ λ_u * T_cold，惩罚因子 δ ≈ 1 - λ_u * T_cold；当 λ_u * T_cold >> 1 时，C_steady → 1，δ → P_hit_cold

## Evidence

先验知识/题面给定，逻辑校验通过：基于指数衰减模型，当参数远小于1时泰勒展开近似成立，远大于1时趋于极限值，符合物理/数学直觉。
