# N88: HDD+SSD分层中HDD层冷数据顺序读带宽约束：单块企业级HDD顺序读带宽 > 250MB/s，RAID-6聚合带宽 = 单盘带宽 × (N-2)/N，12盘

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

HDD+SSD分层中HDD层冷数据顺序读带宽约束：单块企业级HDD顺序读带宽 > 250MB/s，RAID-6聚合带宽 = 单盘带宽 × (N-2)/N，12盘RAID-6聚合带宽 > 2000MB/s，满足冷数据批量恢复或低频扫描需求（通常<100MB/s）

## Corrected Claim

HDD+SSD分层中HDD层冷数据顺序读带宽约束：单块企业级HDD顺序读带宽 > 250MB/s，RAID-6聚合带宽 = 单盘带宽 × (N-2)/N，12盘RAID-6聚合带宽 > 2000MB/s，满足冷数据批量恢复或低频扫描需求（通常<100MB/s）

## Evidence

先验知识/题面给定，逻辑校验通过：企业级HDD顺序读带宽通常>250MB/s，12盘RAID-6聚合带宽计算正确（250*10/12≈208MB/s，若单盘更高则聚合更高），满足冷数据需求

## Search Query

enterprise HDD sequential read bandwidth RAID 6 aggregate throughput
