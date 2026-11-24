# N91: 本地NVMe SSD阵列温数据顺序读带宽约束：单次扫描需在<1小时内完成（假设业务窗口），所需带宽 = 100TB / 3600s ≈ 28.4GB/s，RAI

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

本地NVMe SSD阵列温数据顺序读带宽约束：单次扫描需在<1小时内完成（假设业务窗口），所需带宽 = 100TB / 3600s ≈ 28.4GB/s，RAID-10聚合顺序读带宽 = 单盘带宽 × 磁盘数 × 0.5，单盘NVMe顺序读带宽 > 3000MB/s，500块盘聚合带宽 > 750GB/s，满足28.4GB/s需求，余量>20倍

## Corrected Claim

本地NVMe SSD阵列温数据顺序读带宽约束：单次扫描需在<1小时内完成（假设业务窗口），所需带宽 = 100TB / 3600s ≈ 28.4GB/s，RAID-10聚合顺序读带宽 = 单盘带宽 × 磁盘数 × 0.5，单盘NVMe顺序读带宽 > 3000MB/s，500块盘聚合带宽 > 750GB/s，满足28.4GB/s需求，余量>20倍

## Evidence

先验知识/题面给定，逻辑校验通过：100TB/3600s≈28.4GB/s计算正确；RAID-10聚合带宽公式及500块盘>750GB/s的量级估算符合NVMe SSD工程常识，余量充足。

## Search Query

NVMe SSD sequential read bandwidth GB/s enterprise
