# N454: 平衡工作点下的缓存存储容量需求 N_storage_bal = 2,000,000 MB/day * 0.85 * 3 days * 1.3 ≈ 6.63 TB

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N144

## Claim

平衡工作点下的缓存存储容量需求 N_storage_bal = 2,000,000 MB/day * 0.85 * 3 days * 1.3 ≈ 6.63 TB，与图片工作点相比容量需求略低，但单对象体积增大导致 IOPS 需求下降，吞吐需求上升。

## Corrected Claim

平衡工作点下的缓存存储容量需求 N_storage_bal = 2,000,000 MB/day * 0.85 * 3 days * 1.3 ≈ 6.63 TB，与图片工作点相比容量需求略低，但单对象体积增大导致 IOPS 需求下降，吞吐需求上升。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 2,000,000 * 0.85 * 3 * 1.3 = 6,630,000 MB ≈ 6.63 TB，量纲与量级合理，符合缓存容量估算逻辑。
