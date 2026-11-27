# N131: KV Cache 单 Token 显存占用精确计算：2 (K/V) * 8 (kv_heads) * 128 (head_dim) * 2 (bytes/BF1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

KV Cache 单 Token 显存占用精确计算：2 (K/V) * 8 (kv_heads) * 128 (head_dim) * 2 (bytes/BF16) * 64 (layers) = 262,144 bytes = 256 KB/Token

## Corrected Claim

KV Cache 单 Token 显存占用精确计算：2 (K/V) * 8 (kv_heads) * 128 (head_dim) * 2 (bytes/BF16) * 64 (layers) = 262,144 bytes = 256 KB/Token

## Evidence

先验知识/题面给定，逻辑校验通过：2*8*128*2*64 = 262,144 bytes = 256 KB，计算无误且符合KV Cache显存占用公式。
