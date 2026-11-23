# N47: 缓存淘汰策略（LRU vs LFU）对命中率的影响：对于突发热点，LFU 优于 LRU；对于平稳负载，LRU 足够；策略选择影响 H 的波动幅度，进而影响 P9

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

缓存淘汰策略（LRU vs LFU）对命中率的影响：对于突发热点，LFU 优于 LRU；对于平稳负载，LRU 足够；策略选择影响 H 的波动幅度，进而影响 P99 延迟的稳定性。

## Corrected Claim

缓存淘汰策略（LRU vs LFU）对命中率的影响：对于突发热点，LFU 优于 LRU；对于平稳负载，LRU 足够；策略选择影响 H 的波动幅度，进而影响 P99 延迟的稳定性。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cache eviction policy LRU LFU hit rate stability
