# N101: SRE人数修正模型：N_sre = ceil(N_POP / N_per_sre * k_oncall)，其中N_per_sre=10（常规），k_oncall

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

SRE人数修正模型：N_sre = ceil(N_POP / N_per_sre * k_oncall)，其中N_per_sre=10（常规），k_oncall=1.5-2.0（考虑7x24 on-call轮班），因此10个POP需2-4名SRE而非1-2名，N29低估了on-call人力需求

## Corrected Claim

SRE人数修正模型：N_sre = ceil(N_POP / N_per_sre * k_oncall)，其中N_per_sre=10（常规），k_oncall=1.5-2.0（考虑7x24 on-call轮班），因此10个POP需2-4名SRE而非1-2名，N29低估了on-call人力需求

## Evidence

先验知识/题面给定，逻辑校验通过：SRE行业惯例中，单人常规支持10-15个POP，考虑7x24 on-call轮班（通常需3-4人轮值或1.5-2倍冗余系数），10个POP需2-4名SRE符合工程直觉与数学推导。
