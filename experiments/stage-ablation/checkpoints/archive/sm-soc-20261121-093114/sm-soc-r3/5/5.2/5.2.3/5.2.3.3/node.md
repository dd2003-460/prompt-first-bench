# N214: 卖家风险偏好异质性对 λ_loss 的调节：个体 λ_loss 服从截断正态分布 N(λ_mean, σ_λ²) 截断于 [1, 3]，需估计 σ_λ 的标准差

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N76

## Claim

卖家风险偏好异质性对 λ_loss 的调节：个体 λ_loss 服从截断正态分布 N(λ_mean, σ_λ²) 截断于 [1, 3]，需估计 σ_λ 的标准差，若 σ_λ > 0.5，则单一 λ_loss 模型失效，需引入随机系数模型。

## Corrected Claim

卖家风险偏好异质性可能影响 λ_loss 的估计，若个体差异显著（如标准差超过特定阈值），单一固定系数模型可能失效，需考虑随机系数模型；具体阈值需根据数据分布和模型拟合优度确定。

## Evidence

[质询]阈值 0.5 缺乏理论或实证依据，属于任意设定的经验参数；且截断正态分布的具体参数范围 [1, 3] 及失效判据均为特定模型假设，非通用事实。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该陈述包含具体数值阈值和模型假设，无法从第一性原理严格推出）

## Search Query

individual heterogeneity loss aversion coefficient random effects model
