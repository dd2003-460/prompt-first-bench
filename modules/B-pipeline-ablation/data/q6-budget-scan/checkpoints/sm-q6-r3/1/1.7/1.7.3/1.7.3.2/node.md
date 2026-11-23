# N129: 短视频缓存命中率 H_vid 受对象平均大小 (5MB) 和长尾分布影响，假设每节点缓存 80TB，可容纳约 1600 万个唯一视频对象，由于视频长尾更严重，H

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N38

## Claim

短视频缓存命中率 H_vid 受对象平均大小 (5MB) 和长尾分布影响，假设每节点缓存 80TB，可容纳约 1600 万个唯一视频对象，由于视频长尾更严重，H_vid 估算为 70%。

## Corrected Claim

短视频缓存命中率 H_vid 受对象平均大小 (5MB) 和长尾分布影响，假设每节点缓存 80TB，可容纳约 1600 万个唯一视频对象，由于视频长尾更严重，H_vid 估算为 70%。

## Evidence

先验知识/题面给定，逻辑校验通过：80TB / 5MB = 16,000,000，数值计算准确；短视频长尾分布导致缓存命中率低于静态资源（如图片/JS）符合CDN缓存原理，70%为合理估算值。

## Search Query

video CDN cache hit rate long tail distribution 5MB object size
