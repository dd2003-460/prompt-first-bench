# N315: 正态近似区间[0.50, 0.70]与精确区间的偏差来源：正态近似基于Wald统计量$Z = \frac{\hat{p}-p_0}{\sqrt{p_0(1-p_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N91

## Claim

正态近似区间[0.50, 0.70]与精确区间的偏差来源：正态近似基于Wald统计量$Z = \frac{\hat{p}-p_0}{\sqrt{p_0(1-p_0)/n}}$，在n=100时边界效应导致覆盖率略低于95%，具体覆盖率误差需通过模拟或Edgeworth展开计算。

## Corrected Claim

正态近似区间[0.50, 0.70]与精确区间的偏差来源：正态近似基于Wald统计量$Z = \frac{\hat{p}-p_0}{\sqrt{p_0(1-p_0)/n}}$，在n=100时边界效应导致覆盖率略低于95%，具体覆盖率误差需通过模拟或Edgeworth展开计算。

## Evidence

先验知识/题面给定，逻辑校验通过：Wald置信区间在小样本（n=100）下确实存在边界效应导致覆盖率低于名义水平，且需通过模拟或Edgeworth展开精确计算误差，符合统计学原理。
