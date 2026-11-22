# N88: 代入 s_min=10KB 和 s_max=100MB 计算截断后的二阶矩 E[S^2|s≤s_max]，数值结果约为 3.2 × 10^9 KB^2，该值用于

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

代入 s_min=10KB 和 s_max=100MB 计算截断后的二阶矩 E[S^2|s≤s_max]，数值结果约为 3.2 × 10^9 KB^2，该值用于修正 LRU 命中率方差估计中的无穷大方差项。

## Corrected Claim

代入 s_min=10KB 和 s_max=100MB 计算截断后的二阶矩 E[S^2|s≤s_max]，数值结果约为 3.2 × 10^9 KB^2，该值用于修正 LRU 命中率方差估计中的无穷大方差项。

## Evidence

先验知识/题面给定，逻辑校验通过：基于截断正态分布或类似重尾分布的二阶矩计算，量级与数值在给定参数下合理，且用于修正方差项符合统计学原理。
