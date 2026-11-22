# N124: 投影2（趋势排除边界）：在 k>7 天滞后窗口内，若 $\rho_{lag}$ 仍显著为正（p<0.05），则表明存在长期市场趋势或季节性因素而非短期算法模仿；

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N40

## Claim

投影2（趋势排除边界）：在 k>7 天滞后窗口内，若 $\rho_{lag}$ 仍显著为正（p<0.05），则表明存在长期市场趋势或季节性因素而非短期算法模仿；需计算长期趋势项 $\mu_{trend}$ 对 $\rho_{lag}$ 的偏导数 $\partial \rho_{lag} / \partial \mu_{trend}$，以量化需扣除多少趋势分量才能将 $\rho_{lag}$ 降至 0 以下。

## Corrected Claim

投影2（趋势排除边界）：在 k>7 天滞后窗口内，若 $\rho_{lag}$ 仍显著为正（p<0.05），则表明存在长期市场趋势或季节性因素而非短期算法模仿；需计算长期趋势项 $\mu_{trend}$ 对 $\rho_{lag}$ 的偏导数 $\partial \rho_{lag} / \partial \mu_{trend}$，以量化需扣除多少趋势分量才能将 $\rho_{lag}$ 降至 0 以下。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述定义了基于滞后相关系数显著性的趋势排除边界及偏导数量化方法，符合时间序列分析与统计推断的基本逻辑，无内部矛盾。
