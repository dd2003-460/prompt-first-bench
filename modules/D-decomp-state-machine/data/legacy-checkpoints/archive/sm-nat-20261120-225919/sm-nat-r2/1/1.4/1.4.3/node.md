# N37: 在 128GB 容量下，若采用热度排序缓存策略，缓存的对象数量上限 K_max 由累积大小约束 Σ_{i=1}^{K_max} S_i ≤ 128×10^9 决

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

在 128GB 容量下，若采用热度排序缓存策略，缓存的对象数量上限 K_max 由累积大小约束 Σ_{i=1}^{K_max} S_i ≤ 128×10^9 决定，需结合 Pareto 分布的累积求和公式 S_cumulative(k) ≈ S_min * (k^(α)/(α-1)) 反解 k。

## Corrected Claim

在 128GB 容量下，若采用热度排序缓存策略，缓存的对象数量上限 K_max 由累积大小约束 Σ_{i=1}^{K_max} S_i ≤ 128×10^9 决定，需结合 Pareto 分布的累积求和公式 S_cumulative(k) ≈ S_min * (k^(α)/(α-1)) 反解 k。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布累积和公式推导正确，量纲与约束条件自洽
