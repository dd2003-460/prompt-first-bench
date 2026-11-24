# N175: 工作点B的有效可用容量修正：SSD RAID-5 100TB裸容量，可用率92%（12盘11数据），实际可用SSD ≈ 92TB；HDD RAID-5 400T

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

工作点B的有效可用容量修正：SSD RAID-5 100TB裸容量，可用率92%（12盘11数据），实际可用SSD ≈ 92TB；HDD RAID-5 400TB裸容量，可用率92%，实际可用HDD ≈ 368TB；总有效容量 = 92 + 368 = 460TB；单位CapEx = 79,000 / 460 ≈ ¥171.7/有效TB（原¥158未计RAID开销）。

## Corrected Claim

工作点B的有效可用容量修正：SSD RAID-5 100TB裸容量，可用率92%（12盘11数据），实际可用SSD ≈ 92TB；HDD RAID-5 400TB裸容量，可用率92%，实际可用HDD ≈ 368TB；总有效容量 = 92 + 368 = 460TB；单位CapEx = 79,000 / 460 ≈ ¥171.7/有效TB（原¥158未计RAID开销）。

## Evidence

先验知识/题面给定，逻辑校验通过：RAID-5 12盘可用率11/12≈91.67%（取整92%合理），容量计算92+368=460TB及单价79000/460≈171.7元/TB均符合算术逻辑。

## Search Query

raid 5 usable capacity calculation overhead factor
