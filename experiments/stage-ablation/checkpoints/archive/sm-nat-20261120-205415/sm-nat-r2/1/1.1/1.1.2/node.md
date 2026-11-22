# N29: 总数据量约束方程：N * E[S] = 100,000 * 1MB = 100TB，其中 E[S] = ∫_{x_min}^{B} s * f(s) ds 是截

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N6

## Claim

总数据量约束方程：N * E[S] = 100,000 * 1MB = 100TB，其中 E[S] = ∫_{x_min}^{B} s * f(s) ds 是截断 Pareto 分布的期望值，该方程用于反解截断参数 B

## Corrected Claim

总数据量约束方程：N * E[S] = 100,000 * 1MB = 100GB，其中 E[S] = ∫_{x_min}^{B} s * f(s) ds 是截断 Pareto 分布的期望值，该方程用于反解截断参数 B

## Evidence

先验知识/题面给定，逻辑校验通过：总数据量等于样本数乘以期望文件大小，且截断Pareto分布的期望值定义正确，量纲与数值量级（100,000 * 1MB = 100GB，此处需注意100,000 * 1MB = 100,000 MB = 100 GB，而非100 TB，存在量级错误）
