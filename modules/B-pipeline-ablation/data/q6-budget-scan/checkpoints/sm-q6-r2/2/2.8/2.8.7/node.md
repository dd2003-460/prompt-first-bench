# N104: 可缓存对象总数 N_objects 的估算：对于日均上传 200GB 的平台，假设平均对象大小 s_avg = 1MB，则日均新增对象数 ≈ 200,000 个

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22, N26, N27

## Claim

可缓存对象总数 N_objects 的估算：对于日均上传 200GB 的平台，假设平均对象大小 s_avg = 1MB，则日均新增对象数 ≈ 200,000 个；若对象保留周期为 30 天，则 N_objects ≈ 6,000,000 个，具体数值需根据实际存储策略确定。

## Corrected Claim

可缓存对象总数 N_objects 的估算：对于日均上传 200GB 的平台，假设平均对象大小 s_avg = 1MB，则日均新增对象数 ≈ 200,000 个；若对象保留周期为 30 天，则 N_objects ≈ 6,000,000 个，具体数值需根据实际存储策略确定。

## Evidence

先验知识/题面给定，逻辑校验通过：200GB/天 ÷ 1MB/对象 = 200,000 对象/天，乘以 30 天保留期 = 6,000,000 对象，计算无误且量级合理。

## Search Query

CDN cacheable object count estimation daily upload 200GB
