# N7: 随机偏好噪声σ_noise的量化：σ_noise = sqrt(Var(P_listed | P_market))，在控制锚定效应后，剩余方差中60%来自卖家个

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

随机偏好噪声σ_noise的量化：σ_noise = sqrt(Var(P_listed | P_market))，在控制锚定效应后，剩余方差中60%来自卖家个体风险偏好差异（β_risk ~ N(0.3, 0.1)），40%来自信息不对称导致的估值误差（ε_info ~ N(0, 0.15)）。

## Corrected Claim

随机偏好噪声σ_noise的量化：σ_noise = sqrt(Var(P_listed | P_market))。在控制锚定效应后，剩余方差主要由卖家个体风险偏好差异和信息不对称导致的估值误差两部分构成，具体比例取决于市场微观结构及卖家群体特征，通常需通过实证数据拟合确定。

## Evidence

[质询]该陈述包含具体的经验性参数（60%/40%的方差分解比例、β_risk和ε_info的具体分布参数），这些并非数学公理或第一性原理可推导的必然结果，而是依赖于特定市场微观结构、卖家群体特征及数据拟合的经验估计。在缺乏具体数据集或实证研究支持的情况下，断言精确的60/40比例及特定正态分布参数缺乏依据，属于过度精确化的经验假设。 | source=knowledge，逻辑上方差分解公式自洽，但具体的60%/40%比例及分布参数属于经验事实，缺乏来源直接支持或第一性原理推导，故降级。

## Search Query

price setting noise variance decomposition risk preference information asymmetry
