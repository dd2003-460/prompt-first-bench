# N147: 全自建策略月度运维人力成本 C_ops_self = N_engineers * C_salary_monthly * (1 + overhead_rate)，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

全自建策略月度运维人力成本 C_ops_self = N_engineers * C_salary_monthly * (1 + overhead_rate)，其中 N_engineers=5（10个POP点需5名SRE），C_salary_monthly ≈ ¥25k-40k/人（一线城市），overhead_rate=0.3（社保公积金），故 C_ops_self ≈ ¥162k-260k/月

## Corrected Claim

全自建策略月度运维人力成本 C_ops_self = N_engineers * C_salary_monthly * (1 + overhead_rate)，其中 N_engineers=5（10个POP点需5名SRE），C_salary_monthly ≈ ¥25k-40k/人（一线城市），overhead_rate=0.3（社保公积金），故 C_ops_self ≈ ¥162k-260k/月

## Evidence

先验知识/题面给定，逻辑校验通过：5人 * (2.5万~4万) * 1.3 = 16.25万~26万，计算无误且符合一线城市SRE薪资及社保公积金比例常识。

## Search Query

SRE engineer salary China first-tier city monthly 2024
