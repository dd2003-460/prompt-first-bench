# N345: 公有云 CDN 缓存池大小与命中率关系：H_cloud(t) = 1 - (Traffic_back_cloud / Traffic_total)，其中 Tra

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N115

## Claim

公有云 CDN 缓存池大小与命中率关系：H_cloud(t) = 1 - (Traffic_back_cloud / Traffic_total)，其中 Traffic_back_cloud 为公有云回源流量；公有云全局缓存池容量 C_cloud_pool 通常为 TB 级（如 Cloudflare 全球缓存池 > 100PB），其命中率 H_cloud 对局部故障的敏感度低于自建节点，因为单点故障仅影响该区域缓存，而全局缓存池可跨区共享热数据。

## Corrected Claim

公有云 CDN 缓存池大小与命中率关系：H_cloud(t) = 1 - (Traffic_back_cloud / Traffic_total)，其中 Traffic_back_cloud 为公有云回源流量；公有云全局缓存池容量 C_cloud_pool 通常为 TB 级（如 Cloudflare 全球缓存池 > 100PB），其命中率 H_cloud 对局部故障的敏感度低于自建节点，因为单点故障仅影响该区域缓存，而全局缓存池可跨区共享热数据。

## Evidence

先验知识/题面给定，逻辑校验通过：命中率定义符合基本逻辑，公有云CDN全球缓存池TB-PB级容量及跨区共享机制符合行业常识与工程实践。
