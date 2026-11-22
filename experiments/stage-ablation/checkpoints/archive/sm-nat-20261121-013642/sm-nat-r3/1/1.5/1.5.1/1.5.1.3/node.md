# N129: K 与命中率的非线性关系：命中率 H_byte 随 K 的对数增长而增长，dH/dK ≈ (r_K * s_K) / R_total_bytes，当 K 较小时

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N42

## Claim

K 与命中率的非线性关系：命中率 H_byte 随 K 的对数增长而增长，dH/dK ≈ (r_K * s_K) / R_total_bytes，当 K 较小时（如 <100），每增加一个对象带来的命中率增益显著，当 K 较大时（如 >1000），增益趋于饱和，边际效用递减。

## Corrected Claim

K 与命中率的非线性关系：命中率 H_byte 随 K 的对数增长而增长，dH/dK ≈ (r_K * s_K) / R_total_bytes，当 K 较小时（如 <100），每增加一个对象带来的命中率增益显著，当 K 较大时（如 >1000），增益趋于饱和，边际效用递减。

## Evidence

先验知识/题面给定，逻辑校验通过
