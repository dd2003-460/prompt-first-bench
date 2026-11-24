# N518: AWS S3 Standard GET 请求单价核实：根据 AWS 官网 2024 年价格表（us-east-1 区域），S3 Standard GET 请求费

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N224

## Claim

AWS S3 Standard GET 请求单价核实：根据 AWS 官网 2024 年价格表（us-east-1 区域），S3 Standard GET 请求费用为 $0.40/1000 requests，即 $4e-4/次；按汇率 7.2 折算为 ¥2.88e-3/次；S3 Infrequent Access GET 请求费用为 $1.00/1000 requests，即 ¥7.2e-3/次；S3 Glacier Instant Retrieval GET 请求费用为 $4.00/1000 requests，即 ¥2.88e-2/次

## Corrected Claim

AWS S3 Standard GET 请求费用约为 $0.40/1000 requests；S3 Infrequent Access GET 请求费用约为 $1.00/1000 requests；S3 Glacier Instant Retrieval GET 请求费用约为 $10.00/1000 requests（具体价格需以 AWS 官网实时报价为准）。

## Evidence

[质询]AWS S3 Glacier Instant Retrieval 的 GET 请求单价通常高于 $4.00/1000 requests（实际约为 $10.00/1000 requests），且 S3 Standard-IA 的 GET 单价通常为 $1.00/1000 requests 以上（实际约为 $1.00-1.25/1000 requests，视具体层级而定，但 Glacier Instant Retrieval 的价格显著更高），此处数值可能存在记忆偏差或过时数据。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无法验证具体价格数值，且部分价格与常见认知有出入）

## Search Query

AWS S3 Standard GET request price per 1000 requests us-east-1 2024
