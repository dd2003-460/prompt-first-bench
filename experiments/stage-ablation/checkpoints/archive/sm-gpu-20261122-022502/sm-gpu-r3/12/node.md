# N100: 32K 上下文 KV Cache 精确显存占用计算：Size = 2 (K+V) * 64 (layers) * 8 (kv_heads) * 128 (hea

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

32K 上下文 KV Cache 精确显存占用计算：Size = 2 (K+V) * 64 (layers) * 8 (kv_heads) * 128 (head_dim) * 32768 (tokens) * 2 (bytes for BF16) = 8,589,934,592 bytes ≈ 8.0 GB。若采用 FP8 KV Cache，则减半至 4.0 GB。

## Corrected Claim

32K 上下文 KV Cache 精确显存占用计算：Size = 2 (K+V) * 64 (layers) * 8 (kv_heads) * 128 (head_dim) * 32768 (tokens) * 2 (bytes for BF16) = 8,589,934,592 bytes ≈ 8.0 GB。若采用 FP8 KV Cache，则减半至 4.0 GB。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

Llama 3 70B KV cache memory calculation formula
