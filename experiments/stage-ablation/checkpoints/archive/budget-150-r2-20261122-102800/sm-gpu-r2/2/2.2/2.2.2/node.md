# N80: 基于实际参数 (GQA 4 heads) 修正后的 KV Cache 显存占用：BF16 = 2 * 32 * 4 * 128 * 32768 * 2 / 1e

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

基于实际参数 (GQA 4 heads) 修正后的 KV Cache 显存占用：BF16 = 2 * 32 * 4 * 128 * 32768 * 2 / 1e9 ≈ 2.15 GB；INT8/FP8 ≈ 1.07 GB；W4 ≈ 0.54 GB。修正自 N14 中基于假设参数 (8 heads) 计算的 4.29 GB 高估错误。

## Corrected Claim

基于实际参数 (GQA 4 heads) 修正后的 KV Cache 显存占用：BF16 = 2 * 32 * 4 * 128 * 32768 * 2 / 1e9 ≈ 2.15 GB；INT8/FP8 ≈ 1.07 GB；W4 ≈ 0.54 GB。修正自 N14 中基于假设参数 (8 heads) 计算的 4.29 GB 高估错误。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 2 * 32 * 4 * 128 * 32768 * 2 / 1e9 计算结果约为 2.147 GB，与陈述中的 2.15 GB 一致；INT8/FP8 为 BF16 的一半（1.07 GB），W4 为 BF16 的四分之一（0.54 GB），数值量级与逻辑关系均正确。
