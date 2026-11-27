# N193: 折损系数 δ 对更新率 u 的二阶修正项系数 k_2 在 u=0.01/day 时约为 0.002，导致实际折损略高于线性预测值 1.02%（即 δ ≈ 0.9

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N73

## Claim

折损系数 δ 对更新率 u 的二阶修正项系数 k_2 在 u=0.01/day 时约为 0.002，导致实际折损略高于线性预测值 1.02%（即 δ ≈ 0.9898 而非 0.9900）

## Corrected Claim

折损系数 δ 对更新率 u 存在二阶修正项，导致实际折损略高于线性预测值，具体系数 k_2 及修正幅度需依据特定模型或实验数据确定。

## Evidence

[质询]该陈述包含具体的经验数值（k_2 ≈ 0.002, δ ≈ 0.9898），属于特定模型或经验拟合结果，无法从第一性原理或通用数学公理中严格推导得出，且缺乏来源支持其具体数值量级。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且数值非第一性原理可推导）

## Search Query

CDN cache hit rate second order correction update rate u=0.01
