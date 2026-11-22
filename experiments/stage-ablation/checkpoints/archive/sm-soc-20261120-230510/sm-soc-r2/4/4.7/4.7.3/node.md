# N85: 高/低挂价卖家比例 r_high 的估计方法：r_high = N_sellers(P_ask > P_median * 1.15) / N_sellers_t

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N22

## Claim

高/低挂价卖家比例 r_high 的估计方法：r_high = N_sellers(P_ask > P_median * 1.15) / N_sellers_total，需基于平台历史数据计算该比例的具体数值，以消除 [0.3, 0.5] 的不确定性区间。

## Corrected Claim

高/低挂价卖家比例 r_high 可通过统计挂价高于中位数一定比例（如15%）的卖家占比来估计，具体阈值和比例数值需基于特定平台的历史交易数据实证计算，而非固定为[0.3, 0.5]。

## Evidence

[质询]该陈述包含具体的经验性参数（1.15倍中位数阈值）和具体的不确定性区间（[0.3, 0.5]），这些属于特定平台的市场经验数据，无法从第一性原理推导，且参考来源完全未涉及此内容，缺乏外部证据支持其具体数值的准确性。 | 参考来源[1]讨论的是股票/期货技术分析中的High 1/2/3形态，与二手交易平台卖家挂价比例统计无关，属于无关来源；该事实为经验性统计方法，逻辑自洽但缺乏来源支持，依据经验事实排除条款降级。

## Search Query

second-hand platform price distribution ratio high-priced sellers median

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1893095817650364599&rut=d10f4423bc903d1ab6ecfc4a9b403bb71927f96f92e131b59714f002ef3a47a8', 'type': 'ddg', 'title': '价格行为学：【高胜率策略】High 1、2、3 形态精准入场法'}
