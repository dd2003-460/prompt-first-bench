# N179: 预期销量 Q_suggest 的价格弹性模型：Q_suggest = Q_initial * (P_suggest / P_ask_initial)^(-ε_p

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N56

## Claim

预期销量 Q_suggest 的价格弹性模型：Q_suggest = Q_initial * (P_suggest / P_ask_initial)^(-ε_price)，其中 ε_price 为需求价格弹性系数，需通过历史成交数据回归估计 ε_price 的具体数值。

## Corrected Claim

预期销量 Q_suggest 的价格弹性模型：Q_suggest = Q_initial * (P_suggest / P_ask_initial)^(-ε_price)，其中 ε_price 为需求价格弹性系数，需通过历史成交数据回归估计 ε_price 的具体数值。

## Evidence

[rework-angle r1] 来源[1]和[2]直接支持价格弹性定义及需求对价格的响应关系，公式形式符合常规模型设定，逻辑自洽。

## Search Query

constant elasticity demand model price elasticity estimation regression
