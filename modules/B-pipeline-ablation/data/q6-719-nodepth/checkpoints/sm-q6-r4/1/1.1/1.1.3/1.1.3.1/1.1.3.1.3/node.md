# N451: 图片主导工作点下的缓存存储容量需求 N_storage_img = 2,000,000 MB/day * 0.88 (Hit Rate) * 3 days (H

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N143

## Claim

图片主导工作点下的缓存存储容量需求 N_storage_img = 2,000,000 MB/day * 0.88 (Hit Rate) * 3 days (Hot Window) * 1.3 (Spillover) ≈ 6.86 TB，需据此配置 NVMe SSD 总容量。

## Corrected Claim

图片主导工作点下的缓存存储容量需求 N_storage_img = 2,000,000 MB/day * 0.88 (Hit Rate) * 3 days (Hot Window) * 1.3 (Spillover) ≈ 6.86 TB，需据此配置 NVMe SSD 总容量。

## Evidence

先验知识/题面给定，逻辑校验通过：2,000,000 MB * 0.88 * 3 * 1.3 = 6,864,000 MB ≈ 6.86 TB，计算无误且量级合理。
