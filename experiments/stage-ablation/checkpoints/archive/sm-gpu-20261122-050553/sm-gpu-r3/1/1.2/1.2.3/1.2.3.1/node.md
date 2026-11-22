# N134: 修正自矛盾检测：RTX 4060 Ti 16GB 在 LLM 推理负载下的平均功耗 P_avg 并非满载 160W，而是随负载在 80-160W 之间波动，保守

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N42

## Claim

修正自矛盾检测：RTX 4060 Ti 16GB 在 LLM 推理负载下的平均功耗 P_avg 并非满载 160W，而是随负载在 80-160W 之间波动，保守估计取 120W 用于 TCO 计算，以反映长上下文推理中显存读取主导的低功耗特性。

## Corrected Claim

修正自矛盾检测：RTX 4060 Ti 16GB 在 LLM 推理负载下的平均功耗 P_avg 并非满载 160W，而是随负载在 80-160W 之间波动，保守估计取 120W 用于 TCO 计算，以反映长上下文推理中显存读取主导的低功耗特性。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4060 Ti TDP为160W，LLM推理显存带宽受限导致功耗低于峰值，120W为合理保守估计。
