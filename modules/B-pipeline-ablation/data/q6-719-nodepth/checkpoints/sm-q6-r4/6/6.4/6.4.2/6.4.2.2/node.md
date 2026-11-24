# N514: 缓存命中率 H_pop 对对象大小 s 的依赖关系：H_pop 并非恒定 0.9。对于图片 (s_img ~ 1MB)，由于内容重复度高，H_pop_img 可

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N170

## Claim

缓存命中率 H_pop 对对象大小 s 的依赖关系：H_pop 并非恒定 0.9。对于图片 (s_img ~ 1MB)，由于内容重复度高，H_pop_img 可达 0.95；对于短视频 (s_video ~ 10MB)，内容唯一性高，H_pop_video 约为 0.5-0.7。加权命中率 H_pop(s) 需根据 P_img 和 P_video 重新计算，而非简单假设不变。

## Corrected Claim

缓存命中率 H_pop 对对象大小 s 的依赖关系：H_pop 并非恒定 0.9。对于图片 (s_img ~ 1MB)，由于内容重复度高，H_pop_img 可达 0.95；对于短视频 (s_video ~ 10MB)，内容唯一性高，H_pop_video 约为 0.5-0.7。加权命中率 H_pop(s) 需根据 P_img 和 P_video 重新计算，而非简单假设不变。

## Evidence

先验知识/题面给定，逻辑校验通过
