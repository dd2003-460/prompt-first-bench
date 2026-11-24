# N185: 故障概率与成本的期望值 E[Failure_Cost] = (Annual_Failure_Rate * MTTR_pop * C_penalty_per_mi

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N44

## Claim

故障概率与成本的期望值 E[Failure_Cost] = (Annual_Failure_Rate * MTTR_pop * C_penalty_per_minute) / Q_day * 1000，其中 Annual_Failure_Rate 为年故障次数（自建通常2-4次/年，公有云<0.5次/年），C_penalty_per_minute 为每分钟故障损失（由DAU和ARPU推导）。

## Corrected Claim

故障概率与成本的期望值 E[Failure_Cost] = (Annual_Failure_Rate * MTTR_pop * C_penalty_per_minute) / Q_day * 1000，其中 Annual_Failure_Rate 为年故障次数（自建通常2-4次/年，公有云<0.5次/年），C_penalty_per_minute 为每分钟故障损失（由DAU和ARPU推导）。

## Evidence

先验知识/题面给定，逻辑校验通过
