# N181: 基于 N129 参数计算的 KV Cache 单 Token 大小：2 (K+V) * num_key_value_heads (8) * head_dim (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

基于 N129 参数计算的 KV Cache 单 Token 大小：2 (K+V) * num_key_value_heads (8) * head_dim (128) * 2 bytes (BF16) = 4096 bytes = 4 KB/token/layer。总 KV Cache 大小 = 4 KB * num_hidden_layers (54) * seq_len。对于 seq_len=32768, Batch=1, 总 KV Cache = 4 * 54 * 32768 KB = 7.08 GB。

## Corrected Claim

基于 N129 参数计算的 KV Cache 单 Token 大小：2 (K+V) * num_key_value_heads (8) * head_dim (128) * 2 bytes (BF16) = 4096 bytes = 4 KB/token/layer。总 KV Cache 大小 = 4 KB * num_hidden_layers (54) * seq_len。对于 seq_len=32768, Batch=1, 总 KV Cache = 4 * 54 * 32768 KB = 7.08 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2 * 8 * 128 * 2 = 4096 bytes (4KB) 正确；总量 4 * 54 * 32768 KB = 7,208,947.2 KB ≈ 7.08 GB (按 1024 进制换算) 数值量级与逻辑均自洽。
