# N52: 低质卖家进入概率 P_entry_low_quality 与价格下限 P_floor 负相关：P_entry_low_quality = f(P_floor /

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N13

## Claim

低质卖家进入概率 P_entry_low_quality 与价格下限 P_floor 负相关：P_entry_low_quality = f(P_floor / P_market)，当 P_floor 低于市场均价 10% 时，低质卖家进入概率上升幅度 ΔP_entry 需通过历史数据回归估算。

## Corrected Claim

低质卖家进入概率 P_entry_low_quality 通常与价格下限 P_floor 负相关。具体函数形式及阈值（如低于市场均价10%时的影响幅度）需通过特定市场的历史数据回归估算，缺乏通用理论公式。

## Evidence

[质询]该陈述包含具体的经验性阈值（低于市场均价10%）和特定的函数形式，属于经验事实。参考来源[1]讨论的是交易机器人的挂单策略（entry/exit pricing），与卖家进入概率无关；来源[2]讨论的是Lowe's零售定价，未涉及低质卖家进入概率与价格下限的定量关系。因此，缺乏直接来源支持该具体数值和函数关系。 | 逻辑上，降低价格下限通常会降低进入门槛，从而可能增加低质卖家进入概率，方向合理。但具体阈值（10%）和函数形式 f(P_floor/P_market) 属于经验事实，参考来源[1][2]均与该特定经济模型或统计规律无关，无法提供直接支持。

## Search Query

market entry probability low quality sellers price threshold second hand market

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1955300140131804396&rut=72e9edf7cdcd48da1a50c531d260cfbcec26915c1a0ce6dbb957c22ec105d825', 'type': 'ddg', 'title': '第13篇： 如何精准控制买入卖出价格？entry/exit_pricing 实战配置'}
- {'url': 'https://zhuanlan.zhihu.com/p/2070443219201029608&rut=4c15588b61f449880123ff785ab36e5ddb9ebac00033ce652a2e74bd1bca3156', 'type': 'ddg', 'title': "Lowe's定价实操指南｜VC和3P全拆解 - 知乎"}
