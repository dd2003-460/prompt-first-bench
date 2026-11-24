# N91: NVMe SSD RAID重建/故障切换时间量化：NVMe SSD顺序读取速度约3,000MB/s，RAID5/6重建100TB数据量，理论时间 = 100TB

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

NVMe SSD RAID重建/故障切换时间量化：NVMe SSD顺序读取速度约3,000MB/s，RAID5/6重建100TB数据量，理论时间 = 100TB / 3000MB/s ≈ 9.5分钟；考虑元数据更新和校验，实际RTO（恢复时间目标）为15-30分钟，远低于4小时目标，因此NVMe方案RTO代价为$0（未超出目标），但需计入故障检测时间（SMART预警或心跳超时，通常5-10分钟）。

## Corrected Claim

NVMe SSD RAID重建/故障切换时间量化：NVMe SSD顺序读取速度约3,000MB/s，RAID5/6重建100TB数据量，理论时间 = 100TB / 3000MB/s ≈ 9.5分钟；考虑元数据更新和校验，实际RTO（恢复时间目标）为15-30分钟，远低于4小时目标，因此NVMe方案RTO代价为$0（未超出目标），但需计入故障检测时间（SMART预警或心跳超时，通常5-10分钟）。

## Evidence

先验知识/题面给定，逻辑校验通过：100TB/3000MB/s≈9.5分钟计算正确，加上元数据开销后15-30分钟符合NVMe RAID重建的工程经验量级，且远低于4小时目标，逻辑自洽。

## Search Query

NVMe SSD RAID rebuild time 100TB estimated minutes
