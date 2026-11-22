# N429: 模型失效边界条件：当ΔP > 30% * C_ref时，信号破坏效应主导，δ_inquiry_48h不再遵循幂律关系，而应切换为线性衰减模型δ_inquiry_

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N151

## Claim

模型失效边界条件：当ΔP > 30% * C_ref时，信号破坏效应主导，δ_inquiry_48h不再遵循幂律关系，而应切换为线性衰减模型δ_inquiry_48h = -β * ΔP，其中β为线性系数。

## Corrected Claim

模型失效边界条件：当ΔP超过特定阈值（如30% * C_ref）时，信号破坏效应可能主导，δ_inquiry_48h可能不再遵循幂律关系，需考虑切换为线性衰减模型δ_inquiry_48h = -β * ΔP，其中β为线性系数。

## Evidence

[质询]该陈述包含具体的经验性阈值（30% * C_ref）和特定的模型切换逻辑（从幂律切换为线性衰减），这属于经验事实或特定领域模型参数，无法从第一性原理或数学公理中严格推导出来。 | 经验事实，逻辑自洽但缺来源支持
