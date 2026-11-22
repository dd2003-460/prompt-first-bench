# N127: 锚定偏差 δ_anchoring 的实证均值量化：在二手非标品市场中，卖家挂价相对于近期成交中位数的锚定偏差均值 μ_δ 约为 0.05 * V_true，标准

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N38

## Claim

锚定偏差 δ_anchoring 的实证均值量化：在二手非标品市场中，卖家挂价相对于近期成交中位数的锚定偏差均值 μ_δ 约为 0.05 * V_true，标准差 σ_δ 约为 0.02 * V_true，导致 P_ask 分布的右偏。

## Corrected Claim

在二手非标品市场中，卖家挂价相对于近期成交中位数通常存在正向锚定偏差，导致 P_ask 分布呈现右偏特征，但具体偏差均值和标准差因市场环境和品类而异，缺乏统一的固定量化标准。

## Evidence

[质询]该陈述提供了非常具体的量化数值（均值0.05，标准差0.02），但参考来源仅定性描述了锚定偏差的概念，未提供针对“二手非标品市场”的具体实证统计数据，且不同市场、不同品类下的锚定偏差幅度差异巨大，缺乏普适性的固定数值支持。 | 来源[1]仅定性解释锚定偏差，未提供具体数值支持；该事实属于特定市场场景下的经验统计参数，逻辑上自洽（右偏分布符合锚定效应特征），但缺乏直接来源支持具体数值，故降级。

## Search Query

second-hand marketplace seller asking price anchoring bias deviation mean standard deviation

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/336629232&rut=58d384d4427087e6e91ae5293a6e14d259399a437289608e8b731e04f6116131', 'type': 'ddg', 'title': '投资中的心理偏差（七）锚定偏差 - 知乎 - 知乎专栏'}
