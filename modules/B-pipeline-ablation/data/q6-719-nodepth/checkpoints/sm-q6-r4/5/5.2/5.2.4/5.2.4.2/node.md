# N284: 公有云缓存命中率 H_cloud = f(Object_Size, Popularity, TTL)，对于图片+短视频混合负载，H_cloud ≈ 90-95%

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N94

## Claim

公有云缓存命中率 H_cloud = f(Object_Size, Popularity, TTL)，对于图片+短视频混合负载，H_cloud ≈ 90-95%（基于阿里云/Cloudflare公开数据），需验证在 2TB/天流量下的实际值。

## Corrected Claim

公有云缓存命中率 H_cloud 受 Object_Size, Popularity, TTL 影响，在优化良好的图片+短视频混合负载下，典型值通常在 80-95% 区间，具体数值需根据实际流量特征（如 2TB/天）及缓存策略进行实测验证。

## Evidence

[质询]该陈述将具体的经验数值（90-95%）归因于“阿里云/Cloudflare公开数据”，但缺乏具体报告或数据集的引用，且不同负载特征（如对象大小分布、TTL策略）下命中率波动极大，直接断言该区间可能混淆了特定优化场景与通用混合负载的平均值。 | source=knowledge，逻辑自洽（缓存命中率受对象大小、流行度、TTL影响符合基本缓存原理，90-95%在优化良好的公有云CDN场景下属于合理量级），但作为经验事实，缺乏具体来源直接支持该精确区间，故降级。

## Search Query

CDN cache hit ratio image video workload 90-95%
