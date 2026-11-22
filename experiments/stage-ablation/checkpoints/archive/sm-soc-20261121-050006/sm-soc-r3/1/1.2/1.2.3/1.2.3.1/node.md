# N133: 心理参考价权重 w_purchase（购买成本权重）的估计值：基于卖家自报数据回归，预期 w_purchase ∈ [0.4, 0.6]，且与卖家持有时间 T_

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N38

## Claim

心理参考价权重 w_purchase（购买成本权重）的估计值：基于卖家自报数据回归，预期 w_purchase ∈ [0.4, 0.6]，且与卖家持有时间 T_hold 正相关（w_purchase = 0.5 + 0.02 * T_hold/30），需通过面板数据固定效应模型校准。

## Corrected Claim

心理参考价权重 w_purchase 的估计值需通过面板数据固定效应模型校准，预期与卖家持有时间 T_hold 正相关，具体数值区间及回归系数需依据特定数据集实证结果确定。

## Evidence

[质询]该陈述包含具体的经验性回归系数（w_purchase = 0.5 + 0.02 * T_hold/30）和特定区间 [0.4, 0.6]，属于具体的实证研究结论或模型参数，无法从第一性原理推导，且参考来源未提供此具体数值支持。 | 参考来源[1]仅讨论PSM模型的一般步骤，未涉及购买成本权重w_purchase的具体估计值或回归公式，属于经验事实且缺乏直接来源支持。

## Search Query

weight of purchase price in seller reference price formation holding period effect

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/545942954&rut=55039934843aeb89a537e8d122c751a19e463f85b6c1f1aed124379f9cef540a', 'type': 'ddg', 'title': '一个模型帮你找到消费者的"心理价" - 知乎'}
