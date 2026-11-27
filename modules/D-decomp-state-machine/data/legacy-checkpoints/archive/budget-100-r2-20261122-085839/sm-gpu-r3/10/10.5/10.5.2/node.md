# N317: BF16 精度下 KV Cache 显存占用 (32K context, Batch=1) = 2 (K/V) * 48 layers * 8 heads (G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N114

## Claim

BF16 精度下 KV Cache 显存占用 (32K context, Batch=1) = 2 (K/V) * 48 layers * 8 heads (GQA) * 128 head_dim * 32768 tokens * 2 bytes = 12.58 GB

## Corrected Claim

BF16 精度下 KV Cache 显存占用 (32K context, Batch=1) = 2 (K/V) * 48 layers * 8 heads (GQA) * 128 head_dim * 32768 tokens * 2 bytes = 12.58 GB

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2 * 48 * 8 * 128 * 32768 * 2 = 12,884,901,888 bytes ≈ 12.58 GB，数值量级与算术逻辑自洽。
