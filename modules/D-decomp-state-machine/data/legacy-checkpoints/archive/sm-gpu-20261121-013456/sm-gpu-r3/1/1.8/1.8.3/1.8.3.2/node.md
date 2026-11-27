# N184: FP8 KV Cache 显存占用计算：2 * num_layers(64) * num_kv_heads(8) * head_dim(128) * seq_l

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

FP8 KV Cache 显存占用计算：2 * num_layers(64) * num_kv_heads(8) * head_dim(128) * seq_len(32K) * 1 byte/param / 1024^3 = 4.29 GB

## Corrected Claim

FP8 KV Cache 显存占用计算：2 * num_layers(64) * num_kv_heads(8) * head_dim(128) * seq_len(32K) * 1 byte/param / 1024^3 = 4.29 GB

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2 * 64 * 8 * 128 * 32768 * 1 / 1024^3 ≈ 4.29 GB，数值量级与算术逻辑均正确。
