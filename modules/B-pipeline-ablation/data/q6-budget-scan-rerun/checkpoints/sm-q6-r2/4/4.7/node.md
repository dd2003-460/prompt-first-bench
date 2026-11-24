# N23: 全公有云策略的控制粒度：控制粒度 G_pub 定义为可独立配置的最小单元数量，公有云 CDN 的控制粒度通常为区域级（如按国家/省份配置缓存策略），单区域可配置

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

全公有云策略的控制粒度：控制粒度 G_pub 定义为可独立配置的最小单元数量，公有云 CDN 的控制粒度通常为区域级（如按国家/省份配置缓存策略），单区域可配置参数包括缓存 TTL、回源策略、压缩算法等，控制粒度数值为 N_regions_pub（如阿里云支持 30+ 区域，Cloudflare 支持 200+ 城市），每个区域可独立调整 P99 延迟目标。

## Corrected Claim

全公有云策略的控制粒度：控制粒度 G_pub 定义为可独立配置的最小单元数量，公有云 CDN 的控制粒度通常为区域级（如按国家/省份配置缓存策略），单区域可配置参数包括缓存 TTL、回源策略、压缩算法等，控制粒度数值为 N_regions_pub（如阿里云支持 30+ 区域，Cloudflare 支持 200+ 城市），每个区域可独立调整 P99 延迟目标。

## Evidence

先验知识/题面给定，逻辑校验通过：公有云CDN确实以区域（Region）为基本管理单元，阿里云和Cloudflare的区域/城市数量级符合常识，控制粒度定义为区域级在逻辑上自洽。

## Search Query

public cloud CDN control granularity region level configuration cache TTL origin strategy
