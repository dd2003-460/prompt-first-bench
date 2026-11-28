# N518: 单卡 V100-16GB 在 TP=4 配置下，每张卡分配的 KV Cache 显存上限为 16GB × 0.85 (安全阈值) - 2GB (模型权重分片) 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N185

## Claim

单卡 V100-16GB 在 TP=4 配置下，每张卡分配的 KV Cache 显存上限为 16GB × 0.85 (安全阈值) - 2GB (模型权重分片) ≈ 11.6GB

## Corrected Claim

单卡 V100-16GB 在 TP=4 配置下，每张卡分配的 KV Cache 显存上限为 16GB × 0.85 (安全阈值) - 2GB (模型权重分片) ≈ 11.6GB

## Evidence

先验知识/题面给定，逻辑校验通过：16 * 0.85 = 13.6，13.6 - 2 = 11.6，计算无误且符合显存分配常规逻辑。
