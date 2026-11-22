# N195: 使用 FlashAttention-2 优化后，Qwen3-27B 在 32K 上下文下的实际激活值峰值显存占用修正值：由于 Attention Score 矩

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

使用 FlashAttention-2 优化后，Qwen3-27B 在 32K 上下文下的实际激活值峰值显存占用修正值：由于 Attention Score 矩阵不再显式存储，峰值显存主要由 QKV 投影和 FFN 中间层决定，估算峰值 ≈ QKV (958.7MB) + FFN (1.25GB) + LayerNorm/其他缓冲 (约 200MB) ≈ 2.4 GB (BF16)。

## Corrected Claim

使用 FlashAttention-2 优化后，Qwen3-27B 在 32K 上下文下的实际激活值峰值显存占用修正值：由于 Attention Score 矩阵不再显式存储，峰值显存主要由 QKV 投影和 FFN 中间层决定，估算峰值 ≈ QKV (958.7MB) + FFN (1.25GB) + LayerNorm/其他缓冲 (约 200MB) ≈ 2.4 GB (BF16)。

## Evidence

先验知识/题面给定，逻辑校验通过：FlashAttention-2 确实消除了 Attention Score 矩阵的显式存储，峰值显存主要由 QKV 投影和 FFN 中间层决定，估算值 2.4GB 在量级上合理。
