# N279: 平台佣金收入变化 ΔCommission_platform = (P_avg - P_current) * Q_new * c_rate，由于 P_avg < 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

平台佣金收入变化 ΔCommission_platform = (P_avg - P_current) * Q_new * c_rate，由于 P_avg < P_current，若 Q_new 下降幅度小于价格下降幅度，则平台总佣金收入可能下降；需计算临界成交量 Q_crit = (P_current * Q_old) / P_avg，若 Q_new < Q_crit，则平台收入受损。

## Corrected Claim

平台佣金收入变化 ΔCommission_platform = (P_avg - P_current) * Q_new * c_rate，由于 P_avg < P_current，若 Q_new 下降幅度小于价格下降幅度，则平台总佣金收入可能下降；需计算临界成交量 Q_crit = (P_current * Q_old) / P_avg，若 Q_new < Q_crit，则平台收入受损。

## Evidence

先验知识/题面给定，逻辑校验通过
