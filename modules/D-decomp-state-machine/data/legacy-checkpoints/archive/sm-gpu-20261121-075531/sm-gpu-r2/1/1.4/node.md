# N9: 单卡显存硬性门槛 = 权重显存 + KV Cache显存 + 激活开销; BF16需≥58GB (排除所有消费级卡), INT8/FP8需≥31GB (需48G

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

单卡显存硬性门槛 = 权重显存 + KV Cache显存 + 激活开销; BF16需≥58GB (排除所有消费级卡), INT8/FP8需≥31GB (需48GB卡或双卡), W4需≥17GB (需24GB卡)

## Corrected Claim

单卡显存硬性门槛 = 权重显存 + KV Cache显存 + 激活开销; BF16需≥58GB (排除所有消费级卡), INT8/FP8需≥31GB (需48GB卡或双卡), W4需≥17GB (需24GB卡)

## Evidence

父节点级核验未通过：不完备（子节点之间正交（分别针对INT8/FP8和W4精度），无冗余。但不完备：父节点明确列出了BF16需≥58GB这一关键门槛，而子节点中完全缺失了BF16精度的计算与硬件匹配分析，导致覆盖不全。）
