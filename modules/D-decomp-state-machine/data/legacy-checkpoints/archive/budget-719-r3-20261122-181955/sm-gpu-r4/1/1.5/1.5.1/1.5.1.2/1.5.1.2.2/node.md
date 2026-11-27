# N571: Qwen3-27B 在 32K 上下文、Batch=1 下的 KV Cache 占用为 8 GB (256 KB/token * 32768 tokens)，基

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N198

## Claim

Qwen3-27B 在 32K 上下文、Batch=1 下的 KV Cache 占用为 8 GB (256 KB/token * 32768 tokens)，基于 n_kv_heads=8, num_layers=64, head_dim=128, BF16 计算。

## Corrected Claim

Qwen3-27B 在 32K 上下文、Batch=1 下的 KV Cache 占用为 8 GB (256 KB/token * 32768 tokens)，基于 n_kv_heads=8, num_layers=64, head_dim=128, BF16 计算。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 大小 = 2 * n_layers * n_kv_heads * head_dim * seq_len * bytes_per_element = 2 * 64 * 8 * 128 * 32768 * 2 = 8,589,934,592 bytes = 8 GB。计算无误。
