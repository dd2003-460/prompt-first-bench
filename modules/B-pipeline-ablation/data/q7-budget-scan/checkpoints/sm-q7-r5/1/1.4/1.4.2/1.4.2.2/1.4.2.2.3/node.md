# N357: 3.84TB 方案的 RAID6 重建时间 T_rebuild_384 估算：重建需读取剩余 235 块盘的数据并重写至新盘。假设聚合读取带宽受限于背板或控制器

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N158

## Claim

3.84TB 方案的 RAID6 重建时间 T_rebuild_384 估算：重建需读取剩余 235 块盘的数据并重写至新盘。假设聚合读取带宽受限于背板或控制器，典型值为 10-15 GB/s（NVMe 阵列常见瓶颈）。需重建数据量 = 3.84TB = 3840GB。T_rebuild ≈ 3840GB / 12GB/s ≈ 320 秒 ≈ 5.3 分钟。远快于 7.68TB 方案的 7.68TB/12GB/s ≈ 640 秒 ≈ 10.7 分钟。

## Corrected Claim

3.84TB 方案的 RAID6 重建时间 T_rebuild_384 估算：重建需读取剩余 235 块盘的数据并重写至新盘。假设聚合读取带宽受限于背板或控制器，典型值为 10-15 GB/s（NVMe 阵列常见瓶颈）。需重建数据量 = 3.84TB = 3840GB。T_rebuild ≈ 3840GB / 12GB/s ≈ 320 秒 ≈ 5.3 分钟。远快于 7.68TB 方案的 7.68TB/12GB/s ≈ 640 秒 ≈ 10.7 分钟。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（3840/12=320s≈5.3min, 7680/12=640s≈10.7min），带宽假设符合NVMe阵列典型瓶颈范围，RAID6重建逻辑自洽。
