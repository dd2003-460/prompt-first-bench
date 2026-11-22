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

父节点级核验通过：正交+完备+无冗余（子节点1负责基于理论上限（CDN限制100MB）的数值计算，子节点2负责基于实际样本极值（350MB）的验证与条件修正。两者逻辑上互补（理论值 vs 实际约束检查），不重复且不矛盾。父节点中的公式推导已由子节点的具体数值代入覆盖，关键方面（计算、验证边界）均已涵盖。）

## Search Query

Pareto distribution truncated second moment formula
