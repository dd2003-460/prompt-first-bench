# N333: 卖家月均成交频率 f_trade 的估计：定义为卖家在 30 天窗口内的平均成交订单数，需结合不同活跃度分层（如月发布 >10 件 vs <3 件）分别计算，以

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N113

## Claim

卖家月均成交频率 f_trade 的估计：定义为卖家在 30 天窗口内的平均成交订单数，需结合不同活跃度分层（如月发布 >10 件 vs <3 件）分别计算，以推导月毛利损失总额 = E[ΔMargin] * f_trade。

## Corrected Claim

卖家月均成交频率 f_trade 可定义为卖家在特定时间窗口（如30天）内的平均成交订单数，具体分层标准（如月发布件数阈值）需根据实际业务数据分布确定，以推导月毛利损失总额 = E[ΔMargin] * f_trade。

## Evidence

[质询]该陈述包含具体的业务定义（30天窗口、特定活跃度分层阈值如>10件/<3件）及计算公式，属于经验性业务规则或特定模型假设，而非通用事实或第一性原理可推导结论。参考来源仅讨论亚马逊数据分析指标概览，未提供该特定定义或分层阈值的依据，存在口径混淆或来源不可靠的风险。 | 逻辑上自洽（定义清晰，公式结构合理），但参考来源[1]仅涉及亚马逊数据分析指标的一般性介绍，未直接支持该特定定义、分层阈值或计算公式，属于经验事实且缺乏直接来源支持。

## Search Query

seller monthly transaction frequency distribution active vs inactive

## Retrieval Sources

- {'url': 'https://www.sellfox.com/blog/article/ymx-sjfxzb-sellfox&rut=143071d84f21242537b6703a5bbdab2d343f907b969cec2f378348ff2ca27f7f', 'type': 'ddg', 'title': '亚马逊数据分析指标有哪些？深度拆解与专业数据分析工具提效指南'}
