# N78: 在 FP8 (E4M3) 精度下，Qwen3-27B 模型权重占用显存约为 27 GB，加上 32K 上下文 KV Cache (约 1.57 GB，假设 BF

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

在 FP8 (E4M3) 精度下，Qwen3-27B 模型权重占用显存约为 27 GB，加上 32K 上下文 KV Cache (约 1.57 GB，假设 BF16 KV) 及激活值开销，总显存占用约 30-31 GB，接近 32 GB 上限，导致可用显存极度紧张

## Corrected Claim

在 FP8 (E4M3) 精度下，Qwen3-27B 模型权重占用显存约为 27 GB，加上 32K 上下文 KV Cache (约 1.57 GB，假设 BF16 KV) 及激活值开销，总显存占用约 30-31 GB，接近 32 GB 上限，导致可用显存极度紧张

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在FP8下约27GB，32K上下文KV Cache在BF16下约1.57GB，加上激活值开销，总显存占用约30-31GB，符合32GB显存卡的容量限制。
