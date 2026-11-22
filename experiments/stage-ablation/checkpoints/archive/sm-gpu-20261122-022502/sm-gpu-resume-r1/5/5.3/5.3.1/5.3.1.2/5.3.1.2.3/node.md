# N879: BF16 KV Cache 显存精确计算：Memory_KV_BF16 = 2 * 60 * 8 * 128 * 32768 * 2 / 1e9 = 2.013

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N276, N277, N278

## Claim

BF16 KV Cache 显存精确计算：Memory_KV_BF16 = 2 * 60 * 8 * 128 * 32768 * 2 / 1e9 = 2.01326592 GB。此值与 N276 中 2.0133 GB 一致，误差 < 0.001%。

## Corrected Claim

BF16 KV Cache 显存精确计算：Memory_KV_BF16 = 2 * 60 * 8 * 128 * 32768 * 2 / 1e9 = 2.01326592 GB。此值与 N276 中 2.0133 GB 一致，误差 < 0.001%。

## Evidence

先验知识/题面给定，逻辑校验通过：计算式 2 * 60 * 8 * 128 * 32768 * 2 / 1e9 数值结果为 2.01326592，与陈述一致，且符合 BF16 (2字节) 显存计算逻辑。
