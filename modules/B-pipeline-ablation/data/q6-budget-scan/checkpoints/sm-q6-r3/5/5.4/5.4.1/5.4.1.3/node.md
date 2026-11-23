# N258: 当工作集大小 N_unique_active 超过存储容量 Cache_Capacity_Objects 时，命中率上限 H_edge_max 降至 0，此时需

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

当工作集大小 N_unique_active 超过存储容量 Cache_Capacity_Objects 时，命中率上限 H_edge_max 降至 0，此时需增加存储或缩短TTL，成本增加 ΔC = (N_unique_active - Cache_Capacity_Objects) * s_avg * c_storage

## Corrected Claim

当工作集大小 N_unique_active 超过存储容量 Cache_Capacity_Objects 时，命中率上限 H_edge_max 降至 0，此时需增加存储或缩短TTL，成本增加 ΔC = (N_unique_active - Cache_Capacity_Objects) * s_avg * c_storage

## Evidence

先验知识/题面给定，逻辑校验通过
