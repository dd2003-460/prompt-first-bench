# N60: 筛选机制有效性的统计判据：若高挂价卖家的成交买家群体在支付意愿分布中的分位数（Q_high）显著高于低挂价卖家的分位数（Q_low），且 Q_high - Q_

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N15

## Claim

筛选机制有效性的统计判据：若高挂价卖家的成交买家群体在支付意愿分布中的分位数（Q_high）显著高于低挂价卖家的分位数（Q_low），且 Q_high - Q_low > 0，则筛选有效；需计算两组买家历史成交均价的差值 ΔP_buyer = E[P|HighList] - E[P|LowList]。

## Corrected Claim

筛选机制有效性的统计判据：在控制卖家特征及市场波动等混淆变量后，若高挂价卖家的成交买家群体在支付意愿分布中的分位数（Q_high）显著高于低挂价卖家的分位数（Q_low），且统计检验显示差异显著（如p<0.05），则初步表明筛选有效；需进一步通过因果推断方法（如双重差分或工具变量）验证 ΔP_buyer = E[P|HighList] - E[P|LowList] 的因果效应。

## Evidence

[质询]该陈述将‘筛选有效性’简化为单一统计指标（分位数差值或均价差值），忽略了因果推断中的内生性问题（如卖家可能根据买家特征动态调整挂价，导致反向因果或遗漏变量偏差），且未定义‘显著’的统计检验标准（如p值或置信区间），仅凭均值/分位数差异不能严格证明筛选机制的因果有效性。 | 逻辑自洽，但作为经验性统计判据，缺乏来源支持且存在因果推断漏洞，依据经验事实排除条款降级。

## Search Query

second hand market price discrimination seller high listing price buyer willingness to pay distribution
