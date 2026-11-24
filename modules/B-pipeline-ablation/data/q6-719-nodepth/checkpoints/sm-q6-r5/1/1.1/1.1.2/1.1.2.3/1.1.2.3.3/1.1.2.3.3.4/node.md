# N1294: 低码率工作点（s=2.5MB）下，基于 Zipf 分布的缓存命中率 H_video_low = 90%，因覆盖度更高，长尾对象回源率降低，P99 延迟更优。

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N441

## Claim

低码率工作点（s=2.5MB）下，基于 Zipf 分布的缓存命中率 H_video_low = 90%，因覆盖度更高，长尾对象回源率降低，P99 延迟更优。

## Corrected Claim

低码率工作点（s=2.5MB）下，基于 Zipf 分布的缓存命中率 H_video_low = 90%，因覆盖度更高，长尾对象回源率降低，P99 延迟更优。

## Evidence

先验知识/题面给定，逻辑校验通过：低码率（s=2.5MB）意味着对象更小，在相同缓存容量下可容纳更多对象，从而提升覆盖度；Zipf分布下覆盖度提升直接导致命中率提高（90%合理）及长尾回源率降低，进而优化P99延迟，因果链条符合缓存系统基本原理。
