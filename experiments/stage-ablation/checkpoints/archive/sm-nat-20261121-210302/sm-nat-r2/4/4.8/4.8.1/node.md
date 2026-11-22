# N66: LRU 驱逐周期 T_evict 的估算：T_evict ≈ T_update / (1 + u * N_cap / N_total)，其中 T_update 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

LRU 驱逐周期 T_evict 的估算：T_evict ≈ T_update / (1 + u * N_cap / N_total)，其中 T_update 为全局更新间隔（1 天），N_cap 为缓存对象数，N_total 为总对象数

## Corrected Claim

LRU 驱逐周期 T_evict 的估算：T_evict ≈ T_update / (1 + u * N_cap / N_total)，其中 T_update 为全局更新间隔（1 天），N_cap 为缓存对象数，N_total 为总对象数

## Evidence

先验知识/题面给定，逻辑校验通过
