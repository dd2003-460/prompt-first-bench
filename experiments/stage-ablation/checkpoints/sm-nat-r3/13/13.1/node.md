# N194: 缓存内对象平均驻留时间 T_res 在稳态下近似为缓存容量 C 除以平均对象大小 S_avg 与平均未命中请求率 R_miss 的乘积，即 T_res ≈ C 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

缓存内对象平均驻留时间 T_res 在稳态下近似为缓存容量 C 除以平均对象大小 S_avg 与平均未命中请求率 R_miss 的乘积，即 T_res ≈ C / (S_avg * R_miss)，其中 R_miss = R_total * (1 - H_base)。

## Corrected Claim

缓存内对象平均驻留时间 T_res 在稳态下近似为缓存容量 C 除以平均对象大小 S_avg 与平均未命中请求率 R_miss 的乘积，即 T_res ≈ C / (S_avg * R_miss)，其中 R_miss = R_total * (1 - H_base)。

## Evidence

先验知识/题面给定，逻辑校验通过
