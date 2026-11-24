# N226: 公有云 CDN 请求数计费的计费周期通常为自然月，且存在阶梯定价机制：当单月请求量超过 10 亿次时，部分云厂商（如腾讯云/阿里云）可能提供 5%-10% 的折

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N67

## Claim

公有云 CDN 请求数计费的计费周期通常为自然月，且存在阶梯定价机制：当单月请求量超过 10 亿次时，部分云厂商（如腾讯云/阿里云）可能提供 5%-10% 的折扣，需将 30 亿次/月的请求量代入阶梯价格表计算实际单价，而非固定 ¥0.04/万次 [时效待核]

## Corrected Claim

公有云 CDN 请求数计费通常以自然月为周期，并采用阶梯定价机制。当单月请求量达到一定规模（如10亿次以上）时，单价会随阶梯降低，具体折扣幅度需参照各云厂商（如腾讯云/阿里云）的最新价格表，而非固定单价。

## Evidence

[质询]具体折扣比例（5%-10%）及触发阈值（10亿次）属于特定厂商的商业政策细节，参考来源仅证实了“阶梯定价”和“自然月”机制，未提供具体的折扣数值，存在经验事实缺乏直接来源支持的风险。 | 来源[1][2][3]直接支持“自然月”计费周期和“阶梯定价”机制，但未直接证实具体的5%-10%折扣数值，属于间接支持/部分支持。

## Search Query

Alibaba Cloud CDN request cost tiered pricing discount for high volume 1 billion requests

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/article/1708278&rut=2ddc55f04c3ee490ae5b44019f150c2428eac2400670b83d41207aae16acf9e2', 'type': 'ddg', 'title': '2026最新阿里云cdn收费标准：不同计费模式价格表（基础服务费和增值服务费用整理）-阿里云开发者社区'}
- {'url': 'https://developer.aliyun.com/article/1712324&rut=d8565d970a3a9aca50dcc1aea6197e5d759235d1f16a243bf38b555228e803a3', 'type': 'ddg', 'title': '2026阿里云cdn收费全揭秘!3种计费模式 + 完整价格表一次看懂'}
- {'url': 'https://cloud.tencent.com/document/product/228/70927&rut=f77ebd6e0c4098e5ec7fdaa0757f1c6e5555c5355c48b2e9815e6d93dfe6407b', 'type': 'ddg', 'title': '内容分发网络 Cdn 计费说明_腾讯云'}
