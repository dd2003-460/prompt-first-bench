# N179: 工作点C的有效可用容量修正：SSD RAID-5 50TB裸容量，可用率92%，实际可用SSD ≈ 46TB；HDD RAID-5 450TB裸容量，可用率92

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

工作点C的有效可用容量修正：SSD RAID-5 50TB裸容量，可用率92%，实际可用SSD ≈ 46TB；HDD RAID-5 450TB裸容量，可用率92%，实际可用HDD ≈ 414TB；总有效容量 = 46 + 414 = 460TB；单位CapEx = 63,250 / 460 ≈ ¥137.5/有效TB（原¥127未计RAID开销）。

## Corrected Claim

工作点C的有效可用容量修正：SSD RAID-5 50TB裸容量，可用率92%，实际可用SSD ≈ 46TB；HDD RAID-5 450TB裸容量，可用率92%，实际可用HDD ≈ 414TB；总有效容量 = 46 + 414 = 460TB；单位CapEx = 63,250 / 460 ≈ ¥137.5/有效TB（原¥127未计RAID开销）。

## Evidence

先验知识/题面给定，逻辑校验通过：50*0.92=46, 450*0.92=414, 46+414=460, 63250/460≈137.5，计算无误且符合RAID-5容量修正逻辑。

## Search Query

raid 5 parity overhead percentage calculation
