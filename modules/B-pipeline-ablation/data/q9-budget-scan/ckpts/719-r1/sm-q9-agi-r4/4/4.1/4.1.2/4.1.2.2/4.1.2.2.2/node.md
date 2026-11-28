# N568: Pooled_SD 的计算公式为 sqrt(((n1-1)s1² + (n2-1)s2²) / (n1+n2-2))，若两组方差不齐（Levene 检验 p<0

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N203

## Claim

Pooled_SD 的计算公式为 sqrt(((n1-1)s1² + (n2-1)s2²) / (n1+n2-2))，若两组方差不齐（Levene 检验 p<0.05），应改用 Glass's delta (d_glass = (Mean1-Mean2)/SD_control)，此时效应量解释需调整，Glass's delta 在控制组方差较小时会高估效应。

## Corrected Claim

Pooled_SD 的计算公式为 sqrt(((n1-1)s1² + (n2-1)s2²) / (n1+n2-2))，若两组方差不齐（Levene 检验 p<0.05），应改用 Glass's delta (d_glass = (Mean1-Mean2)/SD_control)，此时效应量解释需调整，Glass's delta 在控制组方差较小时会高估效应。

## Evidence

先验知识/题面给定，逻辑校验通过
