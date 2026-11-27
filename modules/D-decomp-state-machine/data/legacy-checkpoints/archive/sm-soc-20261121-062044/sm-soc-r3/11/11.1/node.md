# N273: 信号发送成本 C_signal_cost 的量化：C_signal_cost = (P_high - P_avg) * Q_lost * T_holding，其

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N99

## Claim

信号发送成本 C_signal_cost 的量化：C_signal_cost = (P_high - P_avg) * Q_lost * T_holding，其中 P_high 为高挂价，P_avg 为市场均价，Q_lost 为因高挂价导致的预期成交量损失，T_holding 为维持高挂价的时间周期；需通过反事实推断估计 Q_lost。

## Corrected Claim

信号发送成本 C_signal_cost 的量化：C_signal_cost = (P_high - P_avg) * Q_lost * T_holding，其中 P_high 为高挂价，P_avg 为市场均价，Q_lost 为因高挂价导致的预期成交量损失，T_holding 为维持高挂价的时间周期；需通过反事实推断估计 Q_lost。

## Evidence

先验知识/题面给定，逻辑校验通过
