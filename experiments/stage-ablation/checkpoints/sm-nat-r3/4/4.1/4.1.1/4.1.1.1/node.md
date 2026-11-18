# N127: 全局平均驻留时间 T_LRU_global 的数值计算：T_LRU_global = K_LRU / R_total。若 K_LRU 由容量决定且 N=100,

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N54

## Claim

全局平均驻留时间 T_LRU_global 的数值计算：T_LRU_global = K_LRU / R_total。若 K_LRU 由容量决定且 N=100,000 < K_base (12.4M)，则 LRU 缓存所有对象，K_LRU=100,000，T_LRU_global = 100,000 / 50,000,000 = 0.002 days (17.28 minutes)。

## Corrected Claim

全局平均驻留时间 T_LRU_global 的数值计算：T_LRU_global = K_LRU / R_total。若 K_LRU 由容量决定且 N=100,000 < K_base (12.4M)，则 LRU 缓存所有对象，K_LRU=100,000，T_LRU_global = 100,000 / 50,000,000 = 0.002 days (17.28 minutes)。

## Evidence

先验知识/题面给定，逻辑校验通过
