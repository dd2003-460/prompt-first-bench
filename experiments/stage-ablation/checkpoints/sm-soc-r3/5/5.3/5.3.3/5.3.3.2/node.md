# N277: 在高噪声/低信噪比工作点 (σ_noise²/Var(P_ask) = 0.4) 下，ε_price 的区间变化导致 η_profit 的 95% CI 宽度扩

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N94

## Claim

在高噪声/低信噪比工作点 (σ_noise²/Var(P_ask) = 0.4) 下，ε_price 的区间变化导致 η_profit 的 95% CI 宽度扩大 40% (从 0.2 至 0.28)，置信度降至 70% 以下，主要归因于异质性偏差 δ_heterogeneity 放大。

## Corrected Claim

在高噪声/低信噪比工作点 (σ_noise²/Var(P_ask) = 0.4) 下，ε_price 的区间变化导致 η_profit 的 95% CI 宽度显著扩大，置信度降低，主要归因于异质性偏差 δ_heterogeneity 放大。

## Evidence

[质询]该陈述包含具体的数值变化（CI宽度从0.2至0.28，扩大40%）和置信度阈值（70%以下），属于特定模型或实验条件下的经验性结果。虽然逻辑上噪声增加导致不确定性扩大是合理的，但具体的数值幅度和置信度下降程度无法仅从第一性原理推导，且缺乏外部来源验证其具体数值是否准确对应于该特定参数设置。 | 逻辑自洽：噪声增加导致估计方差增大，进而导致置信区间变宽和置信度降低，符合统计推断基本原理。但具体数值（40%扩大、70%置信度）为经验事实，无来源支持，故降级。

## Search Query

high noise variance elasticity estimation confidence interval expansion
