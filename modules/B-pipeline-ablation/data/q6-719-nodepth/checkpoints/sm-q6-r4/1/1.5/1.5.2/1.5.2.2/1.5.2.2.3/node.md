# N553: 缓存命中率对P99延迟的修正：在CDN边缘节点，若热门短视频缓存命中率Hit_Rate=95%，则P99 T_processing_vid仅受5%未命中请求影响

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N187

## Claim

缓存命中率对P99延迟的修正：在CDN边缘节点，若热门短视频缓存命中率Hit_Rate=95%，则P99 T_processing_vid仅受5%未命中请求影响，有效P99延迟 = 0.95 × T_cache_hit + 0.05 × T_miss，其中T_cache_hit≈10ms，T_miss为回源转码耗时，从而将P99从秒级拉低至百毫秒级。

## Corrected Claim

缓存命中率对P99延迟的修正：在CDN边缘节点，若热门短视频缓存命中率Hit_Rate=95%，则P99 T_processing_vid仅受5%未命中请求影响，有效P99延迟 = 0.95 × T_cache_hit + 0.05 × T_miss，其中T_cache_hit≈10ms，T_miss为回源转码耗时，从而将P99从秒级拉低至百毫秒级。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均公式在数学上自洽，且95%命中率下将P99从秒级（回源）拉低至百毫秒级（缓存）符合CDN边缘节点的基本工程直觉与量级规律。

## Search Query

CDN cache hit rate P99 latency calculation formula
