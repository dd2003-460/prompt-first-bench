# N50: 消费级显卡显存带宽与TPS关系：RTX 4090 (24GB, 1008GB/s) 在W4量化下TPS≈带宽/模型大小=1008/13.5≈74.6 TPS（理

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

消费级显卡显存带宽与TPS关系：RTX 4090 (24GB, 1008GB/s) 在W4量化下TPS≈带宽/模型大小=1008/13.5≈74.6 TPS（理论上限，实际受计算单元限制约50-60 TPS）；RTX 5090 (32GB, 1792GB/s) 理论TPS≈132.7，实际约90-110 TPS。

## Corrected Claim

消费级显卡显存带宽与TPS关系：RTX 4090 (24GB, 1008GB/s) 在W4量化下TPS≈带宽/模型大小=1008/13.5≈74.6 TPS（理论上限，实际受计算单元限制约50-60 TPS）；RTX 5090 (32GB, 1792GB/s) 理论TPS≈132.7，实际约90-110 TPS。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一物理公式（TPS = Bandwidth / Total_Memory_Required）在两个不同硬件实例上的应用，属于参数化重复而非正交分解；此外，父节点中提到的'计算单元限制'（Compute-Bound）仅在子节点2中作为修正因素提及，子节点1主要聚焦于Memory-Bound修正，导致对'实际受计算单元限制'这一关键维度的覆盖不一致且不完整。）
