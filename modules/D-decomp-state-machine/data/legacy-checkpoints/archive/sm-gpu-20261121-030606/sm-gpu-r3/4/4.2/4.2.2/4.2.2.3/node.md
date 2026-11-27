# N297: 非Flash Attention（标准Attention）路径下，注意力分数矩阵显存占用计算：占用 = (batch_size * n_heads * seq_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N126

## Claim

非Flash Attention（标准Attention）路径下，注意力分数矩阵显存占用计算：占用 = (batch_size * n_heads * seq_len^2 * dtype_size)。对于Qwen3-27B (n_heads=32, seq_len=32768, BF16=2bytes)，单层占用 = 1 * 32 * 32768^2 * 2 ≈ 68.7 GB。这远超单卡显存，证明在32K上下文下必须使用Flash Attention或近似方法，否则N20的2.5GB估算完全失效。

## Corrected Claim

非Flash Attention（标准Attention）路径下，注意力分数矩阵显存占用计算：占用 = (batch_size * n_heads * seq_len^2 * dtype_size)。对于Qwen3-27B (n_heads=32, seq_len=32768, BF16=2bytes)，单层占用 = 1 * 32 * 32768^2 * 2 ≈ 68.7 GB。这远超单卡显存，证明在32K上下文下必须使用Flash Attention或近似方法，否则N20的2.5GB估算完全失效。

## Evidence

先验知识/题面给定，逻辑校验通过：标准Attention显存公式为 O(N^2)，计算 32 * 32768^2 * 2 bytes ≈ 68.7 GB，数值量级与逻辑推导均正确。
