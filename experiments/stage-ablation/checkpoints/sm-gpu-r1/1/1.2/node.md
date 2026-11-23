# N7: 消费级 GPU 候选集筛选：排除显存 < 48GB 的卡片（如 4090 24GB、3090 24GB）因无法容纳 BF16 权重+KV Cache；保留 50

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

消费级 GPU 候选集筛选：排除显存 < 48GB 的卡片（如 4090 24GB、3090 24GB）因无法容纳 BF16 权重+KV Cache；保留 5090 32GB（需量化至 FP8/INT8）及多卡组合方案。

## Corrected Claim

消费级 GPU 候选集筛选：排除显存 < 48GB 的卡片（如 4090 24GB、3090 24GB）因无法容纳 BF16 权重+KV Cache；保留 5090 32GB（需量化至 FP8/INT8）及多卡组合方案。

## Evidence

先验知识/题面给定，逻辑校验通过：48GB显存阈值符合大模型推理（BF16权重+KV Cache）的常规工程估算，5090 32GB需量化以适配显存限制符合硬件规格与模型部署逻辑。
