# N92: HDD+SSD分层中SSD层温数据顺序读带宽约束：100TB温数据全部置于SSD层，所需带宽 = 100TB / 3600s ≈ 28.4GB/s，假设SSD层

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

HDD+SSD分层中SSD层温数据顺序读带宽约束：100TB温数据全部置于SSD层，所需带宽 = 100TB / 3600s ≈ 28.4GB/s，假设SSD层配置20块企业级NVMe SSD（单盘8TB），聚合顺序读带宽 = 20 × 3000MB/s × 0.5（RAID-10） = 30GB/s，满足28.4GB/s需求，余量<1.06倍（临界状态）

## Corrected Claim

HDD+SSD分层中SSD层温数据顺序读带宽约束：100TB温数据全部置于SSD层，所需带宽 = 100TB / 3600s ≈ 28.4GB/s，假设SSD层配置20块企业级NVMe SSD（单盘8TB），聚合顺序读带宽 = 20 × 3000MB/s × 0.5（RAID-10） = 30GB/s，满足28.4GB/s需求，余量<1.06倍（临界状态）

## Evidence

先验知识/题面给定，逻辑校验通过：100TB/3600s≈28.4GB/s，20*3000MB/s*0.5=30GB/s，30>28.4，余量30/28.4≈1.056，计算与逻辑自洽。

## Search Query

NVMe SSD RAID 10 aggregate sequential read bandwidth calculation
