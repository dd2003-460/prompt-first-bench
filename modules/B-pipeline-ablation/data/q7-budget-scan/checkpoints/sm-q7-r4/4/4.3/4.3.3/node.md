# N81: 500TB NVMe RAID-6 阵列在 24 盘配置下单盘故障的重建时间 T_rebuild_NVMe ≈ (500TB/24) / 100GB/h * 1

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

500TB NVMe RAID-6 阵列在 24 盘配置下单盘故障的重建时间 T_rebuild_NVMe ≈ (500TB/24) / 100GB/h * 1.15 ≈ 23.1 小时，假设单盘容量 20.8TB，重建速率 100GB/h，含 15% 校验开销

## Corrected Claim

500TB NVMe RAID-6 阵列在 24 盘配置下单盘故障的重建时间 T_rebuild_NVMe ≈ (500TB/24) / 100GB/h * 1.15 ≈ 23.1 小时，假设单盘容量 20.8TB，重建速率 100GB/h，含 15% 校验开销

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点并非描述独立的物理机制或维度，而是对同一变量（重建速率/工作点）在不同约束下的三种取值进行枚举。这导致结构上存在高度冗余（本质上是同一个公式的不同参数代入），且逻辑上缺乏正交性（它们共同构成了一个连续的参数空间而非独立分支）。此外，子节点2中关于‘热节流’的描述引入了新的物理限制维度，与单纯的速率设定混合，使得分类标准不统一。）

## Search Query

RAID 6 rebuild time calculation 500TB 24 drives NVMe
