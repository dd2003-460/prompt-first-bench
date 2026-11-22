# N273: 在缓存容量受限（C=128GB < V_total）的常态工作点下，对象 i 的驻留时间 T_res(s_i) 与其大小 s_i 呈负相关，近似关系为 T_re

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94

## Claim

在缓存容量受限（C=128GB < V_total）的常态工作点下，对象 i 的驻留时间 T_res(s_i) 与其大小 s_i 呈负相关，近似关系为 T_res(s_i) ≈ C / (r_byte_total * s_i)，其中 r_byte_total 为总字节请求率。

## Corrected Claim

在缓存容量受限（C=128GB < V_total）的常态工作点下，对象 i 的驻留时间 T_res(s_i) 与其大小 s_i 呈负相关，近似关系为 T_res(s_i) ≈ C / (r_byte_total * s_i)，其中 r_byte_total 为总字节请求率。

## Evidence

先验知识/题面给定，逻辑校验通过
