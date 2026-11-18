# N95: 当 K_avg > N 时，LRU 字节命中率下界由“是否所有对象都能驻留”决定，由于 Σ_{i=1}^{N} S_i 需与 C 比较，若总数据量 Σ S_i 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

当 K_avg > N 时，LRU 字节命中率下界由“是否所有对象都能驻留”决定，由于 Σ_{i=1}^{N} S_i 需与 C 比较，若总数据量 Σ S_i < C，则 H_byte = 1.0；需计算 Σ_{i=1}^{100,000} S_i 在 x_min=100B 下的总值。

## Corrected Claim

当 K_avg > N 时，LRU 字节命中率下界由“是否所有对象都能驻留”决定，由于 Σ_{i=1}^{N} S_i 需与 C 比较，若总数据量 Σ S_i < C，则 H_byte = 1.0；需计算 Σ_{i=1}^{100,000} S_i 在 x_min=100B 下的总值。

## Evidence

先验知识/题面给定，逻辑校验通过
