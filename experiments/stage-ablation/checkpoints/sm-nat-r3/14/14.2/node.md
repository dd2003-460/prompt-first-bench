# N200: 迭代求解 T_avg_residency 的收敛条件：初始假设 T_res0 = C / (S_avg * R_total * (1 - H_base_init

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

迭代求解 T_avg_residency 的收敛条件：初始假设 T_res0 = C / (S_avg * R_total * (1 - H_base_initial))，代入 δ_update 计算 H_eff，再更新 R_miss，直至 T_res 变化小于 1%。

## Corrected Claim

迭代求解 T_avg_residency 的收敛条件：初始假设 T_res0 = C / (S_avg * R_total * (1 - H_base_initial))，代入 δ_update 计算 H_eff，再更新 R_miss，直至 T_res 变化小于 1%。

## Evidence

先验知识/题面给定，逻辑校验通过
