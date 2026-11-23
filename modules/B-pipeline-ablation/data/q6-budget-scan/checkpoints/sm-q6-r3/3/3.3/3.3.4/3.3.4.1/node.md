# N223: 公有云 CDN 计费口径确认：阿里云/Cloudflare 的流量计费仅包含边缘节点到用户的下行流量（Edge Egress），不包含回源流量（Origin F

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76

## Claim

公有云 CDN 计费口径确认：阿里云/Cloudflare 的流量计费仅包含边缘节点到用户的下行流量（Edge Egress），不包含回源流量（Origin Fetch）；回源流量通常按源站出口带宽计费或包含在基础资源包中，不计入 CDN 流量包成本。

## Corrected Claim

公有云 CDN 计费口径确认：阿里云/Cloudflare 的流量计费仅包含边缘节点到用户的下行流量（Edge Egress），不包含回源流量（Origin Fetch）；回源流量通常按源站出口带宽计费或包含在基础资源包中，不计入 CDN 流量包成本。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Alibaba Cloud CDN billing scope origin fetch traffic vs edge egress
