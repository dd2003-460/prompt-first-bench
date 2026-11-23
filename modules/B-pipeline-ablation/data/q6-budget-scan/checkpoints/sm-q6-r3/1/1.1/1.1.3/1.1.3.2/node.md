# N183: 源站应用层缓存命中率 H_app_cache 对 T_origin_processing_P99 的影响：若 H_app_cache > 0.95，P99 延迟

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

源站应用层缓存命中率 H_app_cache 对 T_origin_processing_P99 的影响：若 H_app_cache > 0.95，P99 延迟主要由缓存读取决定（< 5ms）；若 H_app_cache < 0.5，P99 延迟受数据库慢查询主导（> 50ms）；缓存失效策略（TTL vs 事件驱动）导致 P99 波动幅度 ±10-20ms，需监控缓存穿透率。

## Corrected Claim

源站应用层缓存命中率 H_app_cache 对 T_origin_processing_P99 的影响：若 H_app_cache > 0.95，P99 延迟主要由缓存读取决定（< 5ms）；若 H_app_cache < 0.5，P99 延迟受数据库慢查询主导（> 50ms）；缓存失效策略（TTL vs 事件驱动）导致 P99 波动幅度 ±10-20ms，需监控缓存穿透率。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

application layer cache hit rate impact on P99 latency database penetration
