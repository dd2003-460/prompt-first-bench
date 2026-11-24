# N227: HDD层故障重建时间的量化修正：HDD RAID-6（双盘冗余）重建12盘阵列中2块故障盘，T_rebuild_hdd = (Data_Size / Seque

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N70

## Claim

HDD层故障重建时间的量化修正：HDD RAID-6（双盘冗余）重建12盘阵列中2块故障盘，T_rebuild_hdd = (Data_Size / Sequential_Read_Speed_Aggregate) × Parity_Overhead_Factor；若12块16TB HDD聚合读速3GB/s，Parity_Overhead=1.5，T_rebuild_hdd = 500TB / 3GB/s × 1.5 ≈ 250,000s ≈ 69.4h，超出24h假设

## Corrected Claim

HDD层故障重建时间的量化修正：HDD RAID-6（双盘冗余）重建12盘阵列中2块故障盘，T_rebuild_hdd = (Data_Size / Sequential_Read_Speed_Aggregate) × Parity_Overhead_Factor；若12块16TB HDD聚合读速3GB/s，Parity_Overhead=1.5，T_rebuild_hdd = 500TB / 3GB/s × 1.5 ≈ 250,000s ≈ 69.4h，超出24h假设

## Evidence

先验知识/题面给定，逻辑校验通过：500TB/3GB/s≈166,667s，乘以1.5系数得250,000s，换算为小时约69.4h，计算无误且符合HDD重建慢于SSD的工程常识。

## Search Query

HDD RAID 6 rebuild time 12 disks 16TB
