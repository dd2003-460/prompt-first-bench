# N6: HDD+SSD分层中HDD部分采用RAID-6冗余机制，有效可用容量 = 原始物理容量 × (N-2)/N（N为磁盘数，典型N=12时为10/12≈0.833）

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

HDD+SSD分层中HDD部分采用RAID-6冗余机制，有效可用容量 = 原始物理容量 × (N-2)/N（N为磁盘数，典型N=12时为10/12≈0.833）

## Corrected Claim

HDD+SSD分层中HDD部分采用RAID-6冗余机制，有效可用容量 = 原始物理容量 × (N-2)/N（N为磁盘数，典型N=12时为10/12≈0.833）

## Evidence

先验知识/题面给定，逻辑校验通过：RAID-6标准定义允许两块磁盘故障，有效容量公式为(N-2)/N，N=12时计算结果10/12≈0.833正确。
