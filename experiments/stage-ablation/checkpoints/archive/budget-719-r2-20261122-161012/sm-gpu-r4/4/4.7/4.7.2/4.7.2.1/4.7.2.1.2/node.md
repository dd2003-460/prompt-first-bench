# N606: KV Cache 精确计算公式与数值：KV_Size = 2 (K+V) * L (64) * H (32) * d_head (128) * Seq_Len 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N253

## Claim

KV Cache 精确计算公式与数值：KV_Size = 2 (K+V) * L (64) * H (32) * d_head (128) * Seq_Len (32768) * Byte_Size (2 for BF16) = 34.36 GB。注意：原 N253 估算的 1.0-1.2 GB 存在数量级错误，修正为 34.36 GB。

## Corrected Claim

KV Cache 精确计算公式与数值：KV_Size = 2 (K+V) * L (64) * H (32) * d_head (128) * Seq_Len (32768) * Byte_Size (2 for BF16) = 34.36 GB。注意：原 N253 估算的 1.0-1.2 GB 存在数量级错误，修正为 34.36 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2 * 64 * 32 * 128 * 32768 * 2 = 34,359,738,368 Bytes ≈ 34.36 GB，数值量级与公式推导完全一致。
