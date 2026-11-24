# N15: P99 合规约束 T_p99 ≤ T_target，其中 T_target 为业务目标（通常 200-500ms）；若 L_p99 > T_target，需增加

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

P99 合规约束 T_p99 ≤ T_target，其中 T_target 为业务目标（通常 200-500ms）；若 L_p99 > T_target，需增加 POP 点或提升缓存命中率，成本增量 ΔC = C_add_pop * N_add。

## Corrected Claim

P99 合规约束 T_p99 ≤ T_target，其中 T_target 为业务目标（通常 200-500ms）；若 L_p99 > T_target，需增加 POP 点或提升缓存命中率，成本增量 ΔC = C_add_pop * N_add。

## Evidence

先验知识/题面给定，逻辑校验通过
