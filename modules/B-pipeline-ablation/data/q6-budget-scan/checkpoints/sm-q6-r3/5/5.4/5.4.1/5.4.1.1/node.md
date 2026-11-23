# N256: 工作集大小 N_unique_active 的计算公式为 N_unique_active = N_total_uploads * (1 - e^(-λ_deca

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

工作集大小 N_unique_active 的计算公式为 N_unique_active = N_total_uploads * (1 - e^(-λ_decay * T_ttl))，其中 N_total_uploads 为总上传对象数，λ_decay 为对象访问衰减率，T_ttl 为缓存TTL

## Corrected Claim

工作集大小 N_unique_active 的计算公式为 N_unique_active = N_total_uploads * (1 - e^(-λ_decay * T_ttl))，其中 N_total_uploads 为总上传对象数，λ_decay 为对象访问衰减率，T_ttl 为缓存TTL

## Evidence

先验知识/题面给定，逻辑校验通过
