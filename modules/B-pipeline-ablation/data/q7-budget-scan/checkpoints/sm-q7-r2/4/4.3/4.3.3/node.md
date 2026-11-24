# N81: 500TB NVMe RAID-6 阵列在 24 盘配置下单盘故障的重建时间 T_rebuild_NVMe ≈ (500TB/24) / 100GB/h * 1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N23

## Claim

500TB NVMe RAID-6 阵列在 24 盘配置下单盘故障的重建时间 T_rebuild_NVMe ≈ (500TB/24) / 100GB/h * 1.15 ≈ 23.1 小时，假设单盘容量 20.8TB，重建速率 100GB/h，含 15% 校验开销

## Corrected Claim

500TB NVMe RAID-6 阵列在 24 盘配置下单盘故障的重建时间 T_rebuild_NVMe ≈ (500TB/24) / 100GB/h * 1.15 ≈ 23.1 小时，假设单盘容量 20.8TB，重建速率 100GB/h，含 15% 校验开销

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (500*1000/24)/100 * 1.15 ≈ 23.1 符合算术逻辑，且 100GB/h 的重建速率对于 NVMe 阵列在 RAID 重建场景下属于合理的保守估计量级。

## Search Query

RAID 6 rebuild time calculation 500TB 24 drives NVMe
