# N157: 7.68TB SSD 盘数计算：N = ceil(918TB / 7.68TB) = ceil(119.53) = 120 块。注意：原 N47 计算 ceil

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

7.68TB SSD 盘数计算：N = ceil(918TB / 7.68TB) = ceil(119.53) = 120 块。注意：原 N47 计算 ceil(902.5/7.68)=119 未计入 RAID6 冗余，正确值应为 120 块以覆盖 918TB 物理需求。

## Corrected Claim

7.68TB SSD 盘数计算：N = ceil(918TB / 7.68TB) = ceil(119.53) = 120 块。注意：原 N47 计算 ceil(902.5/7.68)=119 未计入 RAID6 冗余，正确值应为 120 块以覆盖 918TB 物理需求。

## Evidence

先验知识/题面给定，逻辑校验通过：918/7.68=119.53，向上取整为120，计算无误且符合RAID6冗余覆盖逻辑。
