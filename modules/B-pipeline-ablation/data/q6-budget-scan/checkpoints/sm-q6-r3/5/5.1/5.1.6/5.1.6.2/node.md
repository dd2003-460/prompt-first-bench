# N270: 阿里云 CDN API 调用单价 $P_{api}$ 的准确数值：需区分不同 API 接口（如 RefreshObjectCaches, DescribeDom

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N94, N95, N96

## Claim

阿里云 CDN API 调用单价 $P_{api}$ 的准确数值：需区分不同 API 接口（如 RefreshObjectCaches, DescribeDomainBpsData）的计费标准。通常基础 API 免费或有免费额度，超额部分按次计费。需查证最新价目表中各类 API 的单价（元/次）及免费配额。

## Corrected Claim

阿里云 CDN 计费包含基础费用（流量/带宽）和增值服务费用。关于 API 调用（如 RefreshObjectCaches），通常基础 API 免费或有免费额度，超额部分按次计费，但具体单价和配额需查阅阿里云官方最新 API 计费文档，当前参考来源未提供确切数值。

## Evidence

[质询]参考来源主要涵盖CDN流量/带宽/HTTPS请求等基础及增值服务的计费，未直接提供具体API接口（如RefreshObjectCaches）的单价数值或免费配额细节，存在信息覆盖不全的风险。 | 来源[1][2][3]确认了阿里云CDN存在基础费用和增值服务费用，且计费模式多样，但未直接列出具体API调用的单价（元/次）及免费额度，属于间接支持或信息缺失，无法直接验证具体数值。

## Search Query

Aliyun CDN API pricing per call 2024 free quota

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-overview&rut=5607cac578e6a0a2822f10843ed70c58160107634276405ba09db4d9580720b7', 'type': 'ddg', 'title': 'Cdn如何计费-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://developer.aliyun.com/article/1712324&rut=d8565d970a3a9aca50dcc1aea6197e5d759235d1f16a243bf38b555228e803a3', 'type': 'ddg', 'title': '2026阿里云cdn收费全揭秘!3种计费模式 + 完整价格表一次看懂'}
