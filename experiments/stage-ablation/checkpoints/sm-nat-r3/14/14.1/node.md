# N306: T_res_avg 的加权计算：T_res_avg = (1/N_cache) * Σ_{i∈S_LRU} W_LRU(i)，其中 W_LRU(i) = 1 /

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N109

## Claim

T_res_avg 的加权计算：T_res_avg = (1/N_cache) * Σ_{i∈S_LRU} W_LRU(i)，其中 W_LRU(i) = 1 / (Σ_{j>i} λ_j)，λ_j 为对象 j 的请求速率；需区分高频对象（头部）和低频对象（尾部）的驻留时间差异，以量化 D_update 的整体折损。

## Corrected Claim

T_res_avg 的加权计算：T_res_avg = (1/N_cache) * Σ_{i∈S_LRU} W_LRU(i)，其中 W_LRU(i) = 1 / (Σ_{j>i} λ_j)，λ_j 为对象 j 的请求速率；需区分高频对象（头部）和低频对象（尾部）的驻留时间差异，以量化 D_update 的整体折损。

## Evidence

先验知识/题面给定，逻辑校验通过
