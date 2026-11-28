# N59: 针对 Nature/Science 子刊 AI 论文中样本量 n 的要求，需基于统计功效（Power）计算：n = (Z_{1-α/2} + Z_{1-β})^

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

针对 Nature/Science 子刊 AI 论文中样本量 n 的要求，需基于统计功效（Power）计算：n = (Z_{1-α/2} + Z_{1-β})^2 * σ^2 / δ^2，其中 δ 为最小可检测效应（MDE），σ 为标准差，通常 Power=0.8 时 n 下限远高于 30。

## Corrected Claim

针对 Nature/Science 子刊 AI 论文中样本量 n 的要求，需基于统计功效（Power）计算：n = (Z_{1-α/2} + Z_{1-β})^2 * σ^2 / δ^2，其中 δ 为最小可检测效应（MDE），σ 为标准差，通常 Power=0.8 时 n 下限远高于 30。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点1和子节点2本质上是对同一公式在不同效应量参数下的重复计算，存在高度冗余；此外，完备性不足，未涵盖AI领域特有的多重比较校正（Multiple Comparisons Correction）、非参检验或基于分类指标（如AUC/F1）的样本量估算等关键方面。）
