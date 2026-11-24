# N45: HDD+SSD分层中SSD部分采用RAID10配置（N=2），冗余系数R_ssd = 2.0，有效容量为物理容量的50%，提供最高数据安全性

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

HDD+SSD分层中SSD部分采用RAID10配置（N=2），冗余系数R_ssd = 2.0，有效容量为物理容量的50%，提供最高数据安全性

## Corrected Claim

HDD+SSD分层中SSD部分采用RAID10配置（N=2），冗余系数R_ssd = 2.0，有效容量为物理容量的50%，提供最高数据安全性

## Evidence

先验知识/题面给定，逻辑校验通过：RAID 10（镜像+条带）在 N=2 磁盘下，有效容量确为物理容量 50%，冗余系数为 2.0，且提供高数据安全性。

## Search Query

SSD RAID10 redundancy ratio hot data
