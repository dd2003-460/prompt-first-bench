# N408: 工作点B (RAID-5) 的有效容量修正：RAID-5有效容量 = (N-1) * Single_Disk_Size = 11 * 16TB = 176TB，

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N136

## Claim

工作点B (RAID-5) 的有效容量修正：RAID-5有效容量 = (N-1) * Single_Disk_Size = 11 * 16TB = 176TB，而非154.56TB（154.56TB是9*16或类似错误计算），修正后分母增大，单位成本降低约12%。

## Corrected Claim

工作点B (RAID-5) 的有效容量修正：RAID-5有效容量 = (N-1) * Single_Disk_Size = 11 * 16TB = 176TB，而非154.56TB（154.56TB是9*16或类似错误计算），修正后分母增大，单位成本降低约12%。

## Evidence

先验知识/题面给定，逻辑校验通过：RAID-5有效容量公式为(N-1)*单盘容量，12盘RAID-5有效容量确为11*16TB=176TB，原154.56TB计算错误，修正后单位成本降低符合逻辑。
