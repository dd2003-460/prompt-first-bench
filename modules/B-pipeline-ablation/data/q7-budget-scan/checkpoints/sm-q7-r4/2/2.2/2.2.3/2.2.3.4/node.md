# N179: 工作点C的有效可用容量修正：SSD RAID-5 50TB裸容量，可用率92%，实际可用SSD ≈ 46TB；HDD RAID-5 450TB裸容量，可用率92

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N52

## Claim

工作点C的有效可用容量修正：SSD RAID-5 50TB裸容量，可用率92%，实际可用SSD ≈ 46TB；HDD RAID-5 450TB裸容量，可用率92%，实际可用HDD ≈ 414TB；总有效容量 = 46 + 414 = 460TB；单位CapEx = 63,250 / 460 ≈ ¥137.5/有效TB（原¥127未计RAID开销）。

## Corrected Claim

工作点C的有效可用容量修正：SSD RAID-5 50TB裸容量，可用率92%，实际可用SSD ≈ 46TB；HDD RAID-5 450TB裸容量，可用率92%，实际可用HDD ≈ 414TB；总有效容量 = 46 + 414 = 460TB；单位CapEx = 63,250 / 460 ≈ ¥137.5/有效TB（原¥127未计RAID开销）。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：前两个分别处理SSD和HDD的独立容量修正，第三个进行汇总，第四个进行单位成本推导。各步骤之间无重叠或矛盾，完整覆盖了父节点中关于容量计算和单位CapEx修正的所有关键信息，不存在冗余。）

## Search Query

raid 5 parity overhead percentage calculation
