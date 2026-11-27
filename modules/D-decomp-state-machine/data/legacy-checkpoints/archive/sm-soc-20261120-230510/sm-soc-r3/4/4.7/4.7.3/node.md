# N85: 高/低挂价卖家比例 r_high 的估计方法：r_high = N_sellers(P_ask > P_median * 1.15) / N_sellers_t

- **status**: pending
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

父节点级核验未通过：不完备（子节点1提供了基于对数正态分布的理论估算方法，子节点2提供了基于品类异质性的参数修正方法。两者在逻辑上是互补的（基础模型 vs. 修正因素），不重复也不矛盾，因此正交性合格。然而，父节点明确要求“基于平台历史数据计算该比例的具体数值”，而两个子节点均依赖于假设的分布参数（σ_log）或经验典型值，缺乏从原始历史数据（P_ask 和 P_median）直接计算 r_high 的具体统计步骤（如直接计数或核密度估计），未能完全覆盖“基于历史数据”这一核心要求。）

## Search Query

second-hand platform price distribution ratio high-priced sellers median

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1893095817650364599&rut=d10f4423bc903d1ab6ecfc4a9b403bb71927f96f92e131b59714f002ef3a47a8', 'type': 'ddg', 'title': '价格行为学：【高胜率策略】High 1、2、3 形态精准入场法'}
