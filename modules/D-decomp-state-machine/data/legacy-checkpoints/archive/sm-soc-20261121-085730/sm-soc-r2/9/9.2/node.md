# N141: 高时间敏感型买家流失率 ΔChurn 的计算公式为：ΔChurn = (ΔT / T_budget) * ε_time，其中 T_budget 为该类买家的剩余

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

高时间敏感型买家流失率 ΔChurn 的计算公式为：ΔChurn = (ΔT / T_budget) * ε_time，其中 T_budget 为该类买家的剩余时间预算（分钟），ε_time 为时间敏感度系数，需区分不同用户分层的 ε_time 值。

## Corrected Claim

高时间敏感型买家流失率 ΔChurn 的计算公式为：ΔChurn = (ΔT / T_budget) * ε_time，其中 T_budget 为该类买家的剩余时间预算（分钟），ε_time 为时间敏感度系数，需区分不同用户分层的 ε_time 值。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

time sensitive customer churn rate decision latency
