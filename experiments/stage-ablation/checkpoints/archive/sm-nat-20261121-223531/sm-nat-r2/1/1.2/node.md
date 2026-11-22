# N7: 请求热度分布的累积分布函数 F_H(h) = 1 - (h_min/h)^{β-1}，其中 β=0.9，h_min 为最小热度权重（[待核验]，通常归一化为 1

- **status**: verified
- **level**: L2
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

请求热度分布的累积分布函数 F_H(h) = 1 - (h_min/h)^{β-1}，其中 β=0.9，h_min 为最小热度权重（[待核验]，通常归一化为 1 或基于总请求数 50M/100k=500 次/对象/天 的基准）。

## Corrected Claim

请求热度分布的累积分布函数 F_H(h) = 1 - (h_min/h)^{β-1}，其中 β=0.9，h_min 为最小热度权重（[待核验]，通常归一化为 1 或基于总请求数 50M/100k=500 次/对象/天 的基准）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Pareto distribution request frequency beta 0.9 web cache
