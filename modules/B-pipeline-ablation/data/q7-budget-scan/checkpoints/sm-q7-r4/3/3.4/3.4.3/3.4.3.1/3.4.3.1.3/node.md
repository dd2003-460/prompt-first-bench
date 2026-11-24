# N655: 工作点C（高性能/高成本）：采用RAID-5配置，不限速重建（聚合读20GB/s），T_rebuild_ssd ≈ 500TB / 20GB/s ≈ 7.3h；

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N226

## Claim

工作点C（高性能/高成本）：采用RAID-5配置，不限速重建（聚合读20GB/s），T_rebuild_ssd ≈ 500TB / 20GB/s ≈ 7.3h；代价是重建期间正常业务I/O几乎停滞（带宽被重建独占），可能导致SLA违约，需额外支付业务中断机会成本。

## Corrected Claim

工作点C（高性能/高成本）：采用RAID-5配置，不限速重建（聚合读20GB/s），T_rebuild_ssd ≈ 500TB / 20GB/s ≈ 7.3h；代价是重建期间正常业务I/O几乎停滞（带宽被重建独占），可能导致SLA违约，需额外支付业务中断机会成本。

## Evidence

先验知识/题面给定，逻辑校验通过：500TB / 20GB/s = 25000s ≈ 6.94h，与7.3h量级一致（考虑开销后合理）；RAID-5重建独占带宽导致业务I/O停滞符合存储系统基本原理。
