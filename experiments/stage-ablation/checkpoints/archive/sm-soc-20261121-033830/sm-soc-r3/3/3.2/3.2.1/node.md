# N60: 筛选机制有效性的统计判据：若高挂价卖家的成交买家群体在支付意愿分布中的分位数（Q_high）显著高于低挂价卖家的分位数（Q_low），且 Q_high - Q_

- **status**: pending
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

父节点级核验失败（LLM 错误）：Invalid control character at: line 7 column 189 (char 682)

## Search Query

second hand market price discrimination seller high listing price buyer willingness to pay distribution
