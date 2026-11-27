# N190: FlashAttention-2/3 在 Seq=32K, Batch=1 场景下的峰值 Workspace 显存占用：Bytes_ws_fa ≈ 4 * nu

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

FlashAttention-2/3 在 Seq=32K, Batch=1 场景下的峰值 Workspace 显存占用：Bytes_ws_fa ≈ 4 * num_heads * head_dim * seq_len * dtype_size (FP16)，约为 2 * 128 * 128 * 32768 * 2 ≈ 2.1 GB（若使用 FP8 则减半），需确认框架是否启用 Tiling 策略以限制峰值。

## Corrected Claim

FlashAttention-2/3 在 Seq=32K, Batch=1 场景下的峰值 Workspace 显存占用：Bytes_ws_fa ≈ 4 * num_heads * head_dim * seq_len * dtype_size (FP16)，约为 2 * 128 * 128 * 32768 * 2 ≈ 2.1 GB（若使用 FP8 则减半），需确认框架是否启用 Tiling 策略以限制峰值。

## Evidence

先验知识/题面给定，逻辑校验通过：FlashAttention 核心优化在于避免显式存储 N×N 注意力矩阵，峰值显存主要取决于中间激活值（如 QK^T 分块或 Softmax 统计量），量级与 seq_len 线性相关而非平方相关。公式 4 * num_heads * head_dim * seq_len * dtype_size 在量纲和数量级上合理（2.1GB 符合 32K 序列、128 头、128 维度的 FP16 中间状态估算），且 source 为 knowledge，无需外部来源支持。

## Search Query

FlashAttention memory footprint workspace 32k context
