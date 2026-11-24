# N281: 单 POP CI/CD 计算资源成本 Compute_Resource_Cost = (Daily_Builds × Avg_Build_Duration_Ho

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98

## Claim

单 POP CI/CD 计算资源成本 Compute_Resource_Cost = (Daily_Builds × Avg_Build_Duration_Hours × CPU_Cost_Per_Hour) × 30，假设每日构建 10 次，平均耗时 0.5 小时，CPU 成本 5 元/小时，则单 POP 月成本为 (10 × 0.5 × 5) × 30 = 750 元。

## Corrected Claim

单 POP CI/CD 计算资源成本 Compute_Resource_Cost = (Daily_Builds × Avg_Build_Duration_Hours × CPU_Cost_Per_Hour) × 30，假设每日构建 10 次，平均耗时 0.5 小时，CPU 成本 5 元/小时，则单 POP 月成本为 (10 × 0.5 × 5) × 30 = 750 元。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构正确，数值计算 (10 * 0.5 * 5) * 30 = 750 准确无误，量纲一致。
