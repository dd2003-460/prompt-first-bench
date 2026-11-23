# N203: s_avg 对缓存容量的影响：Cache_Capacity_Objects = Cache_Size / s_avg，若 s_avg 从 2.4MB 增至 3.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N65

## Claim

s_avg 对缓存容量的影响：Cache_Capacity_Objects = Cache_Size / s_avg，若 s_avg 从 2.4MB 增至 3.05MB，相同缓存容量下可存储对象数减少 21%，直接降低理论命中率上限 H_edge_max。

## Corrected Claim

s_avg 对缓存容量的影响：Cache_Capacity_Objects = Cache_Size / s_avg，若 s_avg 从 2.4MB 增至 3.05MB，相同缓存容量下可存储对象数减少 21%，直接降低理论命中率上限 H_edge_max。

## Evidence

先验知识/题面给定，逻辑校验通过：2.4/3.05 ≈ 0.787，即减少约21.3%，且对象数减少直接导致理论命中率上限降低，符合缓存基本原理。
