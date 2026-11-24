# N140: 工作点C (RAID-10) 的单盘故障重建时间 T_rebuild 约为 1小时，基于RAID-10镜像特性，故障盘只需从镜像伙伴同步，无需跨组重构，假设同步

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

工作点C (RAID-10) 的单盘故障重建时间 T_rebuild 约为 1小时，基于RAID-10镜像特性，故障盘只需从镜像伙伴同步，无需跨组重构，假设同步带宽为 5GB/s，数据量 8TB，T_rebuild = 8,000,000MB / 5,000MB/s = 1,600秒 ≈ 0.44小时，加上系统开销预估1小时。

## Corrected Claim

工作点C (RAID-10) 的单盘故障重建时间 T_rebuild 约为 1小时，基于RAID-10镜像特性，故障盘只需从镜像伙伴同步，无需跨组重构，假设同步带宽为 5GB/s，数据量 8TB，T_rebuild = 8,000,000MB / 5,000MB/s = 1,600秒 ≈ 0.44小时，加上系统开销预估1小时。

## Evidence

先验知识/题面给定，逻辑校验通过：RAID-10重建仅需镜像同步，计算过程（8TB/5GB/s≈0.44h）及加上开销后约1小时的结论符合工程直觉与数学逻辑。
