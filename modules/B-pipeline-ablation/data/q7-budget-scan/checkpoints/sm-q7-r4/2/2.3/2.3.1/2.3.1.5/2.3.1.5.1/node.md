# N562: 工作点1（极低访问/高取回延迟）：在年访问次数 < 1 次且 RTO > 24h 场景下，Glacier Flexible Retrieval 年化成本 = ¥

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N203

## Claim

工作点1（极低访问/高取回延迟）：在年访问次数 < 1 次且 RTO > 24h 场景下，Glacier Flexible Retrieval 年化成本 = ¥32.1/TB/年 + 取回成本（500TB * 1024GB * $0.02/GB * 7.2 ≈ ¥73,728/年，分摊 ¥147.5/TB/年）+ 运维 ¥20/TB/年 ≈ ¥199.6/TB/年，取回延迟 3-5 小时，适合归档冷数据。

## Corrected Claim

工作点1（极低访问/高取回延迟）：在年访问次数 < 1 次且 RTO > 24h 场景下，基于估算的 Glacier Flexible Retrieval 年化成本约为 ¥199.6/TB/年（含存储、取回及运维），取回延迟 3-5 小时，适合归档冷数据。（注：具体单价需以官方最新报价为准）

## Evidence

[质询]参考来源仅讨论高可用数据库的RTO/RPO概念，完全未涉及AWS Glacier的具体定价、取回费用或运维成本，无法提供外部证据支持具体的数值计算（如¥32.1/TB/年、¥73,728/年等）。 | 逻辑校验通过：500TB * 1024GB * $0.02/GB * 7.2 ≈ 73,728元，分摊至500TB为147.456元/TB，加上存储费32.1元和运维费20元，总计约199.6元/TB/年，算术无误。但根据经验事实排除条款，具体价格属于经验事实，且参考来源[1][2]与云存储定价无关，缺乏直接来源支持，故降级。

## Search Query

AWS S3 Glacier Flexible Retrieval retrieval cost $0.02/GB 500TB annual

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2030300481931720246&rut=12f16c531c75a7d56a7a927d6e03e3c63b96a5b790ac5788a8e5f464f050cc29', 'type': 'ddg', 'title': '高可用数据库：Rto、Rpo与架构选型，一篇讲透 - 知乎'}
- {'url': 'https://www.toutiao.com/article/7631474653869097508/&rut=bdd6dfb68afce3c718cbea8ec232b94314c33a2d897aef121b77100160f1e7c9', 'type': 'ddg', 'title': '高可用数据库：Rto、Rpo与架构选型，一篇讲透 - 今日头条'}
