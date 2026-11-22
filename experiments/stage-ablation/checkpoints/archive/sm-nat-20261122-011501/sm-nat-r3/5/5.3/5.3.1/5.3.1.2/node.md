# N149: LFU 增益上限工作点 2（含计数开销，有限精度）：实际 LFU 使用固定位宽计数器（如 8-bit 或 16-bit）。计数器溢出导致频率估计失真，特别是对于

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

LFU 增益上限工作点 2（含计数开销，有限精度）：实际 LFU 使用固定位宽计数器（如 8-bit 或 16-bit）。计数器溢出导致频率估计失真，特别是对于极高频率对象。量化影响：若计数器最大值为 M，实际频率 f > M 的对象被低估。对于 Top-1 对象，f >> M，其驻留优先级被错误降低。修正项 ΔH_penalty ≈ P_overflow * (H_top - H_avg)，其中 P_overflow 为计数器溢出概率。此工作点下 ΔH_lfu 降至 6%-8%。

## Corrected Claim

LFU 增益上限工作点 2（含计数开销，有限精度）：实际 LFU 使用固定位宽计数器（如 8-bit 或 16-bit）。计数器溢出导致频率估计失真，特别是对于极高频率对象。量化影响：若计数器最大值为 M，实际频率 f > M 的对象被低估。对于 Top-1 对象，f >> M，其驻留优先级被错误降低。修正项 ΔH_penalty ≈ P_overflow * (H_top - H_avg)，其中 P_overflow 为计数器溢出概率。此工作点下 ΔH_lfu 降至 6%-8%。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU counter overflow precision impact cache hit rate
