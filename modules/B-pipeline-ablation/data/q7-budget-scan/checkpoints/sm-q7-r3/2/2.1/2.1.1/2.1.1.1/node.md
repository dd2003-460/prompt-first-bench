# N160: 40块NVMe SSD RAID-6的有效容量精确计算：标称容量 = 40 × 16TB = 640TB；RAID-6冗余开销 = 2 disks × 16TB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

40块NVMe SSD RAID-6的有效容量精确计算：标称容量 = 40 × 16TB = 640TB；RAID-6冗余开销 = 2 disks × 16TB = 32TB；文件系统开销（XFS）≈ 2-5%，取3% = 19.2TB；有效容量 = 640 - 32 - 19.2 = 588.8TB，满足≥500TB需求且有17.8%余量，支持未来扩容。

## Corrected Claim

40块NVMe SSD RAID-6的有效容量精确计算：标称容量 = 40 × 16TB = 640TB；RAID-6冗余开销 = 2 disks × 16TB = 32TB；文件系统开销（XFS）≈ 2-5%，取3% = 19.2TB；有效容量 = 640 - 32 - 19.2 = 588.8TB，满足≥500TB需求且有17.8%余量，支持未来扩容。

## Evidence

先验知识/题面给定，逻辑校验通过：RAID-6冗余计算正确（2盘），文件系统开销估算合理，算术运算无误（640-32-19.2=588.8），余量计算正确（(588.8-500)/500=17.76%≈17.8%）。

## Search Query

RAID-6 effective capacity calculation NVMe SSD overhead
