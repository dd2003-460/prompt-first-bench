# N36: Qwen3-27B (GQA, 8 KV heads, head_dim 128, 64 layers) 在 fp8 精度下，每 1k tokens 的 KV 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

Qwen3-27B (GQA, 8 KV heads, head_dim 128, 64 layers) 在 fp8 精度下，每 1k tokens 的 KV Cache 占用量为 128MB (计算: 2 * 8 heads * 128 dim * 64 layers * 1 byte)，因此在 262k 上下文下，单序列 KV Cache 占用为 33.5GB，远超单卡 16GB 显存，证实必须依赖 PagedAttention 或 offloading。

## Corrected Claim

Qwen3-27B (GQA, 8 KV heads, head_dim 128, 64 layers) 在 fp8 精度下，每 1k tokens 的 KV Cache 占用量为 128MB (计算: 2 * 8 heads * 128 dim * 64 layers * 1 byte)，因此在 262k 上下文下，单序列 KV Cache 占用为 33.5GB，远超单卡 16GB 显存，证实必须依赖 PagedAttention 或 offloading。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 计算公式正确（2 * 8 * 128 * 64 * 1 = 131,072 bytes ≈ 128KB per token），262k tokens 总占用约 33.5GB，远超 16GB 显存，结论合理。
