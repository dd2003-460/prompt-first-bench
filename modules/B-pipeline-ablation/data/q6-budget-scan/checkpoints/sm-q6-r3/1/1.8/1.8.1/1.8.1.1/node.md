# N167: 自建策略下的回源概率 p_miss_self = 1 - H_edge_self，其中 H_edge_self = 1 - (N_unique_active_s

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

自建策略下的回源概率 p_miss_self = 1 - H_edge_self，其中 H_edge_self = 1 - (N_unique_active_self / Cache_Capacity_Objects_self)，N_unique_active_self 为自建POP点TTL窗口内活跃唯一对象数，通常低于公有云因覆盖用户更集中

## Corrected Claim

自建策略下的回源概率 p_miss_self = 1 - H_edge_self，其中 H_edge_self = 1 - (N_unique_active_self / Cache_Capacity_Objects_self)，N_unique_active_self 为自建POP点TTL窗口内活跃唯一对象数，通常低于公有云因覆盖用户更集中

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义符合缓存命中率基本逻辑（1-活跃对象占比），且自建POP用户集中导致活跃对象数低于公有云的推断符合业务直觉。

## Search Query

edge cache hit rate calculation unique active objects
