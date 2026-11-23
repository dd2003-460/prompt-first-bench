# N82: 边缘缓存命中率 H_edge 的理论上限由工作集大小决定：H_edge_max = 1 - (N_unique_active / Cache_Capacity_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N25

## Claim

边缘缓存命中率 H_edge 的理论上限由工作集大小决定：H_edge_max = 1 - (N_unique_active / Cache_Capacity_Objects)，其中 N_unique_active 为 TTL 窗口内活跃唯一对象数，Cache_Capacity_Objects = 单节点总存储 / s_avg

## Corrected Claim

边缘缓存命中率 H_edge 的理论上限由工作集大小决定：H_edge_max = 1 - (N_unique_active / Cache_Capacity_Objects)，其中 N_unique_active 为 TTL 窗口内活跃唯一对象数，Cache_Capacity_Objects = 单节点总存储 / s_avg

## Evidence

先验知识/题面给定，逻辑校验通过：该公式基于理想缓存模型（无替换开销、无网络延迟影响），在数学上自洽，且量纲正确（对象数/对象数=无量纲比率）。
