# N104: 公有云 CDN 阶梯计费单价表：以阿里云 CDN 为例，月度流量 0-10TB 区间单价 ¥0.24/GB，10-50TB 区间 ¥0.21/GB，50-100

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N26

## Claim

公有云 CDN 阶梯计费单价表：以阿里云 CDN 为例，月度流量 0-10TB 区间单价 ¥0.24/GB，10-50TB 区间 ¥0.21/GB，50-100TB 区间 ¥0.18/GB，>100TB 区间 ¥0.15/GB；需根据日均 2TB×30=60TB 基准及波动后的实际月度流量定位阶梯区间，避免使用单一平均单价。

## Corrected Claim

公有云 CDN（如阿里云）通常采用阶梯计费模式，流量越大单价越低。需根据日均流量推算月度总流量（如日均2TB×30=60TB），并依据当月实际累计流量定位对应的阶梯区间进行计费，避免使用单一平均单价。具体单价需查阅阿里云官网最新价格表。

## Evidence

[质询]具体单价数值（如0-10TB区间¥0.24/GB）属于经验事实，且阿里云CDN价格随时间、地域及促销活动频繁变动，参考来源摘要仅提及存在阶梯计费模式，未提供2026年或当前具体的精确单价数值，无法直接验证具体数字的准确性。 | 来源[1][2][3]证实阿里云CDN采用按流量计费且存在阶梯价格机制，逻辑上支持需根据实际月度流量定位阶梯区间以避免单一平均单价的错误；但具体单价数值缺乏来源直接支持，属于经验事实，故降级。

## Search Query

Alibaba Cloud CDN pricing tiers traffic cost per GB 2024

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/article/1712324&rut=d8565d970a3a9aca50dcc1aea6197e5d759235d1f16a243bf38b555228e803a3', 'type': 'ddg', 'title': '2026阿里云cdn收费全揭秘!3种计费模式 + 完整价格表一次看懂'}
- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://docsv4.qingcloud.com/user_guide/network/cdn/billing/price/&rut=5d61c86496841278c91ca524d0b4c5ad19e7808d0663d81deed8f9349d13e860', 'type': 'ddg', 'title': 'Cdn 计费 - 公有云文档中心'}
