# N22: 缓存容量匹配度 C_match = Cache_Size / (s_avg * N_unique_hot)，其中 N_unique_hot 为热点对象数；匹配度

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

缓存容量匹配度 C_match = Cache_Size / (s_avg * N_unique_hot)，其中 N_unique_hot 为热点对象数；匹配度 <1 时命中率显著下降

## Corrected Claim

缓存容量匹配度 C_match = Cache_Size / (s_avg * N_unique_hot)，其中 N_unique_hot 为热点对象数；匹配度 <1 时命中率显著下降

## Evidence

先验知识/题面给定，逻辑校验通过
