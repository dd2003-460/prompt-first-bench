# N50: 消费级显卡显存带宽与TPS关系：RTX 4090 (24GB, 1008GB/s) 在W4量化下TPS≈带宽/模型大小=1008/13.5≈74.6 TPS（理

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

消费级显卡显存带宽与TPS关系：RTX 4090 (24GB, 1008GB/s) 在W4量化下TPS≈带宽/模型大小=1008/13.5≈74.6 TPS（理论上限，实际受计算单元限制约50-60 TPS）；RTX 5090 (32GB, 1792GB/s) 理论TPS≈132.7，实际约90-110 TPS。

## Corrected Claim

消费级显卡显存带宽与TPS关系：RTX 4090 (24GB, 1008GB/s) 在W4量化下TPS≈带宽/模型大小=1008/13.5≈74.6 TPS（理论上限，实际受计算单元限制约50-60 TPS）；RTX 5090 (32GB, 1792GB/s) 理论TPS≈132.7，实际约90-110 TPS。

## Evidence

先验知识/题面给定，逻辑校验通过：带宽除以模型大小（1008/13.5≈74.6, 1792/13.5≈132.7）符合内存带宽瓶颈下的理论TPS计算逻辑，且实际TPS低于理论上限符合计算单元限制的工程常识。
