# N290: DDoS_Attack_Frequency_Cost_Delta = (Monthly_Attacks - Annual_Attacks/12) × (MTTD

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N101

## Claim

DDoS_Attack_Frequency_Cost_Delta = (Monthly_Attacks - Annual_Attacks/12) × (MTTD_Hours × Hourly_Sec_Cost + MTTR_Hours × Hourly_Sec_Cost + Mitigation_Fee_Per_Event)，其中 MTTD/MTTR 为平均检测/响应时间，Mitigation_Fee 为云清洗服务单次费用（典型 ¥5k-20k/次）。

## Corrected Claim

DDoS_Attack_Frequency_Cost_Delta = (Monthly_Attacks - Annual_Attacks/12) × (MTTD_Hours × Hourly_Sec_Cost + MTTR_Hours × Hourly_Sec_Cost + Mitigation_Fee_Per_Event)，其中 MTTD/MTTR 为平均检测/响应时间，Mitigation_Fee 为云清洗服务单次费用（典型 ¥5k-20k/次）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

DDoS mitigation service cost per event incident fee
