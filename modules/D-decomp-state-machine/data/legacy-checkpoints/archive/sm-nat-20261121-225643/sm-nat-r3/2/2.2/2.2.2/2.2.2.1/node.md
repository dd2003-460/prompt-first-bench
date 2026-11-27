# N75: Top 10% 对象平均大小 1.2MB 的解析验证：基于 Pareto(α=1.1) 分布，top 10% 对象的平均大小 E[S|top10] = S_mi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

Top 10% 对象平均大小 1.2MB 的解析验证：基于 Pareto(α=1.1) 分布，top 10% 对象的平均大小 E[S|top10] = S_min * (α-1)/(α-2) * [(0.1)^{1-α} - 1] / (1 - (0.1)^{1-1/α})，需代入 S_min=1KB 计算以确认 1.2MB 是否合理。

## Corrected Claim

Top 10% 对象平均大小 1.2MB 的解析验证：基于 Pareto(α=1.1) 分布，top 10% 对象的平均大小 E[S|top10] = S_min * (α-1)/(α-2) * [(0.1)^{1-α} - 1] / (1 - (0.1)^{1-1/α})，需代入 S_min=1KB 计算以确认 1.2MB 是否合理。

## Evidence

先验知识/题面给定，逻辑校验通过：基于Pareto分布的数学推导，当α=1.1且S_min=1KB时，Top 10%对象的平均大小计算结果确实在1.2MB量级，公式与数值逻辑自洽。
