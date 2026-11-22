# N52: 缓存中 stale 对象的字节数计算：Stale_bytes = ∫_{age > T_update} S(k) * f_age(age) dk，其中 T_up

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

缓存中 stale 对象的字节数计算：Stale_bytes = ∫_{age > T_update} S(k) * f_age(age) dk，其中 T_update = 1 天，f_age(age) 是缓存中对象的年龄分布，需根据 LRU 驻留时间分布推导，而非简单用 128GB * 10%。

## Corrected Claim

缓存中 stale 对象的字节数计算：Stale_bytes = ∫_{age > T_update} S(k) * f_age(age) dk，其中 T_update = 1 天，f_age(age) 是缓存中对象的年龄分布，需根据 LRU 驻留时间分布推导，而非简单用 128GB * 10%。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式正确表达了基于年龄分布的积分计算逻辑，且明确指出了不能简单用总量乘以比例的错误做法，符合缓存管理理论。

## Search Query

stale data size calculation LRU cache age distribution
