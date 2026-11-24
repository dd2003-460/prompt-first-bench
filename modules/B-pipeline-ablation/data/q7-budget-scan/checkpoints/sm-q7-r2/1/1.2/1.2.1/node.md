# N43: HDD+SSD分层中HDD部分采用RAID6配置（N=8），冗余系数R_hdd = 1.25，有效容量为物理容量的80%，提供双盘故障保护

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

HDD+SSD分层中HDD部分采用RAID6配置（N=8），冗余系数R_hdd = 1.25，有效容量为物理容量的80%，提供双盘故障保护

## Corrected Claim

HDD+SSD分层中HDD部分采用RAID6配置（N=8），冗余系数R_hdd = 1.25，有效容量为物理容量的80%，提供双盘故障保护

## Evidence

先验知识/题面给定，逻辑校验通过：RAID6在N=8时冗余系数为1+2/8=1.25，有效容量占比80%，且具备双盘故障保护能力，数值与定义完全自洽。

## Search Query

HDD RAID6 redundancy ratio cold data
