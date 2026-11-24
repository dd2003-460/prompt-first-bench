# N216: 公有云CDN预热的流量费用与免费额度：阿里云 CDN 预热流量按下行流量计费，单价 ¥0.24/GB，日均预热 2GB，月度成本 = 2 × 30 × 0.24

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N80

## Claim

公有云CDN预热的流量费用与免费额度：阿里云 CDN 预热流量按下行流量计费，单价 ¥0.24/GB，日均预热 2GB，月度成本 = 2 × 30 × 0.24 = ¥14.4，年度 ¥172.8；Cloudflare 预热流量通常包含在 Enterprise 套餐中，超出部分按 $0.06/GB 计费，日均 2GB，月度成本 = 2 × 30 × 0.06 = $3.6（约 ¥25.92），年度 ¥311.04

## Corrected Claim

阿里云CDN预热流量按下行流量计费，具体单价需参考实时价格表（来源未提供确切数值）；Cloudflare预热流量通常包含在套餐中，具体超额计费标准需查阅官方文档，无法仅凭现有来源确认$0.06/GB的单价。

## Evidence

[质询]阿里云CDN预热流量单价¥0.24/GB及Cloudflare预热流量计费模式（包含在Enterprise中/超出$0.06/GB）均为具体经验参数，参考来源仅提供了计费模式概述（按流量/带宽），未提供具体单价数值，且Cloudflare预热通常不单独按GB计费而是包含在套餐或按请求数/带宽计费，具体数值缺乏来源直接支持。 | 来源[1][2][3]确认了阿里云CDN按下行流量计费的逻辑，但未提供¥0.24/GB的具体单价；Cloudflare部分无相关来源支持，属于经验事实且缺来源直接支持，故降级。

## Search Query

alibaba cloud cdn prefetch traffic cost cloudflare enterprise prefetch pricing

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-overview&rut=5607cac578e6a0a2822f10843ed70c58160107634276405ba09db4d9580720b7', 'type': 'ddg', 'title': 'Cdn如何计费-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://www.aliyun.com/price/detail/cdn&rut=7deffc4f1d34859bcb7594b9f5ea62952b3f14c06ecc370a5099c3c282977b06', 'type': 'ddg', 'title': '阿里云定价_CDN价格详情'}
- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
