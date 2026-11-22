# N91: 对象在 LRU 缓存中的平均驻留时间 T_residence 的精确计算公式为 T_residence = (C_cache * H_byte_LRU) / R

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N30

## Claim

对象在 LRU 缓存中的平均驻留时间 T_residence 的精确计算公式为 T_residence = (C_cache * H_byte_LRU) / R_bytes_miss，其中 C_cache=128GB, R_bytes_miss 为每日缓存未命中的字节流量，需先由 N9/N10 确定 H_byte_LRU 和 R_bytes_miss 的数值。

## Corrected Claim

对象在 LRU 缓存中的平均驻留时间 T_residence 的精确计算公式为 T_residence = (C_cache * H_byte_LRU) / R_bytes_miss，其中 C_cache=128GB, R_bytes_miss 为每日缓存未命中的字节流量，需先由 N9/N10 确定 H_byte_LRU 和 R_bytes_miss 的数值。

## Evidence

先验知识/题面给定，逻辑校验通过：根据利特尔法则（Little's Law）或流量守恒原理，平均驻留时间 = 缓存中平均数据量 / 流出速率（即未命中流量），公式量纲与逻辑自洽。
