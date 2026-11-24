# N36: 预留空间系数：NVMe SSD需预留约10-20%空间用于GC（垃圾回收）和Wear Leveling，实际可用容量 = 标称容量 * (1 - 0.15)；该

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7, N8, N9

## Claim

预留空间系数：NVMe SSD需预留约10-20%空间用于GC（垃圾回收）和Wear Leveling，实际可用容量 = 标称容量 * (1 - 0.15)；该系数需计入总损耗，与RAID冗余系数相乘

## Corrected Claim

预留空间系数：NVMe SSD需预留约10-20%空间用于GC（垃圾回收）和Wear Leveling，实际可用容量 = 标称容量 * (1 - 0.15)；该系数需计入总损耗，与RAID冗余系数相乘

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

NVMe SSD reserved capacity percentage GC wear leveling enterprise
