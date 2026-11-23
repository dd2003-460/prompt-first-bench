# N67: 大对象（短视频）对缓存命中率的影响：短视频对象大但数量少，若缓存容量不足，短视频命中率显著低于图片；需分别计算图片命中率 H_img 与视频命中率 H_vid，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

大对象（短视频）对缓存命中率的影响：短视频对象大但数量少，若缓存容量不足，短视频命中率显著低于图片；需分别计算图片命中率 H_img 与视频命中率 H_vid，并加权得到总命中率 H_total = (N_img * H_img + N_vid * H_vid) / (N_img + N_vid)

## Corrected Claim

大对象（短视频）对缓存命中率的影响：短视频对象大但数量少，若缓存容量不足，短视频命中率显著低于图片；需分别计算图片命中率 H_img 与视频命中率 H_vid，并加权得到总命中率 H_total = (N_img * H_img + N_vid * H_vid) / (N_img + N_vid)

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均公式符合数学定义，大对象因缓存容量限制导致命中率低于小对象符合缓存系统基本原理。
