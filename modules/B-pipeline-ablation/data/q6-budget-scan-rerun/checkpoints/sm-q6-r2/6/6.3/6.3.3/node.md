# N161: 决策边界函数 f(T): 当 T ≥ 200ms 时，公有云 CDN 的 C_total_cloud < C_total_hybrid 且 L_p99_clou

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38, N39, N40

## Claim

决策边界函数 f(T): 当 T ≥ 200ms 时，公有云 CDN 的 C_total_cloud < C_total_hybrid 且 L_p99_cloud ≤ T，故选择公有云；当 150ms ≤ T < 200ms 时，混合策略在满足 L_p99_hybrid ≤ T 前提下成本最优；当 T < 150ms 时，仅自建策略满足 L_p99_self ≤ T，尽管其 C_total_self 最高，但为唯一可行解。

## Corrected Claim

决策边界函数 f(T): 当 T ≥ 200ms 时，公有云 CDN 的 C_total_cloud < C_total_hybrid 且 L_p99_cloud ≤ T，故选择公有云；当 150ms ≤ T < 200ms 时，混合策略在满足 L_p99_hybrid ≤ T 前提下成本最优；当 T < 150ms 时，仅自建策略满足 L_p99_self ≤ T，尽管其 C_total_self 最高，但为唯一可行解。

## Evidence

先验知识/题面给定，逻辑校验通过：决策边界基于成本与延迟约束的单调性推导，区间划分逻辑自洽，无内部矛盾。
