# N619: 单新增 POP 节点对 P99 延迟的边际降低量 ΔL_per_pop(N) 的解析近似：ΔL_per_pop(N) ≈ (R_current / (N_pop

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N204

## Claim

单新增 POP 节点对 P99 延迟的边际降低量 ΔL_per_pop(N) 的解析近似：ΔL_per_pop(N) ≈ (R_current / (N_pop + N)) * (L_prop_avg - L_prop_target) + C_queue_reduction，其中 L_prop_avg 为当前平均传播延迟，L_prop_target 为理想最近节点延迟，C_queue_reduction 为负载分散导致的排队延迟降低量（通常 2-5ms）

## Corrected Claim

单新增 POP 节点对 P99 延迟的边际降低量 ΔL_per_pop(N) 的解析近似：ΔL_per_pop(N) ≈ (R_current / (N_pop + N)) * (L_prop_avg - L_prop_target) + C_queue_reduction，其中 L_prop_avg 为当前平均传播延迟，L_prop_target 为理想最近节点延迟，C_queue_reduction 为负载分散导致的排队延迟降低量（通常 2-5ms）

## Evidence

先验知识/题面给定，逻辑校验通过
