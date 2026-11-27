# N160: 共享随机源映射：卖家在优化时使用的概率估计 Prob̂(Sell|P_ask) = Prob(Sell|P_ask) + ε_seller，其中 ε_selle

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N48

## Claim

共享随机源映射：卖家在优化时使用的概率估计 Prob̂(Sell|P_ask) = Prob(Sell|P_ask) + ε_seller，其中 ε_seller 继承自 N47 的 N(0, σ²_seller)，该随机项直接进入一阶条件的左端项。

## Corrected Claim

共享随机源映射：卖家在优化时使用的概率估计 Prob̂(Sell|P_ask) = Prob(Sell|P_ask) + ε_seller，其中 ε_seller 继承自 N47 的 N(0, σ²_seller)，该随机项直接进入一阶条件的左端项。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述描述了优化问题中概率估计的扰动形式及其在一阶条件中的位置，数学结构自洽，无内部矛盾。
