# N1293: 高码率工作点（s=8.0MB）下，基于 Zipf 分布的缓存命中率 H_video_high = 65%，因仅头部热门对象被覆盖，长尾对象回源率显著增加。

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N441

## Claim

高码率工作点（s=8.0MB）下，基于 Zipf 分布的缓存命中率 H_video_high = 65%，因仅头部热门对象被覆盖，长尾对象回源率显著增加。

## Corrected Claim

高码率工作点（s=8.0MB）下，基于 Zipf 分布的缓存命中率 H_video_high = 65%，因仅头部热门对象被覆盖，长尾对象回源率显著增加。

## Evidence

先验知识/题面给定，逻辑校验通过：高码率下缓存容量受限，仅覆盖头部热门对象，导致长尾回源率增加，命中率65%符合Zipf分布下的典型缓存行为。
