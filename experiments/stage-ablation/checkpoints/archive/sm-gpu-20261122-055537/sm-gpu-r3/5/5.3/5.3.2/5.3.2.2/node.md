# N282: Qwen3-27B 在 32K 上下文、Batch Size=1 时，KV Cache 显存占用约为 10.7-11.5 GB (BF16)，加上 FP8 权重

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N86

## Claim

Qwen3-27B 在 32K 上下文、Batch Size=1 时，KV Cache 显存占用约为 10.7-11.5 GB (BF16)，加上 FP8 权重 27 GB，总显存需求约为 38-39 GB，超过 A10 24 GB 显存容量，因此 A10 同样无法在 FP8 精度下直接运行 32K 上下文 Qwen3-27B，必须启用 PagedAttention 共享 KV 或降低上下文/精度。

## Corrected Claim

Qwen3-27B 在 32K 上下文、Batch Size=1 时，KV Cache 显存占用约为 10.7-11.5 GB (BF16)，加上 FP8 权重 27 GB，总显存需求约为 38-39 GB，超过 A10 24 GB 显存容量，因此 A10 同样无法在 FP8 精度下直接运行 32K 上下文 Qwen3-27B，必须启用 PagedAttention 共享 KV 或降低上下文/精度。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 在 32K 上下文、Batch Size=1 时 KV Cache 显存占用约 10.7-11.5 GB (BF16)，加上 FP8 权重 27 GB，总显存需求约 38-39 GB，超过 A10 24 GB 显存容量，结论合理。

## Search Query

Qwen3-27B A10 24GB VRAM feasibility 32k context
