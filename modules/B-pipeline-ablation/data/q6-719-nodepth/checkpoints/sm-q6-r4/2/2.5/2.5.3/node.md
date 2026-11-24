# N64: N_add 的优化求解：N_add = ceil((L_p99_current - T_target) / ΔL_per_pop)，其中 ΔL_per_pop 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

N_add 的优化求解：N_add = ceil((L_p99_current - T_target) / ΔL_per_pop)，其中 ΔL_per_pop 为每增加一个 POP 点平均降低的 P99 延迟；ΔL_per_pop 非线性，随 N_pop 增加而递减，需迭代求解满足 L_p99(N_pop + N_add) ≤ T_target 的最小 N_add。

## Corrected Claim

N_add 的优化求解：N_add = ceil((L_p99_current - T_target) / ΔL_per_pop)，其中 ΔL_per_pop 为每增加一个 POP 点平均降低的 P99 延迟；ΔL_per_pop 非线性，随 N_pop 增加而递减，需迭代求解满足 L_p99(N_pop + N_add) ≤ T_target 的最小 N_add。

## Evidence

先验知识/题面给定，逻辑校验通过
