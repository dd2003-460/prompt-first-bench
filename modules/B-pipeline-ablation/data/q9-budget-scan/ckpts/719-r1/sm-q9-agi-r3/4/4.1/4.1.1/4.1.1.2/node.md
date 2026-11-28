# N199: Bonferroni 校正后的有效 p-value 阈值计算式为 p_eff = 0.05 / k；当 k=5 时 p_eff=0.01，当 k=10 时 p_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

Bonferroni 校正后的有效 p-value 阈值计算式为 p_eff = 0.05 / k；当 k=5 时 p_eff=0.01，当 k=10 时 p_eff=0.005，该线性衰减模型假设检验间完全独立，未考虑相关性导致的保守偏差。

## Corrected Claim

Bonferroni 校正后的有效 p-value 阈值计算式为 p_eff = 0.05 / k；当 k=5 时 p_eff=0.01，当 k=10 时 p_eff=0.005，该线性衰减模型假设检验间完全独立，未考虑相关性导致的保守偏差。

## Evidence

先验知识/题面给定，逻辑校验通过：Bonferroni校正公式p_eff=α/k及k=5,10时的数值计算正确，且其基于独立性假设导致保守偏差的特性符合统计学原理。
