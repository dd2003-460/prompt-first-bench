# N149: 先验均值 μ_prior 的构成：μ_prior = μ_category_base + η_category * Category_Quality_Index

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N48, N49, N50

## Claim

先验均值 μ_prior 的构成：μ_prior = μ_category_base + η_category * Category_Quality_Index，其中 μ_category_base 为平台该品类历史成交商品的质量评分均值（需从平台数据库提取），η_category 为品类质量敏感度系数（通常 0.5-1.0），决定了买家在未接收特定卖家信号前的基准质量预期。

## Corrected Claim

先验均值 μ_prior 的构成通常建模为 μ_prior = μ_category_base + η_category * Category_Quality_Index，其中 μ_category_base 为平台该品类历史成交商品的质量评分均值，η_category 为品类质量敏感度系数（具体数值需根据平台数据校准，常见范围可能在 0.5-1.0 之间），用于确定买家在未接收特定卖家信号前的基准质量预期。

## Evidence

[质询]该公式属于特定模型假设或经验设定，并非通用的第一性原理或数学公理；η_category 的取值范围（0.5-1.0）及公式结构缺乏普适性理论支持，属于经验事实。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该公式非第一性原理可推导，适用经验事实排除条款）

## Search Query

platform historical average quality score by category second-hand market baseline expectation
