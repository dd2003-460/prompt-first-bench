# N21: 工作负载归一化参数：总对象平均大小 E[S] 的计算公式，基于截断 Pareto 分布 (α=1.1, min=1KB, max=100MB)，E[S] = (

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

工作负载归一化参数：总对象平均大小 E[S] 的计算公式，基于截断 Pareto 分布 (α=1.1, min=1KB, max=100MB)，E[S] = (α * S_min) / (α-1) * (1 - (S_min/S_max)^(α-1)) / (1 - (S_min/S_max)^α)，用于将 128GB 容量转换为可存储对象数量上限 K_max = C / E[S]。

## Corrected Claim

工作负载归一化参数：总对象平均大小 E[S] 的计算公式，基于截断 Pareto 分布 (α=1.1, min=1KB, max=100MB)，E[S] = (α * S_min) / (α-1) * (1 - (S_min/S_max)^(α-1)) / (1 - (S_min/S_max)^α)，用于将 128GB 容量转换为可存储对象数量上限 K_max = C / E[S]。

## Evidence

检索失败: no sources from any channel (all 5 failed)
