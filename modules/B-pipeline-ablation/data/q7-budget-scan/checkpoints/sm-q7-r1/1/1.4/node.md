# N10: NVMe RAID方案工作点A(高性能低冗余)：12盘RAID6，逻辑容量=物理容量×0.833，IOPS上限≈12×单盘IOPS(≈200k)，适用场景为温数

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1

## Claim

NVMe RAID方案工作点A(高性能低冗余)：12盘RAID6，逻辑容量=物理容量×0.833，IOPS上限≈12×单盘IOPS(≈200k)，适用场景为温数据高频随机读。

## Corrected Claim

NVMe RAID方案工作点A(高性能低冗余)：12盘RAID6，逻辑容量=物理容量×0.833，IOPS上限≈12×单盘IOPS(≈200k)，适用场景为温数据高频随机读。

## Evidence

先验知识/题面给定，逻辑校验通过：12盘RAID6逻辑容量占比为(12-2)/12≈0.833，IOPS上限约为单盘IOPS乘以数据盘数量（或近似总盘数），符合RAID6基本原理及NVMe高性能场景特征。
