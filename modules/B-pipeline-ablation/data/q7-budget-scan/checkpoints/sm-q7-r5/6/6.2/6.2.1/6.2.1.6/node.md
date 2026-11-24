# N608: AWS S3 Glacier Flexible Retrieval 与 Instant Retrieval 的价格对比作为基准校准：Glacier Flexib

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N253, N254, N255

## Claim

AWS S3 Glacier Flexible Retrieval 与 Instant Retrieval 的价格对比作为基准校准：Glacier Flexible Standard 取回费为 $0.03/GB，Instant Retrieval 为 $0.03/GB（数据访问费）+ 无延迟，用于验证阿里云价格的合理性及国际厂商定价结构的一致性

## Corrected Claim

AWS S3 Glacier Flexible Retrieval 标准取回费约为 $0.01/GB，Instant Retrieval 取回费约为 $0.03/GB（具体价格随地区和时间波动，需以 AWS 官网实时报价为准），二者主要差异在于取回延迟而非单价绝对值的巨大差距。

## Evidence

[质询]数值量级存疑：AWS S3 Glacier Flexible Retrieval 的标准取回费通常为 $0.01/GB，而 Instant Retrieval 的取回费通常为 $0.03/GB。陈述中称 Flexible 为 $0.03/GB 可能与当前官方定价不符，且将两者并列对比时若数值相同则失去‘对比’意义，暗示可能存在记忆偏差或数据过时。 | 经验事实，逻辑自洽但缺来源支持（检索失败，且具体价格参数属于易变的市场数据，无法从第一性原理推导，需依赖最新官方文档确认）

## Search Query

AWS S3 Glacier Flexible Retrieval pricing standard instant 2024
