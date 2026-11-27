# N244: GMV变动项的具体计算为 ΔGMV = (P_new_median - P_old_median) * Q_new + P_old_median * (Q_ne

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75, N76, N77

## Claim

GMV变动项的具体计算为 ΔGMV = (P_new_median - P_old_median) * Q_new + P_old_median * (Q_new - Q_old)，其中 P_new_median 为干预后成交中位数，Q_new 为干预后成交量，该公式需结合 N89 中的挂价下调幅度 ΔP_ask 和 N100 中的匹配概率变化 p_match 进行联动计算。

## Corrected Claim

GMV变动项的具体计算为 ΔGMV = (P_new_median - P_old_median) * Q_new + P_old_median * (Q_new - Q_old)，其中 P_new_median 为干预后成交中位数，Q_new 为干预后成交量，该公式需结合 N89 中的挂价下调幅度 ΔP_ask 和 N100 中的匹配概率变化 p_match 进行联动计算。

## Evidence

先验知识/题面给定，逻辑校验通过
