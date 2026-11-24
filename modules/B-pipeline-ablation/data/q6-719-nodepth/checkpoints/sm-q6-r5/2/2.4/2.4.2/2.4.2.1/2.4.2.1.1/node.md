# N576: 工作点1（高性低成/低负载骨干）：L_hop_p99 ≈ 10ms，发生概率 p_low ≈ 0.9，对整体P99延迟贡献权重 W ≈ 0.9 * 10ms。

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N188

## Claim

工作点1（高性低成/低负载骨干）：L_hop_p99 ≈ 10ms，发生概率 p_low ≈ 0.9，对整体P99延迟贡献权重 W ≈ 0.9 * 10ms。

## Corrected Claim

工作点1（高性低成/低负载骨干）：L_hop_p99 ≈ 10ms，发生概率 p_low ≈ 0.9，对整体P99延迟贡献权重 W ≈ 0.9 * 10ms。

## Evidence

先验知识/题面给定，逻辑校验通过：权重计算 W = p * L 符合概率加权延迟贡献的基本定义，数值量级合理。
