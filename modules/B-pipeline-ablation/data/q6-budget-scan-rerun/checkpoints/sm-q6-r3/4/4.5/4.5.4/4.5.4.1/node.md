# N226: 阿里云CDN WAF企业版按QPS阶梯计费，峰值5万QPS对应的具体月度单价需查询官网价格表（通常阶梯为：0-5k, 5k-10k, 10k-50k等区间，单价

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N84

## Claim

阿里云CDN WAF企业版按QPS阶梯计费，峰值5万QPS对应的具体月度单价需查询官网价格表（通常阶梯为：0-5k, 5k-10k, 10k-50k等区间，单价随QPS增加递减或递增），需确认50k QPS所在阶梯的精确单价

## Corrected Claim

阿里云CDN WAF企业版通常按QPS阶梯计费，具体月度单价及50k QPS所在阶梯的精确价格需查询阿里云官网最新价格表，参考来源未提供具体数值。

## Evidence

[质询]陈述中关于计费阶梯的具体区间（0-5k, 5k-10k, 10k-50k）及单价变化趋势（递减或递增）属于具体经验参数，参考来源未提供WAF企业版的具体QPS阶梯价格表，无法验证这些具体数值和趋势的准确性，存在口径混淆或数据过时的风险。 | 来源[1]和[2]确认了阿里云CDN包含增值服务（如边缘WAF）且需单独计费，但未提供WAF企业版按QPS阶梯计费的具体价格表或50k QPS对应的精确单价，属于经验事实缺来源支持。

## Search Query

Alibaba Cloud CDN WAF Enterprise QPS pricing 50000 QPS monthly cost

## Retrieval Sources

- {'url': 'https://www.aliyun.com/price/detail/cdn&rut=7deffc4f1d34859bcb7594b9f5ea62952b3f14c06ecc370a5099c3c282977b06', 'type': 'ddg', 'title': '阿里云定价_CDN价格详情'}
- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://www.alibabacloud.com/help/zh/anti-ddos/anti-ddos-pro-and-premium/product-overview/billing-of-the-burstable-qps-feature&rut=0575e4390503f14eda84cf03352f8c9ea44748a019ef05e157222ebf74305435', 'type': 'ddg', 'title': '弹性QPS如何计费 - DDoS 防护 - 阿里云 - Alibaba Cloud'}
