# N236: Qwen3-27B 在 32K 上下文下的精确 KV Cache 显存占用计算：基于 Qwen3-27B 架构参数 (Num_Layers=64, Num_KV

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82, N83, N84

## Claim

Qwen3-27B 在 32K 上下文下的精确 KV Cache 显存占用计算：基于 Qwen3-27B 架构参数 (Num_Layers=64, Num_KV_Heads=8, Head_Dim=128, Batch_Size=1)，公式为 2 * Num_Layers * Num_KV_Heads * Head_Dim * Seq_Len * Bytes_Per_Element。BF16 (2 bytes) 下占用 = 2 * 64 * 8 * 128 * 32768 * 2 = 8,589,934,592 bytes ≈ 8.0 GB (而非 N82 中的 40GB 或 N83 中的 20GB，需修正前序错误估算)。

## Corrected Claim

Qwen3-27B 在 32K 上下文下的精确 KV Cache 显存占用计算：基于 Qwen3-27B 架构参数 (Num_Layers=64, Num_KV_Heads=8, Head_Dim=128, Batch_Size=1)，公式为 2 * Num_Layers * Num_KV_Heads * Head_Dim * Seq_Len * Bytes_Per_Element。BF16 (2 bytes) 下占用 = 2 * 64 * 8 * 128 * 32768 * 2 = 8,589,934,592 bytes ≈ 8.0 GB (而非 N82 中的 40GB 或 N83 中的 20GB，需修正前序错误估算)。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 2 * 64 * 8 * 128 * 32768 * 2 计算结果确为 8,589,934,592 bytes，即 8.0 GB，量纲与数值均正确。

## Search Query

Qwen3-27B architecture parameters num_heads num_kv_heads head_dim layers
