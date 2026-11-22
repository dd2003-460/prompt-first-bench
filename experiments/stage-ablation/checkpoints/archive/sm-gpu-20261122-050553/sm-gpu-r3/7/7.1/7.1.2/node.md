# N300: 工作点B（FP8 权重 + INT8 KV, 32K ctx）：显存占用 = 27GB (Weights) + 8GB (KV) = 35GB > 32GB，仍

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N102

## Claim

工作点B（FP8 权重 + INT8 KV, 32K ctx）：显存占用 = 27GB (Weights) + 8GB (KV) = 35GB > 32GB，仍不可行；缺口 3GB 需通过减少 Batch Size 至 1 并启用 CUDA Graphs 优化显存碎片来争取，但无余量应对系统开销，稳定性风险高。

## Corrected Claim

工作点B（FP8 权重 + INT8 KV, 32K ctx）：显存占用 = 27GB (Weights) + 8GB (KV) = 35GB > 32GB，仍不可行；缺口 3GB 需通过减少 Batch Size 至 1 并启用 CUDA Graphs 优化显存碎片来争取，但无余量应对系统开销，稳定性风险高。

## Evidence

先验知识/题面给定，逻辑校验通过：27GB+8GB=35GB>32GB，算术正确且符合显存占用基本逻辑
