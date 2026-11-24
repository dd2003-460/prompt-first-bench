# N154: 公有云CDN的P99延迟基线为 L_p99_cloud = 200ms，由 L_edge(50ms) + L_backhaul(100ms) + L_jitte

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35, N36, N37

## Claim

公有云CDN的P99延迟基线为 L_p99_cloud = 200ms，由 L_edge(50ms) + L_backhaul(100ms) + L_jitter(50ms) 构成，其中 L_backhaul 基于5%未命中率和平均回源距离计算。

## Corrected Claim

公有云CDN的P99延迟基线为 L_p99_cloud = 200ms，由 L_edge(50ms) + L_backhaul(100ms) + L_jitter(50ms) 构成，其中 L_backhaul 基于5%未命中率和平均回源距离计算。

## Evidence

先验知识/题面给定，逻辑校验通过
