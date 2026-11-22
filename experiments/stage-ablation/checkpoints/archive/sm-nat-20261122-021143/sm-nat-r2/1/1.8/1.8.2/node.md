# N40: 平均驻留时间 T_c 的计算：T_c = C_total / (R_cached * S_avg_cached)，其中 C_total=128GB，R_cach

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

平均驻留时间 T_c 的计算：T_c = C_total / (R_cached * S_avg_cached)，其中 C_total=128GB，R_cached 为缓存内对象总请求率，S_avg_cached 为缓存内对象平均大小 [待核验]

## Corrected Claim

平均驻留时间 T_c 的计算：T_c = C_total / (R_cached * S_avg_cached)，其中 C_total=128GB，R_cached 为缓存内对象总请求率，S_avg_cached 为缓存内对象平均大小 [待核验]

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cache average residence time calculation formula LRU LFU
