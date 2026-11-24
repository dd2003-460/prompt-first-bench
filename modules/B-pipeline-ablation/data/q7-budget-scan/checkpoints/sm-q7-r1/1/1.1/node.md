# N7: NVMe SSD RAID阵列的有效容量系数：采用RAID-6（假设4盘组，2盘冗余）时，有效容量 = 裸容量 * (4-2)/4 = 50%；若采用RAID-

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

NVMe SSD RAID阵列的有效容量系数：采用RAID-6（假设4盘组，2盘冗余）时，有效容量 = 裸容量 * (4-2)/4 = 50%；若采用RAID-10（2盘组，1盘冗余），有效容量 = 裸容量 * 50%。需根据实际磁盘数量和RAID级别确定具体系数，此处以RAID-6为例，系数为0.5。

## Corrected Claim

NVMe SSD RAID阵列的有效容量系数：采用RAID-6（假设4盘组，2盘冗余）时，有效容量 = 裸容量 * (4-2)/4 = 50%；若采用RAID-10（2盘组，1盘冗余），有效容量 = 裸容量 * 50%。需根据实际磁盘数量和RAID级别确定具体系数，此处以RAID-6为例，系数为0.5。

## Evidence

先验知识/题面给定，逻辑校验通过：RAID-6 (4盘, 2冗余) 有效容量系数为 (4-2)/4=0.5，RAID-10 (2盘组, 1冗余) 有效容量系数为 50%，计算逻辑自洽且符合存储技术基本原理。

## Search Query

RAID-6 effective capacity ratio calculation
