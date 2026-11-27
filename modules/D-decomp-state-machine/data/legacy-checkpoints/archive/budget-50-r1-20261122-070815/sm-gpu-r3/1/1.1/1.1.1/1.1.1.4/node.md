# N160: BF16 精度下 KV Cache 单 token 占用量计算：2 (K+V) * 4 (n_kv_heads) * 128 (head_dim) * 2 (b

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35, N36, N37

## Claim

BF16 精度下 KV Cache 单 token 占用量计算：2 (K+V) * 4 (n_kv_heads) * 128 (head_dim) * 2 (bytes per BF16) = 2048 bytes/token = 2 KB/token，此为单头单 token 的基础单位

## Corrected Claim

BF16 精度下 KV Cache 单 token 占用量计算：2 (K+V) * 4 (n_kv_heads) * 128 (head_dim) * 2 (bytes per BF16) = 2048 bytes/token = 2 KB/token，此为单头单 token 的基础单位

## Evidence

先验知识/题面给定，逻辑校验通过：2(K+V) * 4(头数) * 128(维度) * 2(字节) = 2048 字节，计算无误且符合 BF16 精度定义。
