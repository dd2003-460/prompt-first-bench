# N30: 共享随机源：偏好噪声的方差分解模型。定义总偏好方差 Var(P) = Var(λ_loss) + Var(α_anchor) + Var(I_asym)，其中各

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N6

## Claim

共享随机源：偏好噪声的方差分解模型。定义总偏好方差 Var(P) = Var(λ_loss) + Var(α_anchor) + Var(I_asym)，其中各分项独立同分布或存在协方差项 Cov(λ, α)。需量化各分项在二手交易场景下的相对贡献占比。

## Corrected Claim

在特定的偏好噪声方差分解模型中，总偏好方差可分解为损失厌恶、锚定效应及不对称性等因素的方差之和及协方差项；各分项在二手交易场景下的具体相对贡献占比需通过实证数据量化，而非由模型定义直接给出。

## Evidence

[质询]该陈述包含具体的数学模型定义（方差分解公式）和特定的变量命名（λ_loss, α_anchor, I_asym），这属于特定研究或理论框架下的经验性/假设性设定，而非通用的第一性原理或数学公理。此外，'各分项独立同分布'这一假设在行为经济学中通常不成立（偏好噪声往往存在相关性），且'需量化...相对贡献占比'是一个任务描述而非已验证的事实结论，缺乏实证数据支持。 | 逻辑上方差分解公式自洽（总方差等于各分项方差加协方差项），但该模型的具体变量定义和独立性假设属于特定理论框架的经验性设定，非通用真理；检索无可用来源，无法验证该特定模型在二手交易场景下的有效性或具体贡献占比，故降级。

## Search Query

preference noise variance decomposition loss aversion anchoring effect empirical estimation
