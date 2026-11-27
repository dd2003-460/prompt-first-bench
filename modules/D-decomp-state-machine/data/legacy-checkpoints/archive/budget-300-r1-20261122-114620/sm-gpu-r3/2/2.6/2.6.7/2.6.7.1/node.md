# N273: Qwen3-27B 在 32K 上下文下，单个请求的 KV Cache 显存占用量化：KV_cache_per_req = 2 * num_layers * n

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

Qwen3-27B 在 32K 上下文下，单个请求的 KV Cache 显存占用量化：KV_cache_per_req = 2 * num_layers * num_kv_heads * head_dim * seq_len * dtype_size。对于 Qwen3-27B (64 layers, 8 kv_heads, 128 head_dim, 32768 tokens, BF16=2 bytes)，计算为 2 * 64 * 8 * 128 * 32768 * 2 = 8,589,934,592 bytes ≈ 8.0 GB。注意：此前节点 N131/N132 中引用的 1.6GB 数据严重偏低，需以本计算值为准进行显存预算修正。

## Corrected Claim

Qwen3-27B 在 32K 上下文下，单个请求的 KV Cache 显存占用量化：KV_cache_per_req = 2 * num_layers * num_kv_heads * head_dim * seq_len * dtype_size。对于 Qwen3-27B (64 layers, 8 kv_heads, 128 head_dim, 32768 tokens, BF16=2 bytes)，计算为 2 * 64 * 8 * 128 * 32768 * 2 = 8,589,934,592 bytes ≈ 8.0 GB。注意：此前节点 N131/N132 中引用的 1.6GB 数据严重偏低，需以本计算值为准进行显存预算修正。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导正确，数值计算准确（2*64*8*128*32768*2 = 8,589,934,592 bytes ≈ 8.0 GB），符合KV Cache显存占用的基本物理/工程直觉。

## Search Query

Qwen3-27B architecture num_kv_heads head_dim layers
