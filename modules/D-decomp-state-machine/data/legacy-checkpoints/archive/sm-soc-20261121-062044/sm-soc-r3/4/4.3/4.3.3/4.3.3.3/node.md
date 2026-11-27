# N212: Bootstrap 收敛性诊断：在 p < 0.05 场景下，需验证 bootstrap 分布的稳定性，计算 bootstrap 标准误 SE_boot 与解析

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75

## Claim

Bootstrap 收敛性诊断：在 p < 0.05 场景下，需验证 bootstrap 分布的稳定性，计算 bootstrap 标准误 SE_boot 与解析标准误 SE_analytic 的比值，若 |SE_boot/SE_analytic - 1| > 0.2，则表明样本量不足或分布极度偏斜，需增加 bootstrap 重复次数至 B=5000 或扩大原始样本量，否则置信区间宽度将不可靠，量化指标为比值偏离度 > 20%。

## Corrected Claim

Bootstrap 收敛性诊断：在 p < 0.05 场景下，需验证 bootstrap 分布的稳定性，计算 bootstrap 标准误 SE_boot 与解析标准误 SE_analytic 的比值，若 |SE_boot/SE_analytic - 1| > 0.2，则表明样本量不足或分布极度偏斜，需增加 bootstrap 重复次数至 B=5000 或扩大原始样本量，否则置信区间宽度将不可靠，量化指标为比值偏离度 > 20%。

## Evidence

先验知识/题面给定，逻辑校验通过
