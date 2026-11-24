# N94: 全公有云策略 P99 延迟 L_p99_cloud = L_edge_cloud + L_backhaul_cloud * (1 - H_cloud) + L_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

全公有云策略 P99 延迟 L_p99_cloud = L_edge_cloud + L_backhaul_cloud * (1 - H_cloud) + L_processing，其中 L_edge_cloud ≈ 5-10ms（公有云边缘优化较好），H_cloud 为公有云缓存命中率（通常 90-95%），需验证 L_p99_cloud ≤ 100ms。

## Corrected Claim

全公有云策略 P99 延迟 L_p99_cloud = L_edge_cloud + L_backhaul_cloud * (1 - H_cloud) + L_processing，其中 L_edge_cloud ≈ 5-10ms（公有云边缘优化较好），H_cloud 为公有云缓存命中率（通常 90-95%），需验证 L_p99_cloud ≤ 100ms。

## Evidence

先验知识/题面给定，逻辑校验通过
