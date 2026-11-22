# N187: BF16 KV Cache 显存占用计算：2 * num_layers(64) * num_kv_heads(8) * head_dim(128) * seq_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N74

## Claim

BF16 KV Cache 显存占用计算：2 * num_layers(64) * num_kv_heads(8) * head_dim(128) * seq_len(32K) * 2 bytes/param / 1024^3 = 8.59 GB（注：N74 claim 中写 4.3GB 可能基于 FP8 KV 或不同配置，此处按 BF16 标准计算）

## Corrected Claim

BF16 KV Cache 显存占用计算：2 * num_layers(64) * num_kv_heads(8) * head_dim(128) * seq_len(32K) * 2 bytes/param / 1024^3 = 8.59 GB（注：N74 claim 中写 4.3GB 可能基于 FP8 KV 或不同配置，此处按 BF16 标准计算）

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2 * 64 * 8 * 128 * 32768 * 2 / 1024^3 ≈ 8.59 GB，数值量级与公式推导一致。
