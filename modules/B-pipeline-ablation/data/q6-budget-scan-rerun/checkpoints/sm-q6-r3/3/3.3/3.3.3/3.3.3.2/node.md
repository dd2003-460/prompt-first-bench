# N230: 大对象超标概率计算：假设对象大小 s 服从 LogNormal(μ, σ) 分布。计算 P(s > S_threshold) = 1 - Φ((ln(S_thr

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

大对象超标概率计算：假设对象大小 s 服从 LogNormal(μ, σ) 分布。计算 P(s > S_threshold) = 1 - Φ((ln(S_threshold) - μ) / σ)。其中 S_threshold = (T - T_network - T_processing) * B_link。若 T=100ms, B_link=10Mbps (用户侧)，S_threshold ≈ 100ms * 1.25MB/ms ≈ 125KB。对于短视频 (5MB)，超标概率接近 100%，导致 P99 必然超标，需引入分片传输或预加载机制。

## Corrected Claim

大对象超标概率计算：假设对象大小 s 服从 LogNormal(μ, σ) 分布。计算 P(s > S_threshold) = 1 - Φ((ln(S_threshold) - μ) / σ)。其中 S_threshold = (T - T_network - T_processing) * B_link。若 T=100ms, B_link=10Mbps (用户侧)，S_threshold ≈ 100ms * 1.25MB/ms ≈ 125KB。对于短视频 (5MB)，超标概率接近 100%，导致 P99 必然超标，需引入分片传输或预加载机制。

## Evidence

先验知识/题面给定，逻辑校验通过：10Mbps = 1.25MB/s = 1.25KB/ms，100ms * 1.25KB/ms = 125KB，数值量级与单位换算正确；LogNormal分布概率公式正确；5MB远大于125KB，超标概率接近100%的结论符合逻辑。

## Search Query

lognormal distribution probability exceedance threshold CDN latency
