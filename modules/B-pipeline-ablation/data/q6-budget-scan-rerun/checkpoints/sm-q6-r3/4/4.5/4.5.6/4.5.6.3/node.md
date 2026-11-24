# N233: Cloudflare Free计划无限量DDoS防护但存在速率限制（如单IP每秒请求数限制），C端平台峰值5万QPS下是否触发速率限制及限制阈值，需确认Free

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N86

## Claim

Cloudflare Free计划无限量DDoS防护但存在速率限制（如单IP每秒请求数限制），C端平台峰值5万QPS下是否触发速率限制及限制阈值，需确认Free计划QPS上限

## Corrected Claim

Cloudflare Free计划提供无限量DDoS防护，但具体速率限制阈值（如单IP QPS上限）及在5万QPS峰值下的具体表现需查阅Cloudflare官方最新文档或联系支持确认，当前来源未提供具体数值。

## Evidence

[质询]该陈述包含具体的经验性参数（如“单IP每秒请求数限制”的具体阈值或5万QPS下的具体行为），这些属于Cloudflare Free计划的具体产品规格，无法从第一性原理推导，且参考来源中未提供具体的QPS上限数值或速率限制阈值，仅确认了DDoS防护的可用性。 | 来源[1][3]直接支持“Cloudflare Free计划提供DDoS防护”这一部分，但所有来源均未提及具体的速率限制阈值或5万QPS下的具体表现，属于经验事实且缺乏具体数值支持，故降级。

## Search Query

Cloudflare Free plan rate limit QPS threshold 50000 requests per second

## Retrieval Sources

- {'url': 'https://www.cloudflare.com/zh-cn/application-services/products/ddos-for-web/&rut=299854b37253965560cbc73ee830e0105a4b7c702fee6072aa41ffb019d04dd9', 'type': 'ddg', 'title': 'Cloudflare 提供的免费 DDoS 防护'}
- {'url': 'https://www.cloudflare.com/zh-tw/application-services/products/ddos-for-web/&rut=33a0df256ce54311ed2224dbafa3e06afe309f72181efed71194c22b0297b02e', 'type': 'ddg', 'title': 'Cloudflare 提供的免費 DDoS 防護'}
- {'url': 'https://developers.cloudflare.com/ddos-protection/&rut=9525be8d5f16102a7b5570361eec8470d69703a28c40ab6a93de54c82f3da816', 'type': 'ddg', 'title': 'Overview · Cloudflare DDoS Protection docs'}
