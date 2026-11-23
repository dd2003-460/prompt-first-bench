# N66: 缓存容量需求 C_cache = N_unique_hot * s_avg * R_replica，其中 R_replica 为副本系数（通常 1.2-1.5，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

缓存容量需求 C_cache = N_unique_hot * s_avg * R_replica，其中 R_replica 为副本系数（通常 1.2-1.5，考虑碎片与元数据开销），该值决定边缘节点存储配置成本

## Corrected Claim

缓存容量需求 C_cache = N_unique_hot * s_avg * R_replica，其中 R_replica 为副本系数（通常 1.2-1.5，考虑碎片与元数据开销），该值决定边缘节点存储配置成本

## Evidence

先验知识/题面给定，逻辑校验通过
