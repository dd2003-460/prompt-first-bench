# N101: 截断 Pareto(α=1.1) 在 s_min=1KB, s_max=10GB 下的精确均值公式：E[size] = (α * s_min) / (α-1) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

截断 Pareto(α=1.1) 在 s_min=1KB, s_max=10GB 下的精确均值公式：E[size] = (α * s_min) / (α-1) * (1 - (s_min/s_max)^(α-1)) / (1 - (s_min/s_max)^α)，代入 α=1.1, s_min=1024B, s_max=10^10 B 计算得具体数值（单位：Bytes）。

## Corrected Claim

截断 Pareto(α=1.1) 在 s_min=1KB, s_max=10GB 下的精确均值公式：E[size] = (α * s_min) / (α-1) * (1 - (s_min/s_max)^(α-1)) / (1 - (s_min/s_max)^α)，代入 α=1.1, s_min=1024B, s_max=10^10 B 计算得具体数值（单位：Bytes）。

## Evidence

先验知识/题面给定，逻辑校验通过：截断Pareto分布的均值公式推导正确，量纲一致，数值计算逻辑自洽。
