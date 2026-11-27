# N55: 信息展示对成交概率的非线性影响：展示价格偏离度不仅缩短决策时间，还可能降低成交概率（如果偏离度>阈值 τ_reject，买家直接放弃）。需量化 τ_reject

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

信息展示对成交概率的非线性影响：展示价格偏离度不仅缩短决策时间，还可能降低成交概率（如果偏离度>阈值 τ_reject，买家直接放弃）。需量化 τ_reject 的分布，例如 P(Reject | ΔI > 0.25) = 0.4，这意味着高溢价卖家面临双重打击（时间变短但流失率增加）。

## Corrected Claim

信息展示对成交概率可能存在非线性影响：展示价格偏离度过大可能导致买家直接放弃，从而降低成交概率。具体阈值和概率分布需根据特定市场数据量化，而非固定为P(Reject | ΔI > 0.25) = 0.4。

## Evidence

[质询]陈述中给出的具体数值（如阈值0.25、概率0.4）属于经验事实，参考来源均未提供该特定场景下的量化数据，存在无来源支持的风险。 | 逻辑自洽，但参考来源[1]讨论的是交易延迟与逆向选择，[2]讨论的是限价订单簿深度学习预测，均未直接支持‘信息展示偏离度’导致‘成交概率非线性下降’的具体量化结论，属于经验事实缺来源支持。

## Search Query

price transparency effect on purchase intention threshold rejection rate

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2054723981064901471&rut=f20719b98f151033e2726a82023b009e541058b48e53d48e846cfbd0879f1077', 'type': 'ddg', 'title': '交易延迟对成交率的定量影响：队列、生存分析与逆向选择'}
- {'url': 'https://zhuanlan.zhihu.com/p/594792008&rut=f90d261631dc17f8160afcf10f43eccf7a6d50453abae31e763afc564218200a', 'type': 'ddg', 'title': '用深度学习方法来估计限价订单簿中的成交概率 - 知乎'}
