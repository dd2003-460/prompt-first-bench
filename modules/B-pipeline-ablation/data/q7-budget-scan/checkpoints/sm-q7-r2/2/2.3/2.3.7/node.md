# N69: 云存储取回费用（Retrieval）：冷数据400TB若发生1%意外访问（4TB），从IA层取回费用约为$0.01/GB×4000GB=$40，从Glacier

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

云存储取回费用（Retrieval）：冷数据400TB若发生1%意外访问（4TB），从IA层取回费用约为$0.01/GB×4000GB=$40，从Glacier Instant Retrieval取回费用约为$0.025/GB×4000GB=$100，年取回费取决于访问频率假设，典型场景下年取回费约为¥300-1000

## Corrected Claim

云存储取回费用（Retrieval）：冷数据400TB若发生1%意外访问（4TB），从IA层取回费用约为$0.01/GB×4000GB=$40，从Glacier Instant Retrieval取回费用约为$0.025/GB×4000GB=$100，年取回费取决于访问频率假设，典型场景下年取回费约为¥300-1000

## Evidence

先验知识/题面给定，逻辑校验通过：AWS S3 IA取回费$0.01/GB与Glacier Instant Retrieval取回费$0.025/GB符合公开定价标准，计算过程（4000GB * 单价）逻辑自洽，最终人民币估算在合理汇率与波动范围内。
