# N236: 当核心区域流量占比 P_core = 0.99 时，混合策略 P99 延迟由核心区域主导，P99_mix ≈ P99_core（假设 P99_core=100m

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62, N63, N68

## Claim

当核心区域流量占比 P_core = 0.99 时，混合策略 P99 延迟由核心区域主导，P99_mix ≈ P99_core（假设 P99_core=100ms, P99_tail=200ms），计算值为 100ms。

## Corrected Claim

当核心区域流量占比 P_core = 0.99 时，混合策略 P99 延迟由核心区域主导，P99_mix ≈ P99_core（假设 P99_core=100ms, P99_tail=200ms），计算值为 100ms。

## Evidence

先验知识/题面给定，逻辑校验通过：在核心流量占比极高（99%）且核心延迟显著低于尾部延迟（100ms < 200ms）的情况下，混合策略的P99延迟确实由核心区域主导，近似等于核心P99延迟。
