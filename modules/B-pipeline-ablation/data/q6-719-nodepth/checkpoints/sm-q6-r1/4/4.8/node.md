# N32: 混合策略的P99延迟为加权最大值：P99_mix = max(P99_core, P99_tail)，其中P99_core对应自建POP区域，P99_tail对

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

混合策略的P99延迟为加权最大值：P99_mix = max(P99_core, P99_tail)，其中P99_core对应自建POP区域，P99_tail对应公有云CDN区域，权重由流量占比 P_core 和 (1-P_core) 决定。

## Corrected Claim

混合策略的P99延迟通常介于 P99_core 和 P99_tail 之间，具体数值取决于流量占比及两个区域延迟分布的具体形态，不能简单等同于加权最大值。

## Evidence

[质询]P99延迟是尾部指标，不具备线性可加性或简单的加权最大值性质。混合系统的P99取决于流量分布与延迟分布的卷积，通常 P99_mix 会介于 P99_core 和 P99_tail 之间（若两者分布不同），或者接近较大值但受流量占比影响，直接断言等于 max(P99_core, P99_tail) 在统计学上是不严谨的，除非假设两个区域的延迟分布完全相同或存在特定的极端分布假设。 | 先验知识/题面给定，逻辑校验发现P99作为分位数指标，其混合值不能简单由加权最大值定义，存在逻辑漏洞。
