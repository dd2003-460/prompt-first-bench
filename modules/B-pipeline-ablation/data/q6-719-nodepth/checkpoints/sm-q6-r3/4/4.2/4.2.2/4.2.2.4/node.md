# N340: 缓存一致性开销对有效命中率的影响：多POP环境下的缓存失效（Eviction）率 E_rate 与写入频率 Q_write 成正比，E_rate ≈ Q_wri

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N105

## Claim

缓存一致性开销对有效命中率的影响：多POP环境下的缓存失效（Eviction）率 E_rate 与写入频率 Q_write 成正比，E_rate ≈ Q_write / (C_pop_total * TTL_avg)，导致有效命中率 H_pop_eff = H_pop * (1 - E_rate)，典型 E_rate 为 0.01-0.05。

## Corrected Claim

缓存一致性开销对有效命中率的影响：多POP环境下的缓存失效（Eviction）率 E_rate 与写入频率 Q_write 成正比，E_rate ≈ Q_write / (C_pop_total * TTL_avg)，导致有效命中率 H_pop_eff = H_pop * (1 - E_rate)，典型 E_rate 为 0.01-0.05。

## Evidence

先验知识/题面给定，逻辑校验通过
