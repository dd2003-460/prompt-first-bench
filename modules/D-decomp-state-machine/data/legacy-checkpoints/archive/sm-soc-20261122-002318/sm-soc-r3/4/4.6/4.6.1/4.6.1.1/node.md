# N202: 临界条件（C1）：卖家初始利润基准 Initial_Profit = (P_ask - C_seller) * Prob(Sale|P_ask)，其中 C_se

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N71

## Claim

临界条件（C1）：卖家初始利润基准 Initial_Profit = (P_ask - C_seller) * Prob(Sale|P_ask)，其中 C_seller 为卖家持有成本，该值作为计算相对利润下降比例的分母，需从平台历史成交数据中提取平均持有成本和成交概率分布。

## Corrected Claim

临界条件（C1）：卖家初始利润基准 Initial_Profit = (P_ask - C_seller) * Prob(Sale|P_ask)，其中 C_seller 为卖家持有成本，该值作为计算相对利润下降比例的分母，需从平台历史成交数据中提取平均持有成本和成交概率分布。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合经济学中期望利润定义，且作为基准分母的设定在逻辑上自洽。
