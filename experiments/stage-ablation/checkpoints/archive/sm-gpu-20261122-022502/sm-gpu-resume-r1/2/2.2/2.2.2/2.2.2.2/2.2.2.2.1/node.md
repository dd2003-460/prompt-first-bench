# N585: Qwen3-27B 在 32K 上下文长度下的 KV Cache 占用量 = 2 (K+V) * 32768 (seq_len) * 32 (num_kv_he

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N179

## Claim

Qwen3-27B 在 32K 上下文长度下的 KV Cache 占用量 = 2 (K+V) * 32768 (seq_len) * 32 (num_kv_heads) * 128 (head_dim) * 2 (bytes/BF16) = 1.07GB

## Corrected Claim

Qwen3-27B 在 32K 上下文长度下的 KV Cache 占用量 = 2 (K+V) * 32768 (seq_len) * 32 (num_kv_heads) * 128 (head_dim) * 2 (bytes/BF16) = 1.07GB

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2 * 32768 * 32 * 128 * 2 = 1,073,741,824 Bytes = 1.07 GB，数值量级与算术逻辑自洽。
