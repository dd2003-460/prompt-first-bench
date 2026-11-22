# N14: 一致性未命中率 M_invalidation 的量化推导：基于1%/天的更新率，假设对象更新服从泊松过程，M_invalidation ≈ 1 - exp(-λ

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

一致性未命中率 M_invalidation 的量化推导：基于1%/天的更新率，假设对象更新服从泊松过程，M_invalidation ≈ 1 - exp(-λ_update * T_resident)，其中 T_resident 为对象在缓存中的平均驻留时间，需结合LRU的驱逐策略估算 T_resident。

## Corrected Claim

一致性未命中率 M_invalidation 的量化推导：基于1%/天的更新率，假设对象更新服从泊松过程，M_invalidation ≈ 1 - exp(-λ_update * T_resident)，其中 T_resident 为对象在缓存中的平均驻留时间，需结合LRU的驱逐策略估算 T_resident。

## Evidence

先验知识/题面给定，逻辑校验通过：泊松过程下对象在时间T内未被更新的概率为exp(-λT)，故被更新（导致失效）的概率为1-exp(-λT)，公式推导符合概率论基本原理。
