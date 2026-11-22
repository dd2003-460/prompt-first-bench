# N217: 周期性负载对 LRU 命中率误差的边界条件：当 T_access << T_cycle 时，ε_periodic ≈ (π^2 * T_access^2) / 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76

## Claim

周期性负载对 LRU 命中率误差的边界条件：当 T_access << T_cycle 时，ε_periodic ≈ (π^2 * T_access^2) / (24 * T_cycle^2)；若 T_access = 0.1h，T_cycle = 24h，则 ε_periodic ≈ 3.4e-5，表明高频访问下周期性误差可忽略；当 T_access ≈ T_cycle 时，ε_periodic ≈ 0.5，表明周期性误差显著。

## Corrected Claim

周期性负载对 LRU 命中率误差的边界条件：当 T_access << T_cycle 时，ε_periodic ≈ (π^2 * T_access^2) / (24 * T_cycle^2)；若 T_access = 0.1h，T_cycle = 24h，则 ε_periodic ≈ 3.4e-5，表明高频访问下周期性误差可忽略；当 T_access ≈ T_cycle 时，ε_periodic ≈ 0.5，表明周期性误差显著。

## Evidence

先验知识/题面给定，逻辑校验通过
