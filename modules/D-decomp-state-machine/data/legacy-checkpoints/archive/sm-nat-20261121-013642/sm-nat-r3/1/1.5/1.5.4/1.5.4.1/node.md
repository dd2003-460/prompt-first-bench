# N136: 字节覆盖率 H_byte 与对象数量覆盖率 H_obj 的差距量化：ΔCov = H_byte - H_obj = (Σ_{i∈Cache} r_i s_i /

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

字节覆盖率 H_byte 与对象数量覆盖率 H_obj 的差距量化：ΔCov = H_byte - H_obj = (Σ_{i∈Cache} r_i s_i / Σ_{j} r_j s_j) - (K/N)，在 LRU 策略下，由于缓存偏向高热度小对象，H_byte 通常低于 H_obj，具体差距需通过数值积分计算 Σ_{i∈Cache} r_i s_i 和 Σ_{j} r_j s_j。

## Corrected Claim

字节覆盖率 H_byte 与对象数量覆盖率 H_obj 的差距量化：ΔCov = H_byte - H_obj = (Σ_{i∈Cache} r_i s_i / Σ_{j} r_j s_j) - (K/N)，在 LRU 策略下，由于缓存偏向高热度小对象，H_byte 通常低于 H_obj，具体差距需通过数值积分计算 Σ_{i∈Cache} r_i s_i 和 Σ_{j} r_j s_j。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cache hit rate byte vs object count difference
