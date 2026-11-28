# N26: 预算分配最优解：设总预算B=$500/月，分配比例w_local=0.6, w_cloud=0.4，最大化目标函数Max(N_exp) s.t. w_local

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

预算分配最优解：设总预算B=$500/月，分配比例w_local=0.6, w_cloud=0.4，最大化目标函数Max(N_exp) s.t. w_local×Cost_local + w_cloud×Cost_cloud ≤ B，且Time_local ≤ T_deadline

## Corrected Claim

预算分配最优解：设总预算B=$500/月，分配比例w_local=0.6, w_cloud=0.4，最大化目标函数Max(N_exp) s.t. w_local×Cost_local + w_cloud×Cost_cloud ≤ B，且Time_local ≤ T_deadline

## Evidence

先验知识/题面给定，逻辑校验通过
