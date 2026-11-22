# N63: 平台算法曝光权重 w_i 的实证估计：通过回归 log(Exposure_i) = α + β1*log(P_i) + β2*Interaction_i + ε

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N16

## Claim

平台算法曝光权重 w_i 的实证估计：通过回归 log(Exposure_i) = α + β1*log(P_i) + β2*Interaction_i + ε，检验 β1 是否显著为正（>0.1）且 β1*Interaction 交互项是否放大高价高互动商品的曝光，以确认算法是否主动偏向高价。

## Corrected Claim

一种常见的实证分析方法是回归 log(Exposure_i) = α + β1*log(P_i) + β2*Interaction_i + ε，通过检验 β1 的显著性及交互项的影响，来探讨价格与曝光之间的统计关联，但需注意内生性问题以区分算法偏向与商品自身属性影响。

## Evidence

[质询]该陈述描述的是一个具体的实证研究设计（回归模型设定及假设检验标准），属于经验事实范畴。由于缺乏具体的数据来源、样本范围或已发表的实证研究结果，无法确认该特定回归模型在特定平台上的实际估计结果是否如陈述所述（即β1是否显著大于0.1且交互项是否放大曝光）。此外，'确认算法是否主动偏向高价'这一结论依赖于对回归系数的因果解释，而观察性数据中的回归系数可能受内生性（如高价商品本身具有更高互动率或品牌效应）影响，不能直接等同于算法的'主动'偏向。 | 经验事实，逻辑自洽但缺来源支持。该陈述描述了一个合理的计量经济学分析框架，但作为实证结论，其具体数值（β1>0.1）和因果推断（算法主动偏向）需要具体数据支持，当前无可用外部证据验证其具体实证结果。

## Search Query

marketplace algorithm exposure bias high price high engagement GMV optimization regression coefficient
