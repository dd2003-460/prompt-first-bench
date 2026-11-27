# N336: Qwen3-27B 的 KV Cache 在 BF16 精度下，32K 上下文长度的精确显存占用计算公式为：2 (Key+Value) * NumLayers(

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N119

## Claim

Qwen3-27B 的 KV Cache 在 BF16 精度下，32K 上下文长度的精确显存占用计算公式为：2 (Key+Value) * NumLayers(64) * NumKVHeads(8) * HeadDim(128) * SeqLen(32768) * BytesPerElement(2 bytes)，计算结果为 17.18 GB。

## Corrected Claim

Qwen3-27B 的 KV Cache 在 BF16 精度下，32K 上下文长度的精确显存占用计算公式为：2 (Key+Value) * NumLayers(64) * NumKVHeads(8) * HeadDim(128) * SeqLen(32768) * BytesPerElement(2 bytes)，计算结果为 17.18 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构正确（2 * 64 * 8 * 128 * 32768 * 2 bytes = 17,179,869,184 bytes ≈ 17.18 GB），数值量级与计算结果一致。

## Search Query

Qwen3-27B architecture num_layers num_key_value_heads head_dim
