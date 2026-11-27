# N321: 适应度函数映射的具体形式：Fitness_seller = E[Profit] = P_ask * Prob(Sell|P_ask) - C_listing -

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N114

## Claim

适应度函数映射的具体形式：Fitness_seller = E[Profit] = P_ask * Prob(Sell|P_ask) - C_listing - C_negotiation，其中 Prob(Sell|P_ask) 为基于搜索匹配模型的成交概率函数，C_listing 为上架成本，C_negotiation 为议价时间成本。

## Corrected Claim

适应度函数映射的具体形式：Fitness_seller = E[Profit] = P_ask * Prob(Sell|P_ask) - C_listing - C_negotiation，其中 Prob(Sell|P_ask) 为基于搜索匹配模型的成交概率函数，C_listing 为上架成本，C_negotiation 为议价时间成本。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合经济学中期望效用/利润最大化的基本定义（期望收益减去固定与可变成本），量纲一致（货币单位），且作为适应度函数在进化算法或强化学习语境下逻辑自洽。
