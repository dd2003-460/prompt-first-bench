# N176: 尾部修正系数 k_tail 的量化推导：N54假设 k_tail = 1.2-1.5。更精确地，若 P99_remote = 150ms，P99_city = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

尾部修正系数 k_tail 的量化推导：N54假设 k_tail = 1.2-1.5。更精确地，若 P99_remote = 150ms，P99_city = 12.5ms，且偏远地区占20%流量，则全局P99 ≈ P99_remote * (0.99/0.2)^{1/2} (近似对数正态尾部行为)。实际上，若偏远地区未命中请求的P99为 200ms，则全局P99 可能接近 180-200ms，而非简单的 150 * 1.2 = 180ms。需基于具体分布参数计算。

## Corrected Claim

尾部修正系数 k_tail 的量化推导：N54假设 k_tail = 1.2-1.5。更精确地，若 P99_remote = 150ms，P99_city = 12.5ms，且偏远地区占20%流量，则全局P99 ≈ P99_remote * (0.99/0.2)^{1/2} (近似对数正态尾部行为)。实际上，若偏远地区未命中请求的P99为 200ms，则全局P99 可能接近 180-200ms，而非简单的 150 * 1.2 = 180ms。需基于具体分布参数计算。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

tail risk amplification in mixed population latency
