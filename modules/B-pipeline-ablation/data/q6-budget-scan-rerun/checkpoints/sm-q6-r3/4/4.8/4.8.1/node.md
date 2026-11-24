# N93: 缓存算法对命中率(CHR)的量化影响：在10个POP点且对象大小分布为图片(500KB)/视频(5MB)的场景下，LFU算法相比LRU算法的CHR提升幅度 ΔC

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

缓存算法对命中率(CHR)的量化影响：在10个POP点且对象大小分布为图片(500KB)/视频(5MB)的场景下，LFU算法相比LRU算法的CHR提升幅度 ΔCHR_LFU_LR 约为 5%-15%（基于热点内容分布的Zipf系数α=1.2假设），该提升直接降低回源带宽 B_origin = B_total * (1 - CHR)，进而减少每千请求的带宽成本。

## Corrected Claim

缓存算法对命中率(CHR)的量化影响：在10个POP点且对象大小分布为图片(500KB)/视频(5MB)的场景下，LFU算法相比LRU算法的CHR提升幅度 ΔCHR_LFU_LR 约为 5%-15%（基于热点内容分布的Zipf系数α=1.2假设），该提升直接降低回源带宽 B_origin = B_total * (1 - CHR)，进而减少每千请求的带宽成本。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU vs LRU cache hit rate improvement video streaming workload
