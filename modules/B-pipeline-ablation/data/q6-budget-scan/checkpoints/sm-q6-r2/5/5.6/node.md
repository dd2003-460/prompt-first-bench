# N57: 阿里云CDN月度基础成本计算：基于日均下载2TB（月均60TB），按量付费单价¥0.2/GB（含流量包折扣后约¥0.15/GB），月度成本 = 60,000GB

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N14, N15, N16

## Claim

阿里云CDN月度基础成本计算：基于日均下载2TB（月均60TB），按量付费单价¥0.2/GB（含流量包折扣后约¥0.15/GB），月度成本 = 60,000GB * ¥0.15/GB = ¥9,000/月；若使用预付费流量包（1TB包约¥80），60TB需60个包，成本约¥4,800/月，取均值约¥6,900/月。

## Corrected Claim

阿里云CDN月度基础成本计算：基于日均下载2TB（月均60TB），采用按量付费模式。具体成本取决于当前生效的阶梯单价及是否购买流量包，需参照阿里云官网最新价格表计算，此处估算值（约¥4,800-¥9,000/月）仅供参考，实际价格以官方报价为准。

## Evidence

[质询]具体单价（¥0.2/GB, ¥0.15/GB, ¥80/TB）属于经验事实，参考来源仅提供了计费模式（按流量/带宽/95峰值）和阶梯计费的定性描述，未提供具体的2026年最新价格数值，无法直接验证具体金额计算的准确性。 | 来源[1][2][3]确认了阿里云CDN支持按流量计费及阶梯价格机制，与陈述中的计费逻辑一致，但缺乏具体单价数据支持，属于经验事实缺来源直接支持。

## Search Query

Alibaba Cloud CDN pricing per GB 2024

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://developer.aliyun.com/article/1712489&rut=9ac11fc059ec63ddd1ce104c3b0e7d9ac1b1e8c3823c8a667dafda6ca3e1bda1', 'type': 'ddg', 'title': '2026阿里云cdn 计费全攻略：按流量 / 带宽 / 95 峰值 + 基础服务费 + 增值服务价格表'}
- {'url': 'https://help.aliyun.com/zh/cdn/product-overview/billing-rules-of-basic-services&rut=8ac269fc0fd33361b507140bc77f95e7de5882f95004416a424fe1397b02bd86', 'type': 'ddg', 'title': '基础服务计费方式定价规则-cdn-阿里云-cdn (Cdn)-阿里云帮助中心'}
