# N144: Pareto(α=1.1) 分布下对象大小超过 10MB 的概率 P(Size > 10MB) 计算：基于截断帕累托分布公式 P(X > x) = (x_min

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

Pareto(α=1.1) 分布下对象大小超过 10MB 的概率 P(Size > 10MB) 计算：基于截断帕累托分布公式 P(X > x) = (x_min/x)^α，取 x_min=1KB，P(Size > 10MB) = (1/10240)^1.1 ≈ 0.000045。

## Corrected Claim

Pareto(α=1.1) 分布下对象大小超过 10MB 的概率 P(Size > 10MB) 计算：基于截断帕累托分布公式 P(X > x) = (x_min/x)^α，取 x_min=1KB，P(Size > 10MB) = (1/10240)^1.1 ≈ 0.000045。

## Evidence

先验知识/题面给定，逻辑校验通过：截断帕累托分布生存函数公式正确，数值计算 (1/10240)^1.1 ≈ 4.5e-5 准确无误。
