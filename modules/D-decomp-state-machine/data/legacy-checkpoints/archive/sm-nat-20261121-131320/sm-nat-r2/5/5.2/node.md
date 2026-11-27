# N45: Pareto(α=1.1)分布中，对象大小超过阈值 S_th 的累积概率（生存函数）公式为 P(S > S_th) = (x_min/S_th)^α，用于计算被

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

Pareto(α=1.1)分布中，对象大小超过阈值 S_th 的累积概率（生存函数）公式为 P(S > S_th) = (x_min/S_th)^α，用于计算被缓存集合排除的大对象数量占比。

## Corrected Claim

Pareto(α=1.1)分布中，对象大小超过阈值 S_th 的累积概率（生存函数）公式为 P(S > S_th) = (x_min/S_th)^α，用于计算被缓存集合排除的大对象数量占比。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布的标准生存函数公式为 P(X > x) = (x_min/x)^α (x >= x_min)，与陈述一致。
