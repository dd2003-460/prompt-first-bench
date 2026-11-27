# N95: 不同精度下的TPS量化对比：基于带宽受限假设，BF16 (54GB权重) 的TPS理论值约为 FP8 (27GB权重) 的1/2，INT4 (13.5GB权重)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

不同精度下的TPS量化对比：基于带宽受限假设，BF16 (54GB权重) 的TPS理论值约为 FP8 (27GB权重) 的1/2，INT4 (13.5GB权重) 的TPS理论值约为 BF16 的4倍（忽略KV Cache精度变化及计算开销差异）。

## Corrected Claim

不同精度下的TPS量化对比：基于带宽受限假设，BF16 (54GB权重) 的TPS理论值约为 FP8 (27GB权重) 的1/2，INT4 (13.5GB权重) 的TPS理论值约为 BF16 的4倍（忽略KV Cache精度变化及计算开销差异）。

## Evidence

先验知识/题面给定，逻辑校验通过：在带宽受限且忽略计算开销差异的假设下，TPS与模型权重大小成反比，54GB/27GB=2，54GB/13.5GB=4，数值推导自洽。
