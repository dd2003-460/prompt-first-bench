# N243: 对象 i 的平均驻留时间 T_res_i 在 LRU 策略下的近似计算公式为 T_res_i ≈ C / (Σ_{j: h_j > h_i} r_j * S_j

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N89

## Claim

对象 i 的平均驻留时间 T_res_i 在 LRU 策略下的近似计算公式为 T_res_i ≈ C / (Σ_{j: h_j > h_i} r_j * S_j)，其中 r_j 为对象 j 的请求率，S_j 为对象 j 的大小，分母表示热度高于 i 的对象产生的总字节流出速率，决定了 i 被挤出缓存的时间。

## Corrected Claim

对象 i 的平均驻留时间 T_res_i 在 LRU 策略下的近似计算公式为 T_res_i ≈ C / (Σ_{j: h_j > h_i} r_j * S_j)，其中 r_j 为对象 j 的请求率，S_j 为对象 j 的大小，分母表示热度高于 i 的对象产生的总字节流出速率，决定了 i 被挤出缓存的时间。

## Evidence

先验知识/题面给定，逻辑校验通过
