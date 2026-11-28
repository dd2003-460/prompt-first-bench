# N34: 单token KV Cache显存占用公式及数值：Bytes_per_token = 2 (K+V) * L * n_kv * d_head * dtype_s

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

单token KV Cache显存占用公式及数值：Bytes_per_token = 2 (K+V) * L * n_kv * d_head * dtype_size。在FP16 (2bytes) 下，Bytes_per_token = 2 * 64 * 8 * 128 * 2 = 262,144 Bytes = 256 KB/token。

## Corrected Claim

单token KV Cache显存占用公式及数值：Bytes_per_token = 2 (K+V) * L * n_kv * d_head * dtype_size。在FP16 (2bytes) 下，Bytes_per_token = 2 * 64 * 8 * 128 * 2 = 262,144 Bytes = 256 KB/token。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构正确（2代表K和V，L=64层，n_kv=8头，d_head=128维，dtype=2字节），计算过程 2*64*8*128*2 = 262,144 Bytes = 256 KB 准确无误。
