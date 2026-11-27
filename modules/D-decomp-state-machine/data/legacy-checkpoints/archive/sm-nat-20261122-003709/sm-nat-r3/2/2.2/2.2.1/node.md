# N44: 计算热对象（Top 10%）的平均大小 S_hot_avg，公式为 S_hot_avg = (∫_{x_min}^{x_q90} x * f_size(x) d

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

计算热对象（Top 10%）的平均大小 S_hot_avg，公式为 S_hot_avg = (∫_{x_min}^{x_q90} x * f_size(x) dx) / P(Size < x_q90)，其中 x_q90 为大小分布的90分位数，需基于 Pareto(α=1.1) 截断分布积分求解。

## Corrected Claim

计算热对象（Top 10%）的平均大小 S_hot_avg，公式为 S_hot_avg = (∫_{x_min}^{x_q90} x * f_size(x) dx) / P(Size < x_q90)，其中 x_q90 为大小分布的90分位数，需基于 Pareto(α=1.1) 截断分布积分求解。

## Evidence

先验知识/题面给定，逻辑校验通过：公式正确表达了条件期望的定义，Pareto分布截断积分在数学上自洽且量纲正确。
