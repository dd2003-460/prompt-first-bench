# N577: 工作点2（中性价比/中负载骨干）：L_hop_p99 ≈ 20ms，发生概率 p_mid ≈ 0.09，对整体P99延迟贡献权重 W ≈ 0.09 * 20ms

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N188

## Claim

工作点2（中性价比/中负载骨干）：L_hop_p99 ≈ 20ms，发生概率 p_mid ≈ 0.09，对整体P99延迟贡献权重 W ≈ 0.09 * 20ms。

## Corrected Claim

工作点2（中性价比/中负载骨干）：L_hop_p99 ≈ 20ms，发生概率 p_mid ≈ 0.09，对整体P99延迟贡献权重 W ≈ 0.09 * 20ms。

## Evidence

先验知识/题面给定，逻辑校验通过：权重计算 W = p * L 符合概率加权延迟贡献的基本定义，数值量级合理。
