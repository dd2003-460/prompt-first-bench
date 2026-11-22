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

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应父节点中明确忽略的三个关键修正维度：1. KV Cache 精度导致的带宽修正（显存/带宽维度）；2. 反量化带来的计算开销（计算/Compute-bound维度）；3. 硬件对特定精度的支持效率差异（硬件/效率维度）。三者维度正交，无重叠，且共同构成了从‘理论带宽模型’到‘实际硬件性能’的主要修正项，覆盖了父节点隐含的‘忽略项’。）
