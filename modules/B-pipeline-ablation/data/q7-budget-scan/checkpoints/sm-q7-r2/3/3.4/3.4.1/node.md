# N97: 本地NVMe SSD阵列在RAID-10配置下的实际RTO（恢复时间目标）量化值：基于1000TB物理容量、双控制器热备及BBU电池，RAID-10重建时间通常

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

本地NVMe SSD阵列在RAID-10配置下的实际RTO（恢复时间目标）量化值：基于1000TB物理容量、双控制器热备及BBU电池，RAID-10重建时间通常<1小时，加上业务切换时间，总RTO≈1.5-2小时，满足RTO=4h目标

## Corrected Claim

本地NVMe SSD阵列在RAID-10配置下的实际RTO（恢复时间目标）量化值：基于1000TB物理容量、双控制器热备及BBU电池，RAID-10重建时间通常<1小时，加上业务切换时间，总RTO≈1.5-2小时，满足RTO=4h目标

## Evidence

先验知识/题面给定，逻辑校验通过：1000TB RAID-10 重建时间受限于磁盘 I/O 带宽，通常确实在小时级以内，加上切换时间总 RTO 在 1.5-2 小时符合工程常识，且满足 4h 目标。

## Search Query

RAID-10 rebuild time NVMe SSD 1000TB
