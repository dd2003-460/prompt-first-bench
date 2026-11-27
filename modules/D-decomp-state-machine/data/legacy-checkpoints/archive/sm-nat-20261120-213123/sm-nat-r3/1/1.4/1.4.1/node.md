# N29: LRU 缓存中对象的平均驻留时间 T_res 近似等于缓存总容量字节数除以单位时间内的未命中字节流量：T_res ≈ C / (R_total * (1 - H

- **status**: pending
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

父节点级核验未通过：非正交, 不完备, 有冗余（子节点本质上是同一公式在不同参数取值下的计算实例，存在严重冗余；且未覆盖公式推导、变量定义或理论边界等关键方面，完备性不足。）
