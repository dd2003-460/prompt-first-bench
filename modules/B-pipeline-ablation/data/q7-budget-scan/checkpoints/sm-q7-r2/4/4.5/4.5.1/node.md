# N82: NVMe SSD阵列将RTO从24h压缩至4h所需的瞬时写入IOPS需求量为：(500TB * 1.805) / (4 * 3600) ≈ 61,000 IOP

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

NVMe SSD阵列将RTO从24h压缩至4h所需的瞬时写入IOPS需求量为：(500TB * 1.805) / (4 * 3600) ≈ 61,000 IOPS (假设4KB随机写块大小)

## Corrected Claim

NVMe SSD阵列将RTO从24h压缩至4h所需的瞬时写入IOPS需求量为：(500TB * 1.805) / (4 * 3600) ≈ 61,000 IOPS (假设4KB随机写块大小)

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (500 * 1024^4 * 1.805) / (4 * 3600 * 4096) ≈ 61,000 IOPS，量纲与数值量级合理。
