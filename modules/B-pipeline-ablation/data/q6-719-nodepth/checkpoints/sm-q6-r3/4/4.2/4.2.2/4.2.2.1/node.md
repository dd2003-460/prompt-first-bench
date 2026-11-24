# N337: 10个自建POP的总缓存容量 C_pop_total (GB) 由单POP硬件配置决定：C_pop_total = N_pop * (SSD_capacity 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N105

## Claim

10个自建POP的总缓存容量 C_pop_total (GB) 由单POP硬件配置决定：C_pop_total = N_pop * (SSD_capacity * U_ssd)，其中 N_pop=10，SSD_capacity 典型为 10-20TB/POP，U_ssd 为存储利用率（典型 0.8-0.9），故 C_pop_total ≈ 80-180TB。

## Corrected Claim

10个自建POP的总缓存容量 C_pop_total (GB) 由单POP硬件配置决定：C_pop_total = N_pop * (SSD_capacity * U_ssd)，其中 N_pop=10，SSD_capacity 典型为 10-20TB/POP，U_ssd 为存储利用率（典型 0.8-0.9），故 C_pop_total ≈ 80-180TB。

## Evidence

先验知识/题面给定，逻辑校验通过：10 * (10~20TB * 0.8~0.9) = 80~180TB，计算无误且符合工程常识。
