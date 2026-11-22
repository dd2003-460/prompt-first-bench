# N48: KV_Cache_MB 公式中的 n_kv_heads 决定了 KV 缓存的大小：Qwen3 使用 Grouped Query Attention (GQA)，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

KV_Cache_MB 公式中的 n_kv_heads 决定了 KV 缓存的大小：Qwen3 使用 Grouped Query Attention (GQA)，n_kv_heads=8 远小于 n_heads=32，这使得 KV Cache 比 MHA 小 4 倍 (32/8=4)。若为 MHA，KV Cache 将是 GQA 的 4 倍。

## Corrected Claim

KV_Cache_MB 公式中的 n_kv_heads 决定了 KV 缓存的大小：Qwen3 使用 Grouped Query Attention (GQA)，n_kv_heads=8 远小于 n_heads=32，这使得 KV Cache 比 MHA 小 4 倍 (32/8=4)。若为 MHA，KV Cache 将是 GQA 的 4 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：GQA中KV缓存大小与n_kv_heads成正比，MHA中n_kv_heads=n_heads，故32/8=4倍关系成立。
