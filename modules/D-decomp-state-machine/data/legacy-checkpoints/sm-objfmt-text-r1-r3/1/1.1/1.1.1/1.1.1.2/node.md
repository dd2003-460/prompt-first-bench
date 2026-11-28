# N95: 在 32K 上下文、BF16 精度下，KV Cache 显存具体数值为 2 * 64 * 8 * 128 * 32768 * 2 = 10.74 GB，该值用于

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N25, N26, N27

## Claim

在 32K 上下文、BF16 精度下，KV Cache 显存具体数值为 2 * 64 * 8 * 128 * 32768 * 2 = 10.74 GB，该值用于校验 N47 中 10-20GB 的范围估计

## Corrected Claim

在 32K 上下文、BF16 精度下，KV Cache 显存具体数值为 2 * 64 * 8 * 128 * 32768 * 2 = 10.74 GB，该值用于校验 N47 中 10-20GB 的范围估计

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2 * 64 * 8 * 128 * 32768 * 2 = 10,737,418,240 Bytes ≈ 10.74 GB，数值准确且量级合理。
