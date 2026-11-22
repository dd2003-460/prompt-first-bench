# N40: 32K 上下文下 KV Cache 显存占用的数值计算（FP8/INT8 精度）：若 KV Cache 也量化为 8-bit (1 byte/element)，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

32K 上下文下 KV Cache 显存占用的数值计算（FP8/INT8 精度）：若 KV Cache 也量化为 8-bit (1 byte/element)，计算得 KV_Cache = 2 * 64 * 4096 * 8 * 32768 * 1 / 1e9 ≈ 1.4 GB。

## Corrected Claim

32K 上下文下 KV Cache 显存占用的数值计算（FP8/INT8 精度）：若 KV Cache 也量化为 8-bit (1 byte/element)，计算得 KV_Cache = 2 * 64 * 4096 * 8 * 32768 * 1 / 1e9 ≈ 1.4 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 2 * 64 * 4096 * 8 * 32768 * 1 / 1e9 计算结果约为 1.374 GB，与陈述中的 1.4 GB 一致，量纲和数值量级合理。
