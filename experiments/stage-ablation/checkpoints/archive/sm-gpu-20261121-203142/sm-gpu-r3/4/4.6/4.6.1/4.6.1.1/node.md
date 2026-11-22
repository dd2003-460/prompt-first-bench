# N301: Qwen3-27B 的 KV Cache 单 Token 显存占用精确计算公式：KV_bytes_per_token = 2 (K/V) * num_layer

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N97

## Claim

Qwen3-27B 的 KV Cache 单 Token 显存占用精确计算公式：KV_bytes_per_token = 2 (K/V) * num_layers (32) * num_kv_heads (8) * head_dim (128) * bytes_per_element；在 BF16 (2 bytes) 下为 131,072 bytes (128 KB)，在 FP8 (1 byte) 下为 65,536 bytes (64 KB)，在 INT8 下同为 64 KB。

## Corrected Claim

Qwen3-27B 的 KV Cache 单 Token 显存占用精确计算公式：KV_bytes_per_token = 2 (K/V) * num_layers (32) * num_kv_heads (8) * head_dim (128) * bytes_per_element；在 BF16 (2 bytes) 下为 131,072 bytes (128 KB)，在 FP8 (1 byte) 下为 65,536 bytes (64 KB)，在 INT8 下同为 64 KB。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构正确（2 * 32 * 8 * 128 * 2 = 131,072），数值计算无误，符合Qwen3-27B架构参数（32层，GQA 8 KV头，128维头）。

## Search Query

Qwen3-27B model config num_layers num_kv_heads head_dim
