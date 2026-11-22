# N29: LRU 缓存中对象的平均驻留时间 T_res 近似等于缓存总容量字节数除以单位时间内的未命中字节流量：T_res ≈ C / (R_total * (1 - H

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

LRU 缓存中对象的平均驻留时间 T_res 近似等于缓存总容量字节数除以单位时间内的未命中字节流量：T_res ≈ C / (R_total * (1 - H_byte) * E[S_miss])，其中 H_byte 为字节命中率，E[S_miss] 为未命中对象的平均大小。

## Corrected Claim

LRU 缓存中对象的平均驻留时间 T_res 近似等于缓存总容量字节数除以单位时间内的未命中字节流量：T_res ≈ C / (R_total * (1 - H_byte) * E[S_miss])，其中 H_byte 为字节命中率，E[S_miss] 为未命中对象的平均大小。

## Evidence

先验知识/题面给定，逻辑校验通过
