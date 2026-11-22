# N87: 单 token KV Cache 显存占用计算：2 (K+V) * 64 (layers) * 8 (kv_heads) * 128 (head_dim) * 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

单 token KV Cache 显存占用计算：2 (K+V) * 64 (layers) * 8 (kv_heads) * 128 (head_dim) * 2 bytes (BF16) = 262,144 bytes ≈ 256 KB/token。

## Corrected Claim

单 token KV Cache 显存占用计算：2 (K+V) * 64 (layers) * 8 (kv_heads) * 128 (head_dim) * 2 bytes (BF16) = 262,144 bytes ≈ 256 KB/token。

## Evidence

先验知识/题面给定，逻辑校验通过：2 * 64 * 8 * 128 * 2 = 262,144 bytes，计算无误且量级合理。
