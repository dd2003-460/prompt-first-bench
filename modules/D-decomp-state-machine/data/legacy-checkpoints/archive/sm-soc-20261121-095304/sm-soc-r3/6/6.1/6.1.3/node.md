# N171: 非线性交互效应：当 δ > 2σ 时，买家心理账户触发'异常高价'预警，导致搜索跳出率 Jump_Rate 从基线 10% 上升至 30-50%，使得实际有效成

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N60

## Claim

非线性交互效应：当 δ > 2σ 时，买家心理账户触发'异常高价'预警，导致搜索跳出率 Jump_Rate 从基线 10% 上升至 30-50%，使得实际有效成交概率 P(deal)_effective = P(deal) * (1 - Jump_Rate) 进一步骤降，需引入行为修正项。

## Corrected Claim

非线性交互效应：当价格偏离度 δ 超过一定阈值（如 2σ）时，买家心理账户可能触发'异常高价'预警，导致搜索跳出率显著上升，使得实际有效成交概率 P(deal)_effective = P(deal) * (1 - Jump_Rate) 下降，需引入行为修正项。

## Evidence

[质询]该陈述包含具体的经验性数值（基线跳出率10%，异常时30-50%）和特定的行为经济学阈值（δ > 2σ），这些属于经验事实而非第一性原理可推导的数学或逻辑结论。参考来源仅讨论统计模型中交互项的解释方法，未提供电商场景下具体的跳出率数据或心理账户触发阈值，因此缺乏直接来源支持。 | 逻辑上，跳出率上升导致有效成交概率下降的推导自洽（P_eff = P * (1 - Jump)），但具体数值（10%, 30-50%）及阈值（2σ）为经验参数，参考来源[1][2]仅涉及统计方法论，与该具体业务事实主题不匹配，无法提供外部证据支持。

## Search Query

behavioral economics price anomaly jump rate online marketplace

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/573668428&rut=7e6e0e2af44f96af5d4b1671bab4da509e8e05fa7d1bec6e4e37237630a9d956', 'type': 'ddg', 'title': 'Stata：非线性模型的交互效应 - 知乎'}
- {'url': 'https://www.sohu.com/a/324980968_668066&rut=e0416a69ef253b580974ff873e81aa122ade7be442eca1e573ad86c9de3f9d35', 'type': 'ddg', 'title': '关于交互项的那些事（四）：非线性模型中的交互效应_Stata'}
