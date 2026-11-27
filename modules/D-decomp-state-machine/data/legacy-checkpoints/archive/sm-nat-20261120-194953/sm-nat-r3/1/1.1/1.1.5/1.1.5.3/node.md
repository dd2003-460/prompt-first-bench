# N97: 修正后的头部对象字节贡献权重 W_hot_corrected = E[S|R ∈ Top10%] * P(R ∈ Top10% * N) / TotalByte

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

修正后的头部对象字节贡献权重 W_hot_corrected = E[S|R ∈ Top10%] * P(R ∈ Top10% * N) / TotalBytes，与独立假设下的 W_hot_indep = E[S] * P(R ∈ Top10% * N) / TotalBytes 的比值，该比值即为 LFU 策略中头部对象权重的修正因子，需计算具体数值。

## Corrected Claim

修正后的头部对象字节贡献权重 W_hot_corrected = E[S|R ∈ Top10%] * P(R ∈ Top10% * N) / TotalBytes，与独立假设下的 W_hot_indep = E[S] * P(R ∈ Top10% * N) / TotalBytes 的比值，该比值即为 LFU 策略中头部对象权重的修正因子，需计算具体数值。

## Evidence

先验知识/题面给定，逻辑校验通过
