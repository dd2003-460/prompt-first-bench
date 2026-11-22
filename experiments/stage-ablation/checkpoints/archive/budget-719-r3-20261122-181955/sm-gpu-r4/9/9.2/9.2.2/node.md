# N358: 修正后的 BF16 KV Cache 单 token 大小计算：2 * n_layers(64) * n_kv_heads(32) * head_dim(128

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N121

## Claim

修正后的 BF16 KV Cache 单 token 大小计算：2 * n_layers(64) * n_kv_heads(32) * head_dim(128) * 2 bytes = 1,048,576 bytes (1 MB)/token；32K 上下文下单请求 KV Cache 总占用 = 1 MB * 32768 = 32 GB。

## Corrected Claim

修正后的 BF16 KV Cache 单 token 大小计算：2 * n_layers(64) * n_kv_heads(32) * head_dim(128) * 2 bytes = 1,048,576 bytes (1 MB)/token；32K 上下文下单请求 KV Cache 总占用 = 1 MB * 32768 = 32 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2 * 64 * 32 * 128 * 2 = 1,048,576 bytes (1 MB) 正确，32768 * 1 MB = 32 GB 正确。
