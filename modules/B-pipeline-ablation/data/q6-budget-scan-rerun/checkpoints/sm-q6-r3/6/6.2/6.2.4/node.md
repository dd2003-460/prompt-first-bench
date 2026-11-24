# N349: 阿里云CDN请求次数费用：按HTTP/HTTPS请求次数计费，单价约¥0.0001/次（1万次/¥1）；日均500万DAU假设人均10次请求，月请求量=500万

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N121, N122, N123

## Claim

阿里云CDN请求次数费用：按HTTP/HTTPS请求次数计费，单价约¥0.0001/次（1万次/¥1）；日均500万DAU假设人均10次请求，月请求量=500万*10*30=15亿次，月度请求费用=15亿*¥0.0001=¥150,000 [时效待核]

## Corrected Claim

阿里云CDN请求次数费用：按HTTP/HTTPS请求次数计费，单价需以官网实时报价为准（参考值约¥0.0001/次）；日均500万DAU假设人均10次请求，月请求量=15亿次，若按¥0.0001/次估算，月度请求费用约为¥150,000。

## Evidence

[质询]单价数值（¥0.0001/次）属于具体经验参数，参考来源仅确认了计费模式（按HTTPS请求数计费），未提供具体单价数值，无法排除价格变动或不同区域/套餐价格差异的可能性。 | 来源[1]和[2]确认阿里云CDN支持按HTTPS请求数计费，逻辑推导（15亿次 * 0.0001元/次 = 15万元）自洽，但具体单价缺乏直接来源支持，属经验事实。

## Search Query

Alibaba Cloud CDN request count pricing per 10000 requests

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-of-https-requests-for-static-content&rut=b2a9e93598935bbcc4bb8023df740c51e7ee06804c384188e45cda294fd47011', 'type': 'ddg', 'title': '静态https请求数的计费标准及示例-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-overview&rut=5607cac578e6a0a2822f10843ed70c58160107634276405ba09db4d9580720b7', 'type': 'ddg', 'title': 'Cdn如何计费-cdn (Cdn)-阿里云帮助中心'}
- {'url': 'https://www.aliyun.com/price/detail/cdn&rut=7deffc4f1d34859bcb7594b9f5ea62952b3f14c06ecc370a5099c3c282977b06', 'type': 'ddg', 'title': '阿里云定价_CDN价格详情'}
