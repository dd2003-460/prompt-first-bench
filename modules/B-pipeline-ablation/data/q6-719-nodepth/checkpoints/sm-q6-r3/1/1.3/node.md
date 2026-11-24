# N8: 缓存命中率 (Cache Hit Rate) 对延迟的影响：P99_Latency = Hit_Rate × T_cache + (1 - Hit_Rate) 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

缓存命中率 (Cache Hit Rate) 对延迟的影响：P99_Latency = Hit_Rate × T_cache + (1 - Hit_Rate) × T_origin，其中 T_cache 为边缘节点处理时间，T_origin 为回源延迟。

## Corrected Claim

缓存命中率 (Cache Hit Rate) 对延迟的影响：P99_Latency = Hit_Rate × T_cache + (1 - Hit_Rate) × T_origin，其中 T_cache 为边缘节点处理时间，T_origin 为回源延迟。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN cache hit rate latency formula
