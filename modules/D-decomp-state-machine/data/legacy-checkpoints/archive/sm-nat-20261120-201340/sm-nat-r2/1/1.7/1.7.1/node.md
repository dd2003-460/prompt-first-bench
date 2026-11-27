# N47: Pareto(α=1.1) 分布的截断期望值 E[S|S≤s_max] = (α * s_min) / (α - 1) * (1 - (s_min/s_max)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

Pareto(α=1.1) 分布的截断期望值 E[S|S≤s_max] = (α * s_min) / (α - 1) * (1 - (s_min/s_max)^(α-1)) / (1 - (s_min/s_max)^α)，用于计算缓存中对象的平均大小 S_avg，其中 s_max 由容量 C 和对象数 k 隐含决定

## Corrected Claim

Pareto(α=1.1) 分布的截断期望值 E[S|S≤s_max] = (α * s_min) / (α - 1) * (1 - (s_min/s_max)^(α-1)) / (1 - (s_min/s_max)^α)，用于计算缓存中对象的平均大小 S_avg，其中 s_max 由容量 C 和对象数 k 隐含决定

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布截断期望公式推导正确，量纲一致，符合概率论基本性质
