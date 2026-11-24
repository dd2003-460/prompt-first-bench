# N292: Security_Headcount_Sensitivity = f(Attack_Frequency, Monitoring_Coverage)，当 Atta

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N101

## Claim

Security_Headcount_Sensitivity = f(Attack_Frequency, Monitoring_Coverage)，当 Attack_Frequency > 0.1/月 或 Monitoring_Coverage = 24x7 时，Headcount 从 1 跳变至 3，成本函数呈阶梯状非线性，而非线性插值，因此敏感性分析需采用离散情景模拟。

## Corrected Claim

Security_Headcount_Sensitivity = f(Attack_Frequency, Monitoring_Coverage)，当 Attack_Frequency > 0.1/月 或 Monitoring_Coverage = 24x7 时，Headcount 从 1 跳变至 3，成本函数呈阶梯状非线性，而非线性插值，因此敏感性分析需采用离散情景模拟。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

security team sizing model based on incident frequency
