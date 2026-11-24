# N223: 跨网/跨域流量溢价：若用户分布广泛，部分请求需跨运营商（如电信用户访问联通节点）或跨地域（如华南用户访问华北节点），可能产生额外跨网费。阿里云 CDN 通常包含

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

跨网/跨域流量溢价：若用户分布广泛，部分请求需跨运营商（如电信用户访问联通节点）或跨地域（如华南用户访问华北节点），可能产生额外跨网费。阿里云 CDN 通常包含基础跨网费，但高并发跨域场景下可能触发额外计费条款。保守估计跨网溢价系数为 1.1-1.2，即 Traffic_Cost 需乘以 1.15，修正后 Traffic_Cost ≈ ¥12,718 × 1.15 ≈ ¥14,626/月。

## Corrected Claim

跨网/跨域流量溢价：若用户分布广泛，部分请求需跨运营商（如电信用户访问联通节点）或跨地域（如华南用户访问华北节点），可能产生额外跨网费。阿里云 CDN 通常包含基础跨网费，但高并发跨域场景下可能触发额外计费条款。保守估计跨网溢价系数为 1.1-1.2，即 Traffic_Cost 需乘以 1.15，修正后 Traffic_Cost ≈ ¥12,718 × 1.15 ≈ ¥14,626/月。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN cross-network traffic surcharge China telecom unicom
