# N531: HDD RAID-5 有效容量精确计算：25块16TB HDD组成RAID-5，逻辑容量 = (25-1) * 16TB = 384TB；原假设400TB裸容量

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N175

## Claim

HDD RAID-5 有效容量精确计算：25块16TB HDD组成RAID-5，逻辑容量 = (25-1) * 16TB = 384TB；原假设400TB裸容量对应可用368TB（92%），符合RAID-5 (24/25=96%) 或 RAID-6 (23/25=92%) 的特征。若确认为RAID-5，可用率应为96%，可用容量 = 400 * 0.96 = 384TB。

## Corrected Claim

HDD RAID-5 有效容量精确计算：25块16TB HDD组成RAID-5，逻辑容量 = (25-1) * 16TB = 384TB；原假设400TB裸容量对应可用368TB（92%），符合RAID-5 (24/25=96%) 或 RAID-6 (23/25=92%) 的特征。若确认为RAID-5，可用率应为96%，可用容量 = 400 * 0.96 = 384TB。

## Evidence

先验知识/题面给定，逻辑校验通过：RAID-5 可用容量公式为 (N-1)*单盘容量，25*16TB 总裸容量下，(25-1)*16=384TB，占比 96%，计算无误。
