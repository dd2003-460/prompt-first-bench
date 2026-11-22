# N166: 分母项1（独立基准流量）：R_byte_indep = N * E[λ] * E[S] = 10^5 * 500 * 11264 ≈ 5.63×10^11 by

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

分母项1（独立基准流量）：R_byte_indep = N * E[λ] * E[S] = 10^5 * 500 * 11264 ≈ 5.63×10^11 bytes/day。此为未考虑大小-热度相关的总字节流量基准，作为修正项的乘数基底。

## Corrected Claim

分母项1（独立基准流量）：R_byte_indep = N * E[λ] * E[S] = 10^5 * 500 * 11264 ≈ 5.63×10^11 bytes/day。此为未考虑大小-热度相关的总字节流量基准，作为修正项的乘数基底。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 10^5 * 500 * 11264 = 5.632 * 10^11，与陈述中的 5.63×10^11 一致，量纲（bytes/day）合理。
