# N48: 对象 i 在 LRU 缓存中保持有效（未因更新失效）的概率 P_valid(i) = 1 - (1 - e^(-1/τ_obj)) * (τ_res(i) / 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N12

## Claim

对象 i 在 LRU 缓存中保持有效（未因更新失效）的概率 P_valid(i) = 1 - (1 - e^(-1/τ_obj)) * (τ_res(i) / τ_obj)，其中 τ_obj=100 天，τ_res(i)=1/R_i。

## Corrected Claim

对象 i 在 LRU 缓存中保持有效（未因更新失效）的概率 P_valid(i) = 1 - (1 - e^(-1/τ_obj)) * (τ_res(i) / τ_obj)，其中 τ_obj=100 天，τ_res(i)=1/R_i。

## Evidence

先验知识/题面给定，逻辑校验通过
