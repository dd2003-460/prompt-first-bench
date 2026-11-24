# N224: 阿里云CDN标准区域（中国内地）HTTP/HTTPS请求费单价为 ¥0.04/万次，该数值来源于阿里云官方定价页，需确认是否包含HTTPS证书费用及是否有最低消

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N67

## Claim

阿里云CDN标准区域（中国内地）HTTP/HTTPS请求费单价为 ¥0.04/万次，该数值来源于阿里云官方定价页，需确认是否包含HTTPS证书费用及是否有最低消费门槛 [时效待核]

## Corrected Claim

阿里云CDN标准区域（中国内地）HTTP/HTTPS请求费单价需查阅最新官方定价页确认，参考来源未提供具体数值，但确认HTTPS请求通常作为增值服务单独计费。

## Evidence

[质询]参考来源中未包含具体的单价数值（¥0.04/万次），无法直接验证该具体价格点；且来源[1]和[2]均指出HTTPS请求属于增值服务，需确认该单价是否仅指基础HTTP或已包含HTTPS增值费，存在口径混淆风险。 | 来源[1][2][3]确认了阿里云CDN存在HTTPS请求计费项且为增值服务，但未提供具体单价数值，无法直接支持¥0.04/万次这一具体经验事实，故降级。

## Search Query

Alibaba Cloud CDN HTTP request price per 10k requests China region 2024

## Retrieval Sources

- {'url': 'https://www.aliyun.com/price/detail/cdn&rut=7deffc4f1d34859bcb7594b9f5ea62952b3f14c06ecc370a5099c3c282977b06', 'type': 'ddg', 'title': '阿里云定价_CDN价格详情'}
- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-overview&rut=5607cac578e6a0a2822f10843ed70c58160107634276405ba09db4d9580720b7', 'type': 'ddg', 'title': 'Cdn如何计费-cdn (Cdn)-阿里云帮助中心'}
