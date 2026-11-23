# N184: 阿里云CDN按量付费阶梯单价具体数值：月流量60TB（60,000GB）对应的阶梯单价需参考阿里云官网实时价格表，通常前10TB单价约为¥0.25/GB，10-

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N57

## Claim

阿里云CDN按量付费阶梯单价具体数值：月流量60TB（60,000GB）对应的阶梯单价需参考阿里云官网实时价格表，通常前10TB单价约为¥0.25/GB，10-50TB约为¥0.20/GB，50TB以上约为¥0.15/GB；月度成本 = 10,000GB*¥0.25 + 40,000GB*¥0.20 + 10,000GB*¥0.15 = ¥2,500 + ¥8,000 + ¥1,500 = ¥12,000/月（假设值，需以官方报价为准）。

## Corrected Claim

阿里云CDN按量付费采用阶梯累进计费模式，具体单价随地域和官方实时价格表变动，通常前10TB单价较高，后续阶梯单价递减；月度成本需根据当月实际流量分布及官方最新单价表计算，示例中的¥12,000/月仅为基于假设单价的估算值。

## Evidence

[质询]具体阶梯单价数值（¥0.25/¥0.20/¥0.15）属于经验事实，且阿里云CDN价格随地域（中国大陆/海外）和具体时间段波动，参考来源仅确认了“阶梯累进计费”的模式，未提供该特定数值组合的直接证据，存在数值过时或地域不匹配的风险。 | 来源[1][2]确认了阿里云CDN采用按流量阶梯累进计费模式，但未提供具体单价数值；该数值为经验事实，逻辑自洽但缺乏来源直接支持，故降级。

## Search Query

阿里云CDN 按量付费 阶梯单价 60TB 月度成本 2024

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://developer.aliyun.com/article/1712489&rut=9ac11fc059ec63ddd1ce104c3b0e7d9ac1b1e8c3823c8a667dafda6ca3e1bda1', 'type': 'ddg', 'title': '2026阿里云cdn 计费全攻略：按流量 / 带宽 / 95 峰值 + 基础服务费 + 增值服务价格表'}
- {'url': 'https://www.aliyun.com/price/detail/cdn&rut=7deffc4f1d34859bcb7594b9f5ea62952b3f14c06ecc370a5099c3c282977b06', 'type': 'ddg', 'title': '阿里云定价_CDN价格详情'}
