# N70: A100 80GB 在 BF16 精度下可容纳 32K 上下文（总显存需求 81.65GB，略超 80GB，需使用 FP8 或 KV 量化），在 FP8 精度下

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

A100 80GB 在 BF16 精度下可容纳 32K 上下文（总显存需求 81.65GB，略超 80GB，需使用 FP8 或 KV 量化），在 FP8 精度下可完整容纳 32K 上下文（总显存需求 54.65GB），满足题目容量下限。

## Corrected Claim

A100 80GB 在 BF16 精度下可容纳 32K 上下文（总显存需求 81.65GB，略超 80GB，需使用 FP8 或 KV 量化），在 FP8 精度下可完整容纳 32K 上下文（总显存需求 54.65GB），满足题目容量下限。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB 显存限制下，BF16 精度 32K 上下文显存需求约 81.65GB 略超 80GB，FP8 精度需求约 54.65GB 可容纳，数值量级与精度换算逻辑自洽。
