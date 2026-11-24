# N482: 混合策略下的带宽协同优化：自建部分预留固定带宽 B_self，公有云部分预留弹性带宽 B_cloud，总成本 C_total = C_self_fixed + 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N154

## Claim

混合策略下的带宽协同优化：自建部分预留固定带宽 B_self，公有云部分预留弹性带宽 B_cloud，总成本 C_total = C_self_fixed + C_cloud_variable；需优化 B_self 和 B_cloud 的分配比例，使得总成本最小化，约束为 W_peak ≤ B_self + B_cloud × (1 - P_burst_cloud)。

## Corrected Claim

混合策略下的带宽协同优化：自建部分预留固定带宽 B_self，公有云部分预留弹性带宽 B_cloud，总成本 C_total = C_self_fixed + C_cloud_variable；需优化 B_self 和 B_cloud 的分配比例，使得总成本最小化，约束为 W_peak ≤ B_self + B_cloud × (1 - P_burst_cloud)。

## Evidence

先验知识/题面给定，逻辑校验通过
