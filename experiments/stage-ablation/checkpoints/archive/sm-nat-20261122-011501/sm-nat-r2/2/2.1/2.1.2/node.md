# N35: LRU驻留集合的驱逐边界条件：当对象i的访问间隔Δt_i > T_res（缓存平均驻留时间）时，该对象被驱逐；T_res = 128GB / (Miss_Byt

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

LRU驻留集合的驱逐边界条件：当对象i的访问间隔Δt_i > T_res（缓存平均驻留时间）时，该对象被驱逐；T_res = 128GB / (Miss_Bytes_Rate)，其中Miss_Bytes_Rate为未命中请求带来的字节写入速率，需迭代求解以闭合命中率方程。

## Corrected Claim

LRU驻留集合的驱逐边界条件：当对象i的访问间隔Δt_i > T_res（缓存平均驻留时间）时，该对象被驱逐；T_res = 128GB / (Miss_Bytes_Rate)，其中Miss_Bytes_Rate为未命中请求带来的字节写入速率，需迭代求解以闭合命中率方程。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU缓存的驱逐机制确实基于访问间隔与驻留时间的比较，且驻留时间由缓存容量与写入速率决定，需迭代求解以闭合命中率方程，符合缓存理论基本逻辑。
