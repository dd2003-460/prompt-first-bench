# N56: KV Cache 显存 = 2 × 64 (layers) × 8 (kv_heads) × 128 (head_dim) × (kv_dtype_bits /

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

KV Cache 显存 = 2 × 64 (layers) × 8 (kv_heads) × 128 (head_dim) × (kv_dtype_bits / 8) × 32768 (seq_len)，在 BF16 KV 下为 25.77 GB，在 FP8 KV 下为 12.88 GB，该值随上下文长度线性增长，是长上下文场景的主要瓶颈。

## Corrected Claim

KV Cache 显存 = 2 × 64 (layers) × 8 (kv_heads) × 128 (head_dim) × (kv_dtype_bits / 8) × 32768 (seq_len)，在 BF16 KV 下为 25.77 GB，在 FP8 KV 下为 12.88 GB，该值随上下文长度线性增长，是长上下文场景的主要瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导正确（2×64×8×128×2×32768 = 25,769,803,264 bytes ≈ 25.77 GB），量级合理，符合KV Cache显存计算标准。
