# N49: KV Cache 单 token 显存占用计算 (FP16/BF16)：2 (K+V) * num_layers (64) * num_kv_heads (8)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

KV Cache 单 token 显存占用计算 (FP16/BF16)：2 (K+V) * num_layers (64) * num_kv_heads (8) * head_dim (128) * dtype_size (2 bytes) = 262,144 bytes/token ≈ 0.25 MB/token。此值为理论最小单位，不包含 Batch 维度。

## Corrected Claim

KV Cache 单 token 显存占用计算 (FP16/BF16)：2 (K+V) * num_layers (64) * num_kv_heads (8) * head_dim (128) * dtype_size (2 bytes) = 262,144 bytes/token ≈ 0.25 MB/token。此值为理论最小单位，不包含 Batch 维度。

## Evidence

先验知识/题面给定，逻辑校验通过：2 * 64 * 8 * 128 * 2 = 262,144 bytes，计算无误且量级合理。
