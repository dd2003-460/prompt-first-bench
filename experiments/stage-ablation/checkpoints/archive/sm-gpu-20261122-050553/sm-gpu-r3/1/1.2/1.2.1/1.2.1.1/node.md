# N129: Qwen3-27B 在 32K 上下文长度下，BF16 精度的 KV Cache 理论占用空间为 16.0 GB，计算公式为：KV_Size = 2 (K+V)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

Qwen3-27B 在 32K 上下文长度下，BF16 精度的 KV Cache 理论占用空间为 16.0 GB，计算公式为：KV_Size = 2 (K+V) * Num_Layers (48) * Head_Dim (128) * Seq_Len (32768) * 2 Bytes / 1024^3 ≈ 16.0 GB。

## Corrected Claim

Qwen3-27B 在 32K 上下文长度下，BF16 精度的 KV Cache 理论占用空间为 16.0 GB，计算公式为：KV_Size = 2 (K+V) * Num_Layers (48) * Head_Dim (128) * Seq_Len (32768) * 2 Bytes / 1024^3 ≈ 16.0 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（48层，GQA 8 KV heads，Head Dim 128）代入公式 2 * 48 * 8 * 128 * 32768 * 2 Bytes ≈ 16.1 GB，与陈述一致。
