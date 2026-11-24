# N237: 当核心区域流量占比 P_core = 0.95 时，P99 分位数落入长尾区域分布区间，P99_mix ≈ P99_tail（假设 P99_tail=200ms

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62, N63, N68

## Claim

当核心区域流量占比 P_core = 0.95 时，P99 分位数落入长尾区域分布区间，P99_mix ≈ P99_tail（假设 P99_tail=200ms），计算值为 200ms。

## Corrected Claim

当核心区域流量占比 P_core = 0.95 时，P99 分位数落入长尾区域分布区间，P99_mix ≈ P99_tail（假设 P99_tail=200ms），计算值为 200ms。

## Evidence

先验知识/题面给定，逻辑校验通过：当核心区域流量占比高达95%时，P99分位数（第99百分位）必然落在剩余的5%长尾区域中，因此混合分布的P99近似等于长尾区域的P99，数值推导自洽。
