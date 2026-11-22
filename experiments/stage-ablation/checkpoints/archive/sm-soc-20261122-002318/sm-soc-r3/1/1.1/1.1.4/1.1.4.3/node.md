# N115: 均值代理项 $P_{mean\_volume}$ 的计算基准：取过去 30 天内同品类成交单，按成交量加权平均（Volume-Weighted Average 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N37

## Claim

均值代理项 $P_{mean\_volume}$ 的计算基准：取过去 30 天内同品类成交单，按成交量加权平均（Volume-Weighted Average Price, VWAP），公式为 $\frac{\sum (P_i \times V_i)}{\sum V_i}$，以反映市场实际交易重心而非单纯算术平均。

## Corrected Claim

均值代理项 $P_{mean\_volume}$ 的计算基准：取过去 30 天内同品类成交单，按成交量加权平均（Volume-Weighted Average Price, VWAP），公式为 $\frac{\sum (P_i \times V_i)}{\sum V_i}$，以反映市场实际交易重心而非单纯算术平均。

## Evidence

先验知识/题面给定，逻辑校验通过：VWAP定义及公式正确，30天同品类加权平均作为均值代理项在逻辑上自洽且符合金融/交易领域常规做法。
