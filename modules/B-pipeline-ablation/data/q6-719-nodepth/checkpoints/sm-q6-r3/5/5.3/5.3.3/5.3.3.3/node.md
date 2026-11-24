# N297: 单POP监控与工具成本 C_monitoring_pop = C_monitoring_platform * (1/10) + C_log_storage_po

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N97

## Claim

单POP监控与工具成本 C_monitoring_pop = C_monitoring_platform * (1/10) + C_log_storage_pop，其中 C_monitoring_platform 为集中式监控平台月费（¥10,000），C_log_storage_pop 为单POP日志存储与分析成本（¥500-1000/月），计算得 C_monitoring_pop ≈ ¥1,500-2,000/月。

## Corrected Claim

单POP监控与工具成本 C_monitoring_pop = C_monitoring_platform * (1/10) + C_log_storage_pop，其中 C_monitoring_platform 为集中式监控平台月费（¥10,000），C_log_storage_pop 为单POP日志存储与分析成本（¥500-1000/月），计算得 C_monitoring_pop ≈ ¥1,500-2,000/月。

## Evidence

先验知识/题面给定，逻辑校验通过：10000 * 0.1 + 500 = 1500，10000 * 0.1 + 1000 = 2000，计算无误且量级合理。
