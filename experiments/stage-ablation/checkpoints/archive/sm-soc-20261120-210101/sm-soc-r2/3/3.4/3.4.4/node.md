# N72: 平台佣金收入变化量化：计算干预前后平台总佣金变化 ΔCommission = (P_new * Q_new - P_old * Q_old) * Rate_co

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

平台佣金收入变化量化：计算干预前后平台总佣金变化 ΔCommission = (P_new * Q_new - P_old * Q_old) * Rate_commission。由于价格下降但销量可能上升，需计算净效应。若 ΔCommission < 0，表明平台短期受损；若 ΔCommission > 0，表明平台通过以价换量获得净收益。需结合弹性 ε_d 判断盈亏平衡点。

## Corrected Claim

平台佣金收入变化量化：计算干预前后平台总佣金变化 ΔCommission = (P_new * Q_new - P_old * Q_old) * Rate_commission。由于价格下降但销量可能上升，需计算净效应。若 ΔCommission < 0，表明平台短期受损；若 ΔCommission > 0，表明平台通过以价换量获得净收益。需结合弹性 ε_d 判断盈亏平衡点。

## Evidence

先验知识/题面给定，逻辑校验通过
