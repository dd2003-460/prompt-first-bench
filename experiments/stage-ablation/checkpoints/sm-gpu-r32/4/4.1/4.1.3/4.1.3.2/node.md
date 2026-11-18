# N175: Qwen3-27B 在 32K 上下文下的 KV Cache 显存占用计算：KV_Cache_Size = 2 * n_layers * n_heads * h

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

Qwen3-27B 在 32K 上下文下的 KV Cache 显存占用计算：KV_Cache_Size = 2 * n_layers * n_heads * head_dim * seq_len * 2 bytes (FP16/BF16)，假设 Qwen3-27B 有 64 层、32 头、128 维，则 KV_Cache = 2 * 64 * 32 * 128 * 32768 * 2 bytes ≈ 34.4 GB，远超 16GB 显存剩余空间

## Corrected Claim

Qwen3-27B 在 32K 上下文下的 KV Cache 显存占用计算：KV_Cache_Size = 2 * n_layers * n_heads * head_dim * seq_len * 2 bytes (FP16/BF16)，假设 Qwen3-27B 有 64 层、32 头、128 维，则 KV_Cache = 2 * 64 * 32 * 128 * 32768 * 2 bytes ≈ 34.4 GB，远超 16GB 显存剩余空间

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Qwen3-27B architecture layers heads head_dim KV cache size calculation
