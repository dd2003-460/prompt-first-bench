# N657: 阿里云CDN 请求数计费阶梯：目前阿里云标准版请求数计费为固定单价 ¥0.04/万次，无公开阶梯折扣；但企业版或大客户协议可能提供 5%-15% 的谈判折扣，需

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N224, N225, N226

## Claim

阿里云CDN 请求数计费阶梯：目前阿里云标准版请求数计费为固定单价 ¥0.04/万次，无公开阶梯折扣；但企业版或大客户协议可能提供 5%-15% 的谈判折扣，需通过商务渠道确认，公开文档中无自动阶梯机制

## Corrected Claim

阿里云CDN请求数计费通常采用固定单价或资源包模式，公开文档中无自动阶梯折扣机制；具体单价（如¥0.04/万次）需以官方最新定价页为准，企业版可能通过商务渠道获得折扣。

## Evidence

[质询]具体单价数值（¥0.04/万次）属于经验事实，参考来源中未提供该具体数值，且来源[1]主要描述的是流量阶梯计费而非请求数计费，无法直接验证该固定单价的准确性。 | 来源[1]和[3]主要涉及流量和带宽计费，未直接覆盖请求数计费的具体单价；来源[2]提及请求数包但未给出具体价格。逻辑上，CDN请求数通常按固定单价或资源包计费，无自动阶梯符合行业惯例，但具体数值缺乏来源直接支持。

## Search Query

阿里云 CDN 请求数 计费 固定单价 大客户 折扣 协议

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-overview&rut=5607cac578e6a0a2822f10843ed70c58160107634276405ba09db4d9580720b7', 'type': 'ddg', 'title': 'Cdn如何计费-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://www.aliyun.com/price/detail/cdn&rut=7deffc4f1d34859bcb7594b9f5ea62952b3f14c06ecc370a5099c3c282977b06', 'type': 'ddg', 'title': '阿里云定价_CDN价格详情'}
