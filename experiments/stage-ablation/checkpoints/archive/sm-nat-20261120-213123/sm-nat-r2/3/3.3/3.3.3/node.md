# N49: D 的边界条件：当 u * T_LRU > 0.1 时，线性近似 D = 1 - u * T_LRU 失效，需使用指数形式 D = 1 - (1 - e^(-u

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16, N17, N18

## Claim

D 的边界条件：当 u * T_LRU > 0.1 时，线性近似 D = 1 - u * T_LRU 失效，需使用指数形式 D = 1 - (1 - e^(-u * T_LRU)) * (S_hot/S_total)，其中 S_hot/S_total 为热门对象字节占比。

## Corrected Claim

D 的边界条件：当 u * T_LRU > 0.1 时，线性近似 D = 1 - u * T_LRU 失效，需使用指数形式 D = 1 - (1 - e^(-u * T_LRU)) * (S_hot/S_total)，其中 S_hot/S_total 为热门对象字节占比。

## Evidence

先验知识/题面给定，逻辑校验通过
