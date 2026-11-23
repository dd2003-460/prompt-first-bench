# N12: 缓存命中率 $H$ 决定回源流量比例，回源带宽成本占比为 $(1-H)$；对于媒体平台，静态资源缓存命中率通常在 90%-95% 之间，需根据内容热度分布（Zi

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

缓存命中率 $H$ 决定回源流量比例，回源带宽成本占比为 $(1-H)$；对于媒体平台，静态资源缓存命中率通常在 90%-95% 之间，需根据内容热度分布（Zipf 分布）估算 $H$ 值。

## Corrected Claim

缓存命中率 $H$ 决定回源流量比例，回源带宽成本占比为 $(1-H)$；对于媒体平台，静态资源缓存命中率通常在 90%-95% 之间，需根据内容热度分布（Zipf 分布）估算 $H$ 值。

## Evidence

先验知识/题面给定，逻辑校验通过：缓存命中率H与回源流量比例(1-H)在定义上互补，媒体平台静态资源因内容热度长尾分布（Zipf）通常具有高命中率（90%-95%），符合工程常识与逻辑自洽。

## Search Query

CDN cache hit ratio media content zipf distribution
