# N292: 48.8 TB SSD 缓存对应的物理盘数量 = 48.8 TB / 单盘容量；假设使用 1.92 TB 企业级 NVMe SSD，则需 48.8 / 1.92

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N103

## Claim

48.8 TB SSD 缓存对应的物理盘数量 = 48.8 TB / 单盘容量；假设使用 1.92 TB 企业级 NVMe SSD，则需 48.8 / 1.92 ≈ 25.4，取 26 块盘；若使用 3.84 TB 盘，则需 48.8 / 3.84 ≈ 12.7，取 13 块盘。盘数直接决定总功耗基线

## Corrected Claim

48.8 TB SSD 缓存对应的物理盘数量 = 48.8 TB / 单盘容量；假设使用 1.92 TB 企业级 NVMe SSD，则需 48.8 / 1.92 ≈ 25.4，取 26 块盘；若使用 3.84 TB 盘，则需 48.8 / 3.84 ≈ 12.7，取 13 块盘。盘数直接决定总功耗基线

## Evidence

先验知识/题面给定，逻辑校验通过：48.8/1.92≈25.42，向上取整为26；48.8/3.84≈12.71，向上取整为13，计算无误且符合工程实际。

## Search Query

enterprise NVMe SSD capacity 1.92TB 3.84TB standard sizes
