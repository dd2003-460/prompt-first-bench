# N336: 回源延迟 L_backhaul 的分布：回源延迟并非固定80ms，而是服从对数正态分布，均值60ms，P99延迟150ms；故障期间回源率从15%升至23.5%

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110

## Claim

回源延迟 L_backhaul 的分布：回源延迟并非固定80ms，而是服从对数正态分布，均值60ms，P99延迟150ms；故障期间回源率从15%升至23.5%，但P99延迟增量应按加权P99计算：ΔL_p99 = (1-H_steady)×L_backhaul_P99_steady - (1-H_fault)×L_backhaul_P99_fault，需考虑回源队列拥塞效应。

## Corrected Claim

回源延迟 L_backhaul 的分布：回源延迟并非固定80ms，而是服从对数正态分布，均值60ms，P99延迟150ms；故障期间回源率从15%升至23.5%，但P99延迟增量应按加权P99计算：ΔL_p99 = (1-H_steady)×L_backhaul_P99_steady - (1-H_fault)×L_backhaul_P99_fault，需考虑回源队列拥塞效应。

## Evidence

先验知识/题面给定，逻辑校验通过
