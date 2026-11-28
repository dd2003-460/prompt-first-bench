# N97: 单 Token KV Cache 字节数计算公式：Bytes_per_token_kv = 2 (K+V) * num_kv_heads * head_dim 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

单 Token KV Cache 字节数计算公式：Bytes_per_token_kv = 2 (K+V) * num_kv_heads * head_dim * dtype_bytes; 对于 FP8 KV cache (dtype_bytes=1)，Bytes_per_token_kv = 2 * 8 * 128 * 1 = 2048 Bytes = 2 KB/token。

## Corrected Claim

单 Token KV Cache 字节数计算公式：Bytes_per_token_kv = 2 (K+V) * num_kv_heads * head_dim * dtype_bytes; 对于 FP8 KV cache (dtype_bytes=1)，Bytes_per_token_kv = 2 * 8 * 128 * 1 = 2048 Bytes = 2 KB/token。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构正确（2代表K和V，num_kv_heads=8，head_dim=128，FP8为1字节），计算 2*8*128*1=2048 无误。
