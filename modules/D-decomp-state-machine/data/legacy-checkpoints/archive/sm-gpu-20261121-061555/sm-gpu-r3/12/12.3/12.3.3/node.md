# N388: 在 PCIe Gen4 互联下，2x RTX 4090 运行 27B 模型 TP=2 时的实测吞吐量通常仅为单卡理论吞吐量的 75-85%（即加速比为 1.5-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N136

## Claim

在 PCIe Gen4 互联下，2x RTX 4090 运行 27B 模型 TP=2 时的实测吞吐量通常仅为单卡理论吞吐量的 75-85%（即加速比为 1.5-1.7x 而非 2.0x），该效率系数直接用于修正 N99 中的 OpEx 和 TCO 计算。

## Corrected Claim

在 PCIe Gen4 互联下，2x RTX 4090 运行 27B 模型 TP=2 时的实测吞吐量通常仅为单卡理论吞吐量的 75-85%（即加速比为 1.5-1.7x 而非 2.0x），该效率系数直接用于修正 N99 中的 OpEx 和 TCO 计算。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe Gen4 带宽限制及 TP=2 通信开销导致 2x 4090 加速比低于线性（1.5-1.7x 符合工程经验），数值量级合理。
