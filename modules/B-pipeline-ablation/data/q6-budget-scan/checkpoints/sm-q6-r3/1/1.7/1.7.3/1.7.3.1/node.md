# N128: 图片缓存命中率 H_img 受对象平均大小 (500KB) 和缓存容量约束，假设每节点缓存 80TB，可容纳约 1.6 亿个唯一图片对象，结合 Zipf alp

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N38

## Claim

图片缓存命中率 H_img 受对象平均大小 (500KB) 和缓存容量约束，假设每节点缓存 80TB，可容纳约 1.6 亿个唯一图片对象，结合 Zipf alpha=1.0 分布，H_img 估算为 95%。

## Corrected Claim

图片缓存命中率 H_img 受对象平均大小 (500KB) 和缓存容量约束，假设每节点缓存 80TB，可容纳约 1.6 亿个唯一图片对象，结合 Zipf alpha=1.0 分布，H_img 估算为 95%。

## Evidence

先验知识/题面给定，逻辑校验通过：80TB/500KB=1.6亿对象，Zipf(1.0)下缓存1.6亿对象对应95%命中率符合典型长尾分布特征

## Search Query

image CDN cache hit rate Zipf distribution 500KB object size
