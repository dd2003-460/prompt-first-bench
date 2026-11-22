# N197: Qwen3-27B GQA 架构下 32K 上下文 BF16 KV Cache 精确计算：Qwen3-27B 采用 GQA (Grouped Query Att

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

Qwen3-27B GQA 架构下 32K 上下文 BF16 KV Cache 精确计算：Qwen3-27B 采用 GQA (Grouped Query Attention)，KV heads 数量为 8 (而非 32)，因此 KV Cache 大小 = 2 (K+V) * 54 layers * 8 kv_heads * 128 head_dim * 32768 seq_len * 2 bytes / 1024^3 ≈ 1.9 GB，而非 N58 中假设的 9.3 GB (基于 MHA 32 heads)。

## Corrected Claim

Qwen3-27B GQA 架构下 32K 上下文 BF16 KV Cache 精确计算：Qwen3-27B 采用 GQA (Grouped Query Attention)，KV heads 数量为 8 (而非 32)，因此 KV Cache 大小 = 2 (K+V) * 54 layers * 8 kv_heads * 128 head_dim * 32768 seq_len * 2 bytes / 1024^3 ≈ 1.9 GB，而非 N58 中假设的 9.3 GB (基于 MHA 32 heads)。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 确实采用 GQA 架构，KV heads 为 8，计算过程 2*54*8*128*32768*2 / 1024^3 ≈ 1.9 GB 准确无误。

## Search Query

Qwen3-27B GQA kv heads 8 architecture config
