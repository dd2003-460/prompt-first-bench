# N234: ‘成交概率提升 < 2%’的基准线定义：需明确基准是‘相对于未降价商品的成交概率’还是‘相对于降价前的成交概率’。若基准为市场平均成交概率 P_base，则需计

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

‘成交概率提升 < 2%’的基准线定义：需明确基准是‘相对于未降价商品的成交概率’还是‘相对于降价前的成交概率’。若基准为市场平均成交概率 P_base，则需计算 P(Sale | Price -5%) - P(Sale | Price) 的绝对差值，该差值受当前市场供需比 (Supply/Demand Ratio) 调节。

## Corrected Claim

‘成交概率提升 < 2%’的基准线定义：需明确基准是‘相对于未降价商品的成交概率’还是‘相对于降价前的成交概率’。若基准为市场平均成交概率 P_base，则需计算 P(Sale | Price -5%) - P(Sale | Price) 的绝对差值，该差值受当前市场供需比 (Supply/Demand Ratio) 调节。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述准确指出了概率提升基准线定义的歧义性，并正确构建了基于市场供需比调节的绝对差值计算逻辑，符合经济学与统计学基本原理。
