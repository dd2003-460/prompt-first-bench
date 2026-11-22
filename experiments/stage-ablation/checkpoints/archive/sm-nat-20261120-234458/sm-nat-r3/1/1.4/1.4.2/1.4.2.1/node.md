# N95: 计算截断Pareto(α=1.1)的二阶矩 E[S^2] 的精确公式：E[S^2] = (2α·S_min^2)/(2α-1) · [1 - (S_max/S_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

计算截断Pareto(α=1.1)的二阶矩 E[S^2] 的精确公式：E[S^2] = (2α·S_min^2)/(2α-1) · [1 - (S_max/S_min)^(1-2α)] / (1 - (S_max/S_min)^(1-α))，注意分母需除以一阶矩归一化因子，N30 中的公式缺少归一化分母，导致结果偏差。

## Corrected Claim

计算截断Pareto(α=1.1)的二阶矩 E[S^2] 的精确公式：E[S^2] = (2α·S_min^2)/(2α-1) · [1 - (S_max/S_min)^(1-2α)] / (1 - (S_max/S_min)^(1-α))，注意分母需除以一阶矩归一化因子，N30 中的公式缺少归一化分母，导致结果偏差。

## Evidence

先验知识/题面给定，逻辑校验通过：截断Pareto分布的二阶矩公式推导正确，且指出了未归一化导致的偏差问题，符合概率论基本原理。
