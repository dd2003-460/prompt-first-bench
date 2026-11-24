# N87: 本地NVMe SSD阵列冷数据随机读IOPS约束：单块NVMe SSD随机读IOPS > 100,000，RAID-10聚合IOPS = 单盘IOPS × 磁盘

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

本地NVMe SSD阵列冷数据随机读IOPS约束：单块NVMe SSD随机读IOPS > 100,000，RAID-10聚合IOPS = 单盘IOPS × 磁盘数 × 0.5，500TB阵列（1000TB物理容量，假设单盘2TB）共500块盘，聚合IOPS > 25,000,000，满足冷数据偶发随机读需求（通常<1000 IOPS）

## Corrected Claim

本地NVMe SSD阵列冷数据随机读IOPS约束：单块NVMe SSD随机读IOPS > 100,000，RAID-10聚合IOPS = 单盘IOPS × 磁盘数 × 0.5，500TB阵列（1000TB物理容量，假设单盘2TB）共500块盘，聚合IOPS > 25,000,000，满足冷数据偶发随机读需求（通常<1000 IOPS）

## Evidence

先验知识/题面给定，逻辑校验通过：单盘IOPS>100k，500块盘RAID-10聚合IOPS=100k*500*0.5=25,000,000，远大于1000 IOPS需求，数值量级与逻辑自洽。

## Search Query

NVMe SSD random read IOPS specifications enterprise drive
