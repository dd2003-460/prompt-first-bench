# N672: 核心区域 P99_RTT_core 的修正公式：P99_RTT_core = 0.05 * D_core_p99 + 5 + ΔT_cross_core + J

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N223

## Claim

核心区域 P99_RTT_core 的修正公式：P99_RTT_core = 0.05 * D_core_p99 + 5 + ΔT_cross_core + Jitter_P99，其中 Jitter_P99 为核心区域网络抖动 P99 值，通常为 5-10ms，导致总 P99 约为 20-30ms 而非简单的 25ms。

## Corrected Claim

核心区域 P99_RTT_core 的修正公式：P99_RTT_core = 0.05 * D_core_p99 + 5 + ΔT_cross_core + Jitter_P99，其中 Jitter_P99 为核心区域网络抖动 P99 值，通常为 5-10ms，导致总 P99 约为 20-30ms 而非简单的 25ms。

## Evidence

先验知识/题面给定，逻辑校验通过
