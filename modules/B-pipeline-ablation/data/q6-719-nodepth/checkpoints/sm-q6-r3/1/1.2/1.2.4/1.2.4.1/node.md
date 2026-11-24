# N216: L1 缓存未命中率 H_miss_L1 = 0.1，基于公有云 CDN 典型缓存命中率 90%（假设热点内容集中，长尾内容占比 10%），该值决定需要回源到 L

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N55

## Claim

L1 缓存未命中率 H_miss_L1 = 0.1，基于公有云 CDN 典型缓存命中率 90%（假设热点内容集中，长尾内容占比 10%），该值决定需要回源到 L2 的请求比例

## Corrected Claim

L1 缓存未命中率 H_miss_L1 = 0.1，基于公有云 CDN 典型缓存命中率 90%（假设热点内容集中，长尾内容占比 10%），该值决定需要回源到 L2 的请求比例

## Evidence

先验知识/题面给定，逻辑校验通过：命中率90%与未命中率10%互补，量纲与数值逻辑自洽，符合CDN缓存典型经验值。
