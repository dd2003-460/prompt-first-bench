# N275: 静态资源未命中率 Miss_Rate_Static 受对象大小 s 影响：当 s > 5MB 时，由于缓存存储容量限制及热点集中度下降，Miss_Rate_St

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

静态资源未命中率 Miss_Rate_Static 受对象大小 s 影响：当 s > 5MB 时，由于缓存存储容量限制及热点集中度下降，Miss_Rate_Static 从 0.05 上升至 0.15；当 s < 1MB 时，Miss_Rate_Static 稳定在 0.05 左右。

## Corrected Claim

静态资源未命中率 Miss_Rate_Static 受对象大小 s 影响：当 s > 5MB 时，由于缓存存储容量限制及热点集中度下降，Miss_Rate_Static 从 0.05 上升至 0.15；当 s < 1MB 时，Miss_Rate_Static 稳定在 0.05 左右。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN cache miss rate impact of object size large files
