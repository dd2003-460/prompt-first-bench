# N362: 重新评估阈值 ΔP_crit 的动态计算模型：ΔP_crit 不是固定值，而是随买家当前持有成本（Opportunity Cost）和替代品可得性变化。公式为 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N115

## Claim

重新评估阈值 ΔP_crit 的动态计算模型：ΔP_crit 不是固定值，而是随买家当前持有成本（Opportunity Cost）和替代品可得性变化。公式为 ΔP_crit = max(Weber_Fraction * P_current, Search_Cost_Marginal / Elasticity)。若降价幅度 ΔP < ΔP_crit，买家视为噪音；若 ΔP ≥ ΔP_crit，买家视为信号。需计算 60% 无咨询卖家的实际 ΔP 分布，并与基于其商品特征的 ΔP_crit 分布进行叠加，计算 P(ΔP < ΔP_crit) 的理论值，看是否接近 60%。

## Corrected Claim

重新评估阈值 ΔP_crit 的动态计算模型：ΔP_crit 不是固定值，而是随买家当前持有成本（Opportunity Cost）和替代品可得性变化。公式为 ΔP_crit = max(Weber_Fraction * P_current, Search_Cost_Marginal / Elasticity)。若降价幅度 ΔP < ΔP_crit，买家视为噪音；若 ΔP ≥ ΔP_crit，买家视为信号。需计算 60% 无咨询卖家的实际 ΔP 分布，并与基于其商品特征的 ΔP_crit 分布进行叠加，计算 P(ΔP < ΔP_crit) 的理论值，看是否接近 60%。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

dynamic re-evaluation threshold price change signal noise Weber fraction
