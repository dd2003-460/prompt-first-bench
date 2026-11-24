# N654: 工作点B（平衡型/后台重建限速）：采用RAID-5配置，限制重建带宽为正常I/O带宽的20%（4GB/s），T_rebuild_ssd ≈ 500TB / 4G

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N226

## Claim

工作点B（平衡型/后台重建限速）：采用RAID-5配置，限制重建带宽为正常I/O带宽的20%（4GB/s），T_rebuild_ssd ≈ 500TB / 4GB/s ≈ 34.7h；代价是重建期间正常I/O延迟增加约30-50%，但避免了业务完全中断。

## Corrected Claim

工作点B（平衡型/后台重建限速）：采用RAID-5配置，限制重建带宽为正常I/O带宽的20%（4GB/s），T_rebuild_ssd ≈ 500TB / 4GB/s ≈ 34.7h；代价是重建期间正常I/O延迟增加约30-50%，但避免了业务完全中断。

## Evidence

先验知识/题面给定，逻辑校验通过：500TB / 4GB/s ≈ 34.7h 计算正确，RAID-5 重建限速策略符合工程常识
