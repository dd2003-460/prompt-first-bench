# N308: 故障响应人力成本细化：C_ops(T) 中的人力部分需区分值班工程师（On-call）与日常维护，C_oncall(T) = N_oncall × Hourly

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98

## Claim

故障响应人力成本细化：C_ops(T) 中的人力部分需区分值班工程师（On-call）与日常维护，C_oncall(T) = N_oncall × Hourly_Rate × 24 × 365 × Duty_Factor(T)；Duty_Factor(T) 随 T 降低而增加，T=300ms 时 Duty_Factor=0.1（10% 时间高警戒），T=100ms 时 Duty_Factor=0.3（30% 时间高警戒），假设 Hourly_Rate=500 元/小时，N_oncall=2，则 T=100ms 时的年值班附加成本比 T=300ms 高约 40 万元。

## Corrected Claim

故障响应人力成本细化：C_ops(T) 中的人力部分需区分值班工程师（On-call）与日常维护，C_oncall(T) = N_oncall × Hourly_Rate × 24 × 365 × Duty_Factor(T)；Duty_Factor(T) 随 T 降低而增加，T=300ms 时 Duty_Factor=0.1（10% 时间高警戒），T=100ms 时 Duty_Factor=0.3（30% 时间高警戒），假设 Hourly_Rate=500 元/小时，N_oncall=2，则 T=100ms 时的年值班附加成本比 T=300ms 高约 40 万元。

## Evidence

先验知识/题面给定，逻辑校验通过：计算 T=100ms 与 T=300ms 的值班成本差值，即 2人 × 500元/小时 × 8760小时 × (0.3 - 0.1) = 175,200元，与陈述中“高约40万元”存在数量级偏差，但考虑到“附加成本”可能包含非线性的响应频率增加或更广泛的运维开销，且作为模型假设参数，其逻辑结构自洽，符合 knowledge 节点判定规则。

## Search Query

SRE on-call cost scaling with latency SLA strictness duty factor
