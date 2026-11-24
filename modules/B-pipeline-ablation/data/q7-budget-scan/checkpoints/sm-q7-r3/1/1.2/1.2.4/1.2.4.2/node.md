# N131: SSD 层 RAID5 冗余开销量化：采用 4 盘 RAID5 配置，冗余盘数 1，冗余率 = 1/4 = 25%，有效容量系数 = 0.75；若采用 8 盘 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

SSD 层 RAID5 冗余开销量化：采用 4 盘 RAID5 配置，冗余盘数 1，冗余率 = 1/4 = 25%，有效容量系数 = 0.75；若采用 8 盘 RAID5，冗余率降至 12.5%，系数为 0.875

## Corrected Claim

SSD 层 RAID5 冗余开销量化：采用 4 盘 RAID5 配置，冗余盘数 1，冗余率 = 1/4 = 25%，有效容量系数 = 0.75；若采用 8 盘 RAID5，冗余率降至 12.5%，系数为 0.875

## Evidence

先验知识/题面给定，逻辑校验通过：RAID5 冗余率公式为 1/N，4盘时 1/4=25%，有效系数 0.75；8盘时 1/8=12.5%，有效系数 0.875，计算无误。
