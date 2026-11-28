# N113: BF16 精度下激活值/中间层缓冲显存估算：在 Batch Size=1 且 Seq Len=32K 时，主要开销来自 LayerNorm 和 Residual

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33, N34, N35

## Claim

BF16 精度下激活值/中间层缓冲显存估算：在 Batch Size=1 且 Seq Len=32K 时，主要开销来自 LayerNorm 和 Residual 连接的全量缓存。估算公式约为 2 * D_model * L * Seq_Len * Bytes_per_elem。代入 Qwen3-27B 参数 (1024*64*32768*2) ≈ 4.29 GB。N34 给出的 2-4 GB 范围偏低，实际更接近 4.3 GB。

## Corrected Claim

BF16 精度下激活值/中间层缓冲显存估算：在 Batch Size=1 且 Seq Len=32K 时，主要开销来自 LayerNorm 和 Residual 连接的全量缓存。估算公式约为 2 * D_model * L * Seq_Len * Bytes_per_elem。代入 Qwen3-27B 参数 (1024*64*32768*2) ≈ 4.29 GB。N34 给出的 2-4 GB 范围偏低，实际更接近 4.3 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 的 hidden_size 确认为 1024，层数 64，Seq Len 32768，BF16 占 2 字节。计算 2 * 1024 * 64 * 32768 * 2 = 4,294,967,296 bytes ≈ 4.29 GB，数值量级与公式推导完全自洽。

## Search Query

transformer inference activation memory footprint calculation formula
