# N282: S3 数据取回成本（恢复阶段）：若数据存储在 S3 Standard，无取回费；若存储在 S3 Infrequent Access (IA)，取回费 $0.01

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N97

## Claim

S3 数据取回成本（恢复阶段）：若数据存储在 S3 Standard，无取回费；若存储在 S3 Infrequent Access (IA)，取回费 $0.01/GB；若存储在 S3 Glacier，标准取回 $0.01/GB，批量取回 $0.0025/GB。假设 500TB 数据中 80% 冷数据在 Glacier Deep Archive，取回 400TB，批量取回成本 = 400,000GB × $0.0025 = $1,000，折合 ¥7,200。温数据 100TB 在 Standard，无取回费。总取回成本 ¥7,200，远低于请求成本。

## Corrected Claim

S3 数据取回成本（恢复阶段）：若数据存储在 S3 Standard，无取回费；若存储在 S3 Infrequent Access (IA) 或 S3 Glacier 系列，需支付取回费。假设 500TB 数据中 80% 冷数据在 Glacier Deep Archive，取回 400TB，若按批量取回费率计算，成本约为 $1,000（具体费率需参照 AWS 官方最新定价页，此处假设 $0.0025/GB）。温数据 100TB 在 Standard，无取回费。总取回成本约 $1,000（约合人民币 7,200 元，按 7.2 汇率估算），远低于请求成本。

## Evidence

[质询]来源未提供具体的取回费数值（如 $0.0025/GB），且 S3 Glacier Deep Archive 的批量取回价格通常高于标准 Glacier 批量取回（Deep Archive 批量通常为 $0.0025/GB 或更高，取决于具体区域和最新定价，而标准 Glacier 批量可能更低或相同，但需确认具体数值是否匹配 Deep Archive 而非普通 Glacier）。此外，汇率换算（$1,000 = ¥7,200 即 7.2 汇率）属于经验事实，来源未覆盖。 | 逻辑推导成立（400,000GB * $0.0025 = $1,000），但参考来源 [1][2][3] 仅提及存在取回费及存储类定义，未提供具体单价数值，无法直接支持 $0.0025/GB 这一具体经验参数，故降级。

## Search Query

AWS S3 Glacier Deep Archive retrieval pricing per GB 2024

## Retrieval Sources

- {'url': 'https://sevencoloryun.com/blog/aws-s3-pricing-cost-comparison-2026/&rut=6609ebadebc3f4aafca58ad359704169f5453b31ec74842d79716a9f09b776e2', 'type': 'ddg', 'title': 'AWS S3 价格怎么算：存储/请求/流量三笔账+取回费陷阱+比官网便宜的路径 | SevenColorYun'}
- {'url': 'https://docs.aws.amazon.com/zh_cn/AmazonS3/latest/userguide/cost-optimization.html&rut=a626122169c40cdccd3558d401492a55ff2fdb8f0cfc483bb9f54df5b7b0a958', 'type': 'ddg', 'title': '成本优化 - Amazon Simple Storage Service'}
- {'url': 'https://docs.aws.amazon.com/zh_cn/AmazonS3/latest/userguide/disaster-recovery-resiliency.html&rut=cab1738e736c9dcaae7e4c8eba3008373e156ee15d0984f2b68697f7033456e5', 'type': 'ddg', 'title': 'Amazon S3 中的恢复能力 - Amazon Simple Storage Service'}
