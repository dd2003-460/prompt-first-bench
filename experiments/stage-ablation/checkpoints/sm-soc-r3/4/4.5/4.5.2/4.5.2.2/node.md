# N237: Q_demand 的构成项：Q_demand = N_active_buyers * P(purchase | exposure) * E[items_per_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

Q_demand 的构成项：Q_demand = N_active_buyers * P(purchase | exposure) * E[items_per_buyer]，其中 P(purchase | exposure) 为曝光后购买转化率，E[items_per_buyer] 为平均购买件数；该指标对价格敏感度 α_price 和平台推荐算法效率高度敏感。

## Corrected Claim

Q_demand 的构成项：Q_demand = N_active_buyers * P(purchase | exposure) * E[items_per_buyer]，其中 P(purchase | exposure) 为曝光后购买转化率，E[items_per_buyer] 为平均购买件数；该指标对价格敏感度 α_price 和平台推荐算法效率高度敏感。

## Evidence

先验知识/题面给定，逻辑校验通过：需求分解公式符合基本概率与期望定义，量纲一致，且对价格及算法效率的敏感性符合经济学与推荐系统基本原理。

## Search Query

marketplace demand side active buyers conversion rate items per buyer
