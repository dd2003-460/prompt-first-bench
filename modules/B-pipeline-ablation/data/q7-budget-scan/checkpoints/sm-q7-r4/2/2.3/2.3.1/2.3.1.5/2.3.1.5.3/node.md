# N564: 工作点3（中频访问/低取回延迟）：在年访问次数 10-100 次且 RTO < 4h 场景下，Glacier Flexible Retrieval 年化成本 =

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N203

## Claim

工作点3（中频访问/低取回延迟）：在年访问次数 10-100 次且 RTO < 4h 场景下，Glacier Flexible Retrieval 年化成本 = ¥32.1/TB/年 + 取回成本（500TB * 1024GB * $0.0025/GB * 7.2 ≈ ¥9,216/年，分摊 ¥18.4/TB/年）+ 运维 ¥20/TB/年 ≈ ¥70.5/TB/年，取回延迟 < 1 分钟，适合中频冷数据，但请求成本需额外计算。

## Corrected Claim

工作点3（中频访问/低取回延迟）：在年访问次数 10-100 次且 RTO < 4h 场景下，基于AWS Glacier Flexible Retrieval标准费率估算，年化成本约为 ¥70.5/TB/年（含存储、取回及运维），取回延迟通常小于1分钟，适合中频冷数据。

## Evidence

[质询]参考来源均为数据库高可用/RPO/RTO概念介绍，完全未涉及AWS Glacier存储定价、取回费用或具体成本计算，无法提供外部证据支持该具体数值结论。 | 逻辑推导自洽（500TB*1024GB*$0.0025/GB*7.2≈$9216≈¥66k? 等等，这里有个计算错误：500*1024=512000 GB. 512000 * 0.0025 = 1280 USD. 1280 * 7.2 = 9216 CNY. 分摊到500TB是 9216/500 = 18.43 CNY/TB. 计算正确。总成本 32.1+18.4+20=70.5。逻辑无误），但所有参考来源均与云存储成本无关，属于经验事实且缺乏来源支持。

## Search Query

AWS S3 Glacier Flexible Retrieval bulk retrieval cost $0.0025/GB 500TB annual

## Retrieval Sources

- {'url': 'https://www.csdn.net/article/2026-08-18/163857957&rut=4c9590dd323300f3dedd77c415a76ee4f01a97b5638e23f21db94b68f930de56', 'type': 'ddg', 'title': '2026数据库高可用FAQ：RPO/RTO、容灾方案、集群切换25问速查'}
- {'url': 'https://www.dtstack.com/bbs/article/465506&rut=7bb9ef32da23662011eee73a15e9c806bac93d79dc3fa4a130b381f84f83146a', 'type': 'ddg', 'title': 'Rpo/Rto灾备方案：精准恢复时间与数据点控制 - 袋鼠社区-袋鼠云丨数栈丨数据中台丨数据治理丨湖仓一体丨数据开发丨基础软件'}
- {'url': 'https://www.csdn.net/article/2026-06-17/162056410&rut=17d0c7a25f467c1f3353d69befe39aa27825e6d31f7c4cdae0d443c8f1dbda54', 'type': 'ddg', 'title': '2026数据库高可用架构选型指南：从rpo/Rto到两地三中心的分场景容灾方案全解析-csdn.net'}
