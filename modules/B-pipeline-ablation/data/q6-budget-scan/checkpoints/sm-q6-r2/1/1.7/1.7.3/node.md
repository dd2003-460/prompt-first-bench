# N38: 缓存未命中率 m = 1 - H，其中 H 为缓存命中率；对于图片+短视频混合负载，由于短视频对象大且长尾，整体 H 通常低于纯图片场景，需按对象类型加权计算：

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

缓存未命中率 m = 1 - H，其中 H 为缓存命中率；对于图片+短视频混合负载，由于短视频对象大且长尾，整体 H 通常低于纯图片场景，需按对象类型加权计算：H_total = (N_img * H_img + N_vid * H_vid) / N_total。

## Corrected Claim

缓存未命中率 m = 1 - H，其中 H 为缓存命中率；对于图片+短视频混合负载，由于短视频对象大且长尾，整体 H 通常低于纯图片场景，需按对象类型加权计算：H_total = (N_img * H_img + N_vid * H_vid) / N_total。

## Evidence

先验知识/题面给定，逻辑校验通过：命中率定义及加权平均公式符合数学逻辑，且短视频因对象大、长尾分布导致命中率低于图片符合缓存系统基本直觉。

## Search Query

CDN cache hit rate video vs image weighted average
