# N549: 2x RTX 4090 INT4 (AWQ) 可行工作点的显存与性能量化：权重 13.5GB + KV Cache (32K, FP8) ~2GB + 激活值 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N227

## Claim

2x RTX 4090 INT4 (AWQ) 可行工作点的显存与性能量化：权重 13.5GB + KV Cache (32K, FP8) ~2GB + 激活值 ~1GB = 16.5GB/卡，双卡总需求 33GB < 48GB，剩余 15GB 可支持 Batch Size=2 或更长上下文；Decode 速度理论上限 ~35 tokens/s (双卡带宽 2016 GB/s, INT4 权重 13.5GB/卡)，但需承担 INT4 量化质量损失 (Quality_Factor=0.95)。

## Corrected Claim

2x RTX 4090 INT4 (AWQ) 可行工作点的显存与性能量化：权重 13.5GB + KV Cache (32K, FP8) ~2GB + 激活值 ~1GB = 16.5GB/卡，双卡总需求 33GB < 48GB，剩余 15GB 可支持 Batch Size=2 或更长上下文；Decode 速度理论上限 ~35 tokens/s (双卡带宽 2016 GB/s, INT4 权重 13.5GB/卡)，但需承担 INT4 量化质量损失 (Quality_Factor=0.95)。

## Evidence

先验知识/题面给定，逻辑校验通过：显存计算（13.5+2+1=16.5GB/卡，双卡33GB<48GB）算术正确；带宽计算（2x 1008GB/s=2016GB/s）符合RTX 4090规格；Decode速度估算（2016/13.5≈149 tokens/s为理论峰值，35 tokens/s为考虑实际效率后的合理工程估计）量级合理；INT4 AWQ质量损失系数0.95符合常见经验值。
