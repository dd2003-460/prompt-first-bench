# N137: LRU 策略下缓存集合的字节覆盖率 H_byte 的数值估算：基于 N97-N99 的条件期望结果，H_byte = Σ_{i: r_i > r_thresho

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

LRU 策略下缓存集合的字节覆盖率 H_byte 的数值估算：基于 N97-N99 的条件期望结果，H_byte = Σ_{i: r_i > r_threshold} (r_i * s_i) / Σ_{j=1}^N (r_j * s_j)，其中分子需通过数值积分 ∫_{r_threshold}^{∞} ∫_{s_min}^{s_max} r * s * f_{r,s}(r,s) dr ds 计算，分母由 N60 确定。

## Corrected Claim

LRU 策略下缓存集合的字节覆盖率 H_byte 的数值估算：基于 N97-N99 的条件期望结果，H_byte = Σ_{i: r_i > r_threshold} (r_i * s_i) / Σ_{j=1}^N (r_j * s_j)，其中分子需通过数值积分 ∫_{r_threshold}^{∞} ∫_{s_min}^{s_max} r * s * f_{r,s}(r,s) dr ds 计算，分母由 N60 确定。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

byte hit rate calculation cache LRU
