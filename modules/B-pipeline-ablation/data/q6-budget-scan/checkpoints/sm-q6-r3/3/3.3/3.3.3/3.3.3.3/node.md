# N318: 缓存容量限制下的有效命中率修正：实际H_cache = min(H_zipf, C_cache_capacity / (N_hot_objects * s_av

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N107

## Claim

缓存容量限制下的有效命中率修正：实际H_cache = min(H_zipf, C_cache_capacity / (N_hot_objects * s_avg_hot))，其中C_cache_capacity为单POP总缓存容量（如10TB），N_hot_objects为访问前80%流量的对象数，s_avg_hot为热点对象平均大小；若容量不足，H_cache将低于Zipf理论值，需扩容或采用LRU-LFU混合策略。

## Corrected Claim

缓存容量限制下的有效命中率修正：实际H_cache = min(H_zipf, C_cache_capacity / (N_hot_objects * s_avg_hot))，其中C_cache_capacity为单POP总缓存容量（如10TB），N_hot_objects为访问前80%流量的对象数，s_avg_hot为热点对象平均大小；若容量不足，H_cache将低于Zipf理论值，需扩容或采用LRU-LFU混合策略。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cdn cache capacity limit hit rate reduction lru lfu
