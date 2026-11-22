# N122: 在假设 ρ=0（独立）的工作点下，E[S|Requested] = E[S] * E[P] / E[P] = E[S]，需数值积分截断Pareto(α=1.1)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

在假设 ρ=0（独立）的工作点下，E[S|Requested] = E[S] * E[P] / E[P] = E[S]，需数值积分截断Pareto(α=1.1)计算E[S]，TotalByteRequest = 5000万 * E[S]

## Corrected Claim

在假设 ρ=0（独立）的工作点下，E[S|Requested] = E[S] * E[P] / E[P] = E[S]，需数值积分截断Pareto(α=1.1)计算E[S]，TotalByteRequest = 5000万 * E[S]

## Evidence

先验知识/题面给定，逻辑校验通过：在独立假设下条件期望等于无条件期望，且Pareto分布期望公式及数值积分截断处理符合数学定义。
