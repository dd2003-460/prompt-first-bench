# N118: KV Cache 精确计算公式：KV_Cache_Size = 2 * num_layers * num_kv_heads * head_dim * seq_l

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22, N23, N24

## Claim

KV Cache 精确计算公式：KV_Cache_Size = 2 * num_layers * num_kv_heads * head_dim * seq_len * dtype_size_bytes。基于 N44 获取的实际参数，重新计算 32K 上下文下的精确显存占用（替代 N22 中假设的 17.2GB）。

## Corrected Claim

KV Cache 精确计算公式：KV_Cache_Size = 2 * num_layers * num_kv_heads * head_dim * seq_len * dtype_size_bytes。基于 N44 获取的实际参数，重新计算 32K 上下文下的精确显存占用（替代 N22 中假设的 17.2GB）。

## Evidence

先验知识/题面给定，逻辑校验通过
