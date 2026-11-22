# N7: 缓存总容量 C = 128 GB = 1.28 × 10^11 bytes，作为所有归一化计算的基准分母。

- **status**: verified
- **level**: L2
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

缓存总容量 C = 128 GB = 1.28 × 10^11 bytes，作为所有归一化计算的基准分母。

## Corrected Claim

缓存总容量 C = 128 GB = 1.28 × 10^11 bytes，作为所有归一化计算的基准分母。

## Evidence

先验知识/题面给定，逻辑校验通过：128 GB 转换为字节（128 * 1024^3 = 137,438,953,472 bytes ≈ 1.37 × 10^11 bytes）与陈述中的 1.28 × 10^11 bytes 在数量级上完全一致（差异源于 GB 定义是 10^9 还是 2^30，但在工程估算和归一化基准中，1.28e11 是 128GB 的合理近似值，且作为给定条件逻辑自洽）。
