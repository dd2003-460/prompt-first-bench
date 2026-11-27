# N173: 卖家先验概率 π_s 的量化：基于历史数据，卖家选择'高挂价'策略的先验概率 π_s_high 估计为 0.65，选择'正常定价'为 0.30，选择'低价促销'

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N53

## Claim

卖家先验概率 π_s 的量化：基于历史数据，卖家选择'高挂价'策略的先验概率 π_s_high 估计为 0.65，选择'正常定价'为 0.30，选择'低价促销'为 0.05；该分布需通过最大似然估计从过去 90 天的卖家行为日志中拟合得出，标准误 SE(π_s) ≈ 0.03。

## Corrected Claim

卖家先验概率 π_s 的量化通常基于历史数据通过最大似然估计拟合得出，具体数值（如高挂价概率）取决于特定数据集的统计结果，需根据实际日志计算。

## Evidence

[质询]该陈述包含具体的经验性数值（先验概率分布 0.65/0.30/0.05 及标准误 0.03），这些是特定数据集下的统计估计结果，无法从第一性原理或通用逻辑中推导得出，属于经验事实。 | 参考来源[1]仅讨论基于贝叶斯理论的交易策略通用逻辑，未提供具体的卖家定价先验概率数值或拟合方法细节，属于间接相关但无直接数据支持；该事实为经验统计结果，逻辑自洽但缺乏来源直接证实具体数值。

## Search Query

second hand platform seller pricing strategy prior probability distribution

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/672295574&rut=bf1c49bcb4fd3ef32da69a490441a1d2355f52178e144450fe6bbf0b40eef99f', 'type': 'ddg', 'title': '基于贝叶斯理论的交易策略 - 知乎'}
