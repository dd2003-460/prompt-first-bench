# N141: KV Cache 最大占用量计算：KV_Cache_Max = 2 (K+V) * num_layers * num_kv_heads * head_dim *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

KV Cache 最大占用量计算：KV_Cache_Max = 2 (K+V) * num_layers * num_kv_heads * head_dim * seq_len * dtype_size。对于 Qwen3-27B，需获取 num_kv_heads 和 head_dim 以计算 32K 上下文下的确切 GB 数值

## Corrected Claim

KV Cache 最大占用量计算：KV_Cache_Max = 2 (K+V) * num_layers * num_kv_heads * head_dim * seq_len * dtype_size。对于 Qwen3-27B，需获取 num_kv_heads 和 head_dim 以计算 32K 上下文下的确切 GB 数值

## Evidence

先验知识/题面给定，逻辑校验通过
