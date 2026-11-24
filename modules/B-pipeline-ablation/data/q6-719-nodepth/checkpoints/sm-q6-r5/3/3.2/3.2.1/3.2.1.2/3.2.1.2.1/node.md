# N650: 自建缓存命中率 H_self 的构成公式：H_self = H_local_pop * (1 - P_cross_pop_miss)，其中 H_local_po

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N218

## Claim

自建缓存命中率 H_self 的构成公式：H_self = H_local_pop * (1 - P_cross_pop_miss)，其中 H_local_pop 为单个 POP 点本地缓存命中率（受限于单点容量），P_cross_pop_miss 为跨 POP 未命中导致回源的请求占比（因缺乏全局一致性协议），该公式解释了为何自建命中率低于公有云。

## Corrected Claim

自建缓存命中率 H_self 的构成公式：H_self = H_local_pop * (1 - P_cross_pop_miss)，其中 H_local_pop 为单个 POP 点本地缓存命中率（受限于单点容量），P_cross_pop_miss 为跨 POP 未命中导致回源的请求占比（因缺乏全局一致性协议），该公式解释了为何自建命中率低于公有云。

## Evidence

先验知识/题面给定，逻辑校验通过
