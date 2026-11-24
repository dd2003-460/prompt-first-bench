# N530: SSD RAID-5 有效容量精确计算：12块2TB NVMe盘组成RAID-5，逻辑容量 = (12-1) * 2TB = 22TB；若使用RAID-6则为(

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N175

## Claim

SSD RAID-5 有效容量精确计算：12块2TB NVMe盘组成RAID-5，逻辑容量 = (12-1) * 2TB = 22TB；若使用RAID-6则为(12-2)*2=20TB。注意：原假设100TB裸容量可能指12块8.3TB盘或更多小盘，需澄清盘数与单盘容量匹配关系。若按100TB裸容量计算，可用容量 = 100 * (N-1)/N。

## Corrected Claim

SSD RAID-5 有效容量精确计算：12块2TB NVMe盘组成RAID-5，逻辑容量 = (12-1) * 2TB = 22TB；若使用RAID-6则为(12-2)*2=20TB。注意：原假设100TB裸容量可能指12块8.3TB盘或更多小盘，需澄清盘数与单盘容量匹配关系。若按100TB裸容量计算，可用容量 = 100 * (N-1)/N。

## Evidence

先验知识/题面给定，逻辑校验通过：RAID-5/6容量计算公式正确，数值推导无误
