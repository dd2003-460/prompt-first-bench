# N285: 公有云回源网络延迟 L_backhaul_cloud = L_propagation + L_queueing，其中 L_propagation ≈ 20-50

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94

## Claim

公有云回源网络延迟 L_backhaul_cloud = L_propagation + L_queueing，其中 L_propagation ≈ 20-50ms（取决于用户与源站距离），L_queueing ≈ 5-20ms（源站负载），合计 L_backhaul_cloud ≈ 25-70ms。

## Corrected Claim

公有云回源网络延迟 L_backhaul_cloud = L_propagation + L_queueing，其中 L_propagation ≈ 20-50ms（取决于用户与源站距离），L_queueing ≈ 5-20ms（源站负载），合计 L_backhaul_cloud ≈ 25-70ms。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN backhaul latency propagation queueing source server
