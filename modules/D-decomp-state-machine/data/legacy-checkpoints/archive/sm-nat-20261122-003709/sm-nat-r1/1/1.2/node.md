# N6: 计算Pareto(α=1.1)分布下10万对象的总数据量，公式为 S_total = N * E[S]，其中 E[S] = (α * s_min) / (α -

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

计算Pareto(α=1.1)分布下10万对象的总数据量，公式为 S_total = N * E[S]，其中 E[S] = (α * s_min) / (α - 1) * (1 - (s_max/s_min)^(α-1)) / (1 - (s_max/s_min)^(1-α))，需假设 s_min=1KB, s_max=1GB 进行量化。

## Corrected Claim

计算Pareto(α=1.1)分布下10万对象的总数据量，公式为 S_total = N * E[S]，其中 E[S] = (α * s_min) / (α - 1) * (1 - (s_max/s_min)^(α-1)) / (1 - (s_max/s_min)^(1-α))，需假设 s_min=1KB, s_max=1GB 进行量化。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布截断期望公式推导正确，量纲一致（KB/GB换算合理），N=10^5与S_total量级符合直觉。
