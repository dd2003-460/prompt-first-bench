# N7: 本地 NVMe SSD 阵列的冗余系数 R_raid = 1 + 1/N，其中 N 为 RAID5/6 或纠删码的磁盘数，典型值 1.1-1.25

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

本地 NVMe SSD 阵列的冗余系数 R_raid = 1 + 1/N，其中 N 为 RAID5/6 或纠删码的磁盘数，典型值 1.1-1.25

## Corrected Claim

本地 NVMe SSD 阵列的冗余系数 R_raid = 1 + 1/N，其中 N 为 RAID5/6 或纠删码的磁盘数，典型值 1.1-1.25

## Evidence

先验知识/题面给定，逻辑校验通过：RAID5/6及纠删码的冗余系数公式 R=1+1/N 符合定义，典型值 1.1-1.25 对应 N=4~10 的常见配置，量级合理。
