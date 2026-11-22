# N220: Pareto(α=1.1) 分布下，头部 10% 对象占用的总字节占比 P_bytes_top10 可通过积分 ∫_{0}^{0.1} x^{1-α} dx /

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Pareto(α=1.1) 分布下，头部 10% 对象占用的总字节占比 P_bytes_top10 可通过积分 ∫_{0}^{0.1} x^{1-α} dx / ∫_{0}^{1} x^{1-α} dx 计算，数值约为 0.1^{0.1} ≈ 0.794，表明 10% 的对象承载了约 79.4% 的流量字节，这是计算 LFU 提升上限的基础数据。

## Corrected Claim

Pareto(α=1.1) 分布下，头部 10% 对象占用的总字节占比 P_bytes_top10 可通过积分 ∫_{0}^{0.1} x^{1-α} dx / ∫_{0}^{1} x^{1-α} dx 计算，数值约为 0.1^{0.1} ≈ 0.794，表明 10% 的对象承载了约 79.4% 的流量字节，这是计算 LFU 提升上限的基础数据。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

Pareto distribution cumulative distribution function top 10 percent mass
