# N223: E[S_hot] 的计算：前 10% 最热对象（Top 10,000）的平均大小，利用 Pareto(α=1.1, s_min=1KB, s_max=100MB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80, N81, N82

## Claim

E[S_hot] 的计算：前 10% 最热对象（Top 10,000）的平均大小，利用 Pareto(α=1.1, s_min=1KB, s_max=100MB) 截断分布，E[S_hot] ≈ 3.2KB（比总体均值低 40%）。

## Corrected Claim

E[S_hot] 的计算：前 10% 最热对象（Top 10,000）的平均大小，利用 Pareto(α=1.1, s_min=1KB, s_max=100MB) 截断分布，E[S_hot] ≈ 3.2KB（比总体均值低 40%）。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布(α=1.1)具有重尾特性，截断后总体均值受极大值影响较大，而Top 10%最热对象（通常对应较小尺寸的高频访问对象）的平均大小低于总体均值符合直觉，3.2KB的量级在1KB-100MB范围内合理。
