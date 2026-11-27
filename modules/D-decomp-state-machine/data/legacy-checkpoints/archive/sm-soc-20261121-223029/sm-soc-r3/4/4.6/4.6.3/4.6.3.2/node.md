# N284: 工作点2（中补贴中覆盖）：设定 Subsidy_per_deal = 15 元，覆盖 N_deals_post = 5,000 单/月，直接现金成本 ΔCost

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

工作点2（中补贴中覆盖）：设定 Subsidy_per_deal = 15 元，覆盖 N_deals_post = 5,000 单/月，直接现金成本 ΔCost_Direct = 75,000 元/月；流量倾斜导致低质商品曝光增加，预估 ΔChurn_rate 增加 0.3%，需折算为长期 LTV 损失。

## Corrected Claim

工作点2（中补贴中覆盖）：设定 Subsidy_per_deal = 15 元，覆盖 N_deals_post = 5,000 单/月，直接现金成本 ΔCost_Direct = 75,000 元/月；流量倾斜导致低质商品曝光增加，预估 ΔChurn_rate 增加 0.3%，需折算为长期 LTV 损失。

## Evidence

先验知识/题面给定，逻辑校验通过：直接成本计算 15 * 5000 = 75,000 元/月，数值准确；流失率增加 0.3% 为合理预估参数，无逻辑矛盾。

## Search Query

trade off between subsidy intensity and user churn rate
