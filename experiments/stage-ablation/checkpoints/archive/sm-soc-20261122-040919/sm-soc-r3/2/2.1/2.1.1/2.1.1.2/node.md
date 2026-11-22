# N190: 波动率参数 σ_T 的估计：成交周期 T 的标准差 σ_T 需通过平台历史成交数据计算。若 T 服从对数正态分布（常见于等待时间），则 σ_T 可通过样本标准差

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N49

## Claim

波动率参数 σ_T 的估计：成交周期 T 的标准差 σ_T 需通过平台历史成交数据计算。若 T 服从对数正态分布（常见于等待时间），则 σ_T 可通过样本标准差估计。例如，若 T 的均值为 7 天，中位数为 6 天，则 σ_T ≈ 2 天。此参数是计算 Var[r×T] 中 E[r]^2 * Var[T] 项的关键输入。

## Corrected Claim

波动率参数 σ_T 的估计：成交周期 T 的标准差 σ_T 需通过平台历史成交数据计算。若 T 服从对数正态分布，则 σ_T 可通过样本标准差估计。此参数是计算 Var[r×T] 中 E[r]^2 * Var[T] 项的关键输入。

## Evidence

[质询]该陈述包含具体的经验性数值示例（均值7天、中位数6天对应标准差约2天），这属于特定场景下的统计估计，无法从第一性原理严格推导，且参考来源未提供此类具体数值支持。 | 逻辑上，若T服从对数正态分布，其均值、中位数与标准差存在确定的数学关系，给定的数值示例在量级和逻辑上是自洽的（例如，对数正态分布中，若中位数6，均值7，则ln(7/6)≈0.154，sigma_ln≈0.154，sigma_T≈6*exp(0.154^2/2)-6≈0.7天，虽然示例中的2天偏大，但在宽泛的‘常见于等待时间’语境下，作为粗略估计或不同参数下的示例并非逻辑错误，但缺乏来源直接支持具体数值）。参考来源[1][2]讨论的是金融价格波动率模型（GARCH等），与成交周期T的分布估计主题不直接相关，无法提供直接支持。

## Search Query

standard deviation of transaction cycle time e-commerce platform data

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1945152227128877088&rut=f276389f5cb40f11038f99933b2337deed75fe02feb5c193b3a42bc529b0c045', 'type': 'ddg', 'title': '量化交易基础(七)----波动率 - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/1889549508528042592&rut=0cad39759336eb9887f0ce1d483b30274467cbd87fea3543f6a0d47a867e6738', 'type': 'ddg', 'title': '掌握金融波动率模型：完整 Python 实现指南 - 知乎'}
