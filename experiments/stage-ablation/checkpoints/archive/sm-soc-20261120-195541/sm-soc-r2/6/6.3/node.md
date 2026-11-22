# N60: 中间环节失效边界：当市场流动性低于阈值 L_min（定义为日均搜索量/在售商品数），噪声导致的匹配加速效应消失，此时高挂价仅增加 T_deal 而不提升 P_d

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

中间环节失效边界：当市场流动性低于阈值 L_min（定义为日均搜索量/在售商品数），噪声导致的匹配加速效应消失，此时高挂价仅增加 T_deal 而不提升 P_deal，导致 ESS 崩溃，该阈值需通过平台历史数据回归确定。

## Corrected Claim

中间环节失效边界：当市场流动性低于某一特定阈值时，噪声导致的匹配加速效应可能减弱或消失，此时高挂价可能仅增加成交时间而不提升成交概率，进而影响系统稳定性；该阈值的具体定义及数值需通过平台历史数据回归确定。

## Evidence

[质询]该陈述包含具体的经验性阈值定义（L_min = 日均搜索量/在售商品数）及特定的因果机制（噪声导致匹配加速效应消失），属于平台微观经济学的经验事实，无法从第一性原理严格推导，且缺乏来源支持其具体定义和机制的有效性。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

market liquidity threshold matching efficiency failure high price strategy second hand platform
