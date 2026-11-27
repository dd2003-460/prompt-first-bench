# N376: 演化风险偏好 w_risk 的可观测代理指标 O_risk：O_risk = (N_price_changes_30d / N_listings_30d) * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N125

## Claim

演化风险偏好 w_risk 的可观测代理指标 O_risk：O_risk = (N_price_changes_30d / N_listings_30d) * (1 + Var(ΔP) / Mean(ΔP)^2)，该指标通过价格调整频率和幅度变异系数量化卖家的演化风险偏好，用于替代不可直接观测的 w_risk。

## Corrected Claim

演化风险偏好 w_risk 的可观测代理指标 O_risk：O_risk = (N_price_changes_30d / N_listings_30d) * (1 + Var(ΔP) / Mean(ΔP)^2)，该指标通过价格调整频率和幅度变异系数量化卖家的演化风险偏好，用于替代不可直接观测的 w_risk。

## Evidence

先验知识/题面给定，逻辑校验通过
