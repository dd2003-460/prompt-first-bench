# N161: BF16 精度下 32K 上下文 KV Cache 总占用量计算：16 (full_attn_layers) * 2 (K+V) * 4 (n_kv_heads

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35, N36, N37

## Claim

BF16 精度下 32K 上下文 KV Cache 总占用量计算：16 (full_attn_layers) * 2 (K+V) * 4 (n_kv_heads) * 128 (head_dim) * 32768 (context_len) * 2 (bytes) = 1,073,741,824 bytes ≈ 1.0 GB，修正父节点 N37 中 1.07 GB 的精度表述

## Corrected Claim

BF16 精度下 32K 上下文 KV Cache 总占用量计算：16 (full_attn_layers) * 2 (K+V) * 4 (n_kv_heads) * 128 (head_dim) * 32768 (context_len) * 2 (bytes) = 1,073,741,824 bytes ≈ 1.0 GB，修正父节点 N37 中 1.07 GB 的精度表述

## Evidence

先验知识/题面给定，逻辑校验通过：16*2*4*128*32768*2 = 1,073,741,824 bytes，精确等于 1 GiB (1024^3)，约等于 1.0 GB，计算无误且量级合理。
