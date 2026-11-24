# N457: 视频主导工作点下的缓存存储容量需求 N_storage_vid = 2,000,000 MB/day * 0.75 * 3 days * 1.3 ≈ 5.85 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N145

## Claim

视频主导工作点下的缓存存储容量需求 N_storage_vid = 2,000,000 MB/day * 0.75 * 3 days * 1.3 ≈ 5.85 TB，虽然总容量低于前两者，但视频对象的长尾特性导致缓存淘汰策略（如 LFU vs LRU）对命中率 H 的敏感性更高，需引入 A/B 测试量化策略差异。

## Corrected Claim

视频主导工作点下的缓存存储容量需求 N_storage_vid = 2,000,000 MB/day * 0.75 * 3 days * 1.3 ≈ 5.85 TB，虽然总容量低于前两者，但视频对象的长尾特性导致缓存淘汰策略（如 LFU vs LRU）对命中率 H 的敏感性更高，需引入 A/B 测试量化策略差异。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 2,000,000 * 0.75 * 3 * 1.3 = 5,850,000 MB = 5.85 TB 准确无误；视频长尾特性导致对缓存策略敏感符合缓存系统基本原理。
