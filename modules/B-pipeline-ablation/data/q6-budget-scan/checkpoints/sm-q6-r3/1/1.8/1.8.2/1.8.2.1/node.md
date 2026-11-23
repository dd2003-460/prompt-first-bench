# N171: 公有云策略下的回源概率 p_miss_cloud = 1 - H_edge_cloud，其中 H_edge_cloud = 1 - (N_unique_acti

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

公有云策略下的回源概率 p_miss_cloud = 1 - H_edge_cloud，其中 H_edge_cloud = 1 - (N_unique_active_cloud / Cache_Capacity_Objects_cloud)，公有云CDN的POP点更多但单点容量较小，N_unique_active_cloud 通常高于自建，导致 H_edge_cloud 略低

## Corrected Claim

公有云策略下的回源概率 p_miss_cloud = 1 - H_edge_cloud，其中 H_edge_cloud = 1 - (N_unique_active_cloud / Cache_Capacity_Objects_cloud)，公有云CDN的POP点更多但单点容量较小，N_unique_active_cloud 通常高于自建，导致 H_edge_cloud 略低

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

public CDN cache hit rate vs self-hosted edge nodes
