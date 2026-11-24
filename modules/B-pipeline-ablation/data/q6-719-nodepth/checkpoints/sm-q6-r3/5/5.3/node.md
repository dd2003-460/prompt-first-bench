# N35: 公有云CDN的请求单价为 ¥/1000 requests，阿里云和Cloudflare的请求单价差异约为 10-30%，具体值需查询最新价目表。

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

公有云CDN的请求单价为 ¥/1000 requests，阿里云和Cloudflare的请求单价差异约为 10-30%，具体值需查询最新价目表。

## Corrected Claim

公有云CDN中，阿里云对特定请求（如静态HTTPS）按¥/1000 requests计费；Cloudflare也有相应请求计费模式，但两者具体单价差异需查询最新价目表，无法仅凭现有来源确认10-30%的差异范围。

## Evidence

[质询]来源仅覆盖阿里云CDN计费，未提供Cloudflare价格数据，无法验证“差异约为10-30%”这一具体数值范围；且阿里云CDN基础计费主要按流量/带宽，请求数计费通常针对HTTPS等增值服务，直接称“请求单价”可能存在口径混淆。 | 来源[1][2][3]证实阿里云CDN存在请求数计费项（如静态HTTPS请求），但缺乏Cloudflare对比数据及具体价差支持，属于经验事实且缺关键来源支持。

## Search Query

Alibaba Cloud CDN request pricing per 1000 requests Cloudflare request cost

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-overview&rut=5607cac578e6a0a2822f10843ed70c58160107634276405ba09db4d9580720b7', 'type': 'ddg', 'title': 'Cdn如何计费-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-of-https-requests-for-static-content&rut=b2a9e93598935bbcc4bb8023df740c51e7ee06804c384188e45cda294fd47011', 'type': 'ddg', 'title': '静态https请求数的计费标准及示例-cdn (Cdn)-阿里云帮助中心'}
