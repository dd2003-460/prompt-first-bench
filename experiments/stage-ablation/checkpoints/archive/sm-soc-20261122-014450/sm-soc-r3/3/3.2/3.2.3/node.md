# N63: 成交周期 T 与挂价溢价率 δ 的非线性关系：T(δ) = T_0 * (1 + κ * δ^2)，其中 T_0 为基准成交周期，κ 为溢价惩罚系数（通常 κ 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

成交周期 T 与挂价溢价率 δ 的非线性关系：T(δ) = T_0 * (1 + κ * δ^2)，其中 T_0 为基准成交周期，κ 为溢价惩罚系数（通常 κ ≈ 2-5）；需量化当 δ=0.2 时，T 相对于 T_0 的延长倍数（通常为 1.5-2.5 倍）。

## Corrected Claim

成交周期 T 与挂价溢价率 δ 通常存在非线性正相关关系，溢价率越高，成交周期延长越显著，但具体函数形式及系数（如κ值）需依据特定市场数据实证确定，通用理论中无固定标准值。

## Evidence

[质询]该陈述包含具体的经验参数（κ ≈ 2-5，延长倍数 1.5-2.5 倍）和特定的非线性函数形式（二次方），这些属于特定市场或模型下的经验事实，无法从第一性原理推导，且参考来源中完全未提及此类具体量化关系。 | 逻辑上自洽（δ=0.2时，1+κ*0.04在κ=2-5范围内确实对应1.08-1.2倍，与声称的1.5-2.5倍存在数值矛盾，但作为定性描述‘非线性惩罚’逻辑成立；然而，具体数值κ和倍数缺乏来源支持，且来源[1][2][3]均为通用金融/定价概念，未覆盖此具体模型参数，故判为degraded。

## Search Query

time to sell relationship listing price premium used goods market duration model

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Pricing_strategy', 'type': 'wikipedia', 'title': 'Pricing strategy'}
- {'url': 'https://en.wikipedia.org/wiki/Futures_contract', 'type': 'wikipedia', 'title': 'Futures contract'}
- {'url': 'https://en.wikipedia.org/wiki/Outline_of_finance', 'type': 'wikipedia', 'title': 'Outline of finance'}
