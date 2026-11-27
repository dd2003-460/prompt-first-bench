# N206: 无惩罚假设下的基准咨询到达率 λ_base 的量化：定义为同类商品在正常价格区间（±5% P_market）且无风控标记时，48小时内的平均新咨询次数，需从平台

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N75

## Claim

无惩罚假设下的基准咨询到达率 λ_base 的量化：定义为同类商品在正常价格区间（±5% P_market）且无风控标记时，48小时内的平均新咨询次数，需从平台历史日志中剔除已触发风控样本后计算均值。

## Corrected Claim

无惩罚假设下的基准咨询到达率 λ_base 定义为：在同类商品处于正常价格区间（±5% P_market）且无风控标记的条件下，基于平台历史日志剔除已触发风控样本后计算得出的48小时内平均新咨询次数。

## Evidence

[质询]该陈述定义了一个特定的业务指标（λ_base），属于经验性业务规则或内部定义，无法从第一性原理推导，且参考来源完全无关，缺乏外部证据支持其定义的合理性或行业通用性。 | 参考来源[1][2]讨论的是市场调研中的TURF模型（累计不重复到达率），与电商咨询到达率、风控剔除等业务逻辑无关，属于无关来源；该事实为特定场景下的经验性定义，逻辑自洽但缺来源支持。

## Search Query

e-commerce platform average inquiry rate 48 hours normal pricing range historical data

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/677842960&rut=c3947665d4082d191de9d28aa0ce770c7caa24beb9e49766aa405e5a392eb7b3', 'type': 'ddg', 'title': '市场调研分析方法——累计不重复到达率和频次分析（TURF）'}
- {'url': 'https://zhuanlan.zhihu.com/p/490678820&rut=8ac75c0fe74da1d7ab6a74956c84ac8189295837f904004acd04f36d9dc0442f', 'type': 'ddg', 'title': '如何以最小的成本覆盖到最大的消费群体？TURF模型介绍'}
