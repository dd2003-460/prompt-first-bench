# N347: 非 FlashAttention (标准 Attention) 在 Batch Size=1、Seq Len=32K 时的激活值显存开销：需存储注意力分数矩阵，

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N142

## Claim

非 FlashAttention (标准 Attention) 在 Batch Size=1、Seq Len=32K 时的激活值显存开销：需存储注意力分数矩阵，大小为 num_heads * seq_len * seq_len * bytes_per_element = 32 * 32768 * 32768 * 2 ≈ 68.7 GB，远超显存上限，证明标准 Attention 在此场景不可行。

## Corrected Claim

非 FlashAttention (标准 Attention) 在 Batch Size=1、Seq Len=32K 时的激活值显存开销：需存储注意力分数矩阵，大小为 num_heads * seq_len * seq_len * bytes_per_element = 32 * 32768 * 32768 * 2 ≈ 68.7 GB，远超显存上限，证明标准 Attention 在此场景不可行。

## Evidence

先验知识/题面给定，逻辑校验通过：32 * 32768 * 32768 * 2 bytes = 68,719,476,736 bytes ≈ 64 GiB (或 68.7 GB)，计算正确且符合标准Attention显存占用原理。
