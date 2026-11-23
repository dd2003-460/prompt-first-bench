# N227: Cloudflare 对静态资源（图片/视频）采用按流量计费（$0.02/GB 超出免费额度后），但免费额度通常为 50GB/月；对于 60TB/月 的负载，几

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N78

## Claim

Cloudflare 对静态资源（图片/视频）采用按流量计费（$0.02/GB 超出免费额度后），但免费额度通常为 50GB/月；对于 60TB/月 的负载，几乎全部流量超出免费额度，有效单价接近 $0.02/GB，远低于阿里云国内节点单价（~0.23 元/GB ≈ $0.032/GB），但需注意 Cloudflare 主要节点位于海外，国内访问延迟高且可能受合规限制。

## Corrected Claim

Cloudflare 对静态资源（图片/视频）采用按流量计费（$0.02/GB 超出免费额度后），但免费额度通常为 50GB/月；对于 60TB/月 的负载，几乎全部流量超出免费额度，有效单价接近 $0.02/GB，远低于阿里云国内节点单价（~0.23 元/GB ≈ $0.032/GB），但需注意 Cloudflare 主要节点位于海外，国内访问延迟高且可能受合规限制。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Cloudflare bandwidth pricing static assets $0.02/GB free tier limit
