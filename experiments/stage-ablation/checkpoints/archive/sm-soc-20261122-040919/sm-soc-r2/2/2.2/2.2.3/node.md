# N55: 买家响应函数投影2：买家对‘快速成交’信号的质量推断修正项 ΔV_signal = α * T_short / T_avg，其中 α 为信号敏感度系数（假设 α

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N11

## Claim

买家响应函数投影2：买家对‘快速成交’信号的质量推断修正项 ΔV_signal = α * T_short / T_avg，其中 α 为信号敏感度系数（假设 α=0.1），T_short 为观察到的短周期，T_avg 为平均周期。该修正项直接叠加到 E[V_b] 中，导致在 σ_b 较大时，买家更易被噪声误导。

## Corrected Claim

买家响应函数投影2：买家对‘快速成交’信号的质量推断修正项 ΔV_signal = α * T_short / T_avg，其中 α 为信号敏感度系数（假设 α=0.1），T_short 为观察到的短周期，T_avg 为平均周期。该修正项直接叠加到 E[V_b] 中，导致在 σ_b 较大时，买家更易被噪声误导。

## Evidence

先验知识/题面给定，逻辑校验通过
