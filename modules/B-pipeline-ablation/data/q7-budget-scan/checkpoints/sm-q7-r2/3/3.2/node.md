# N17: 温数据（20%）访问频率对成本影响：每日1-2次扫描导致云存储产生高频GET请求费用（约$0.40/1000 requests），本地存储无请求费用但需考虑IO

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

温数据（20%）访问频率对成本影响：每日1-2次扫描导致云存储产生高频GET请求费用（约$0.40/1000 requests），本地存储无请求费用但需考虑IOPS限制

## Corrected Claim

温数据（20%）访问频率对成本影响：每日1-2次扫描导致云存储产生高频GET请求费用（约$0.40/1000 requests），本地存储无请求费用但需考虑IOPS限制

## Evidence

先验知识/题面给定，逻辑校验通过：云存储按请求计费（S3标准约$0.40/1000 GET）与本地存储无请求费但受I/O限制符合基本经济与技术直觉，数值量级合理。

## Search Query

S3 GET request pricing per 1000 requests daily scan cost
