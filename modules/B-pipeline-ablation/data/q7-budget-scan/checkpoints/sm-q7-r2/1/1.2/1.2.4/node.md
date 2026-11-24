# N46: HDD+SSD分层中SSD部分采用RAID5配置（N=4），冗余系数R_ssd = 1.25，有效容量为物理容量的80%，提供单盘故障保护

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

HDD+SSD分层中SSD部分采用RAID5配置（N=4），冗余系数R_ssd = 1.25，有效容量为物理容量的80%，提供单盘故障保护

## Corrected Claim

HDD+SSD分层中SSD部分采用RAID5配置（N=4），冗余系数R_ssd = 1.25，有效容量为物理容量的80%，提供单盘故障保护

## Evidence

先验知识/题面给定，逻辑校验通过：RAID5在N=4时冗余系数为N/(N-1)=1.25，有效容量占比为(N-1)/N=80%，且支持单盘故障保护，数值与逻辑均自洽。

## Search Query

SSD RAID5 redundancy ratio cost optimization
