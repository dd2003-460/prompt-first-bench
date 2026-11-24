# N652: 阿里云CDN中国内地HTTPS请求单价为 ¥0.04/万次（标准版），该费用独立于流量费，且无最低消费门槛；需确认此价格是否包含HTTPS证书托管费（通常证书费

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N224, N225, N226

## Claim

阿里云CDN中国内地HTTPS请求单价为 ¥0.04/万次（标准版），该费用独立于流量费，且无最低消费门槛；需确认此价格是否包含HTTPS证书托管费（通常证书费另计或包含在高级版中，标准版通常仅收请求费）

## Corrected Claim

阿里云CDN中国内地HTTPS请求单独计费，独立于流量费，支持按量后付费；具体单价及证书费包含情况需以阿里云官网实时报价为准（通常标准版仅收请求费，证书费另计或含在高级版中）。

## Evidence

[质询]具体单价数值（¥0.04/万次）及“无最低消费门槛”、“证书费包含情况”等细节在提供的参考来源摘要中未直接体现，存在数值偏差或政策更新导致的信息滞后风险。 | 来源[1]和[3]证实HTTPS请求单独计费且独立于基础流量费，逻辑自洽；但具体单价¥0.04/万次及证书费细节缺乏直接来源支持，属经验事实，降级处理。

## Search Query

阿里云 CDN 中国内地 HTTPS 请求费 单价 0.04 元 万次 计费详情

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-of-https-requests-for-static-content&rut=b2a9e93598935bbcc4bb8023df740c51e7ee06804c384188e45cda294fd47011', 'type': 'ddg', 'title': '静态https请求数的计费标准及示例-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-overview&rut=5607cac578e6a0a2822f10843ed70c58160107634276405ba09db4d9580720b7', 'type': 'ddg', 'title': 'Cdn如何计费-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://www.aliyun.com/price/detail/cdn&rut=7deffc4f1d34859bcb7594b9f5ea62952b3f14c06ecc370a5099c3c282977b06', 'type': 'ddg', 'title': '阿里云定价_CDN价格详情'}
