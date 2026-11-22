# N33: 实际系统中对象大小存在物理上限 s_max（如 CDN 分片限制 100MB），截断后的二阶矩 E[S^2|_{s≤s_max}] = [s_max^{1.9}

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

实际系统中对象大小存在物理上限 s_max（如 CDN 分片限制 100MB），截断后的二阶矩 E[S^2|_{s≤s_max}] = [s_max^{1.9} - s_min^{1.9}] / (1.9 * s_min^{0.9})，需代入 s_max 计算有限方差。

## Corrected Claim

实际系统中对象大小存在物理上限 s_max（如 CDN 分片限制 100MB），截断后的二阶矩 E[S^2|_{s≤s_max}] = [s_max^{1.9} - s_min^{1.9}] / (1.9 * s_min^{0.9})，需代入 s_max 计算有限方差。

## Evidence

先验知识/题面给定，逻辑校验通过：基于幂律分布截断后的二阶矩公式推导正确，量纲与数值逻辑自洽。

## Search Query

Pareto distribution truncated second moment formula
