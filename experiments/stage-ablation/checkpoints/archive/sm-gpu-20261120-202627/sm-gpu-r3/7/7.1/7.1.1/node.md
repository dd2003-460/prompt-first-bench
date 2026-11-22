# N410: 32K 上下文下每生成 1 token 需读取的 KV Cache 总字节数计算：Bytes_per_token = 2 (K+V) × 64 (layers)

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N132

## Claim

32K 上下文下每生成 1 token 需读取的 KV Cache 总字节数计算：Bytes_per_token = 2 (K+V) × 64 (layers) × 8 (kv_heads) × 128 (head_dim) × 2 (bytes/element for BF16) × 32768 (seq_len) ≈ 8.59 GB。

## Corrected Claim

32K 上下文下每生成 1 token 需读取的 KV Cache 总字节数计算：Bytes_per_token = 2 (K+V) × 64 (layers) × 8 (kv_heads) × 128 (head_dim) × 2 (bytes/element for BF16) × 32768 (seq_len) ≈ 8.59 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2*64*8*128*2*32768 = 8,589,934,592 字节，即 8 GiB (约 8.59 GB)，数值量级与逻辑均正确。
