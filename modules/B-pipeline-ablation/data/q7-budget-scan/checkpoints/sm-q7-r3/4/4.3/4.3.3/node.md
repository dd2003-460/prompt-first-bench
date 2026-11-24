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

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一重建公式中'重建速率'这一单一变量在不同工作点（保守、激进、平衡）下的取值，属于参数枚举而非正交维度分解。此外，父节点隐含了'RAID-6双盘容错'的关键特性（即单盘故障不影响数据可用性，主要风险在于重建期间的二次故障），但子节点仅聚焦于时间计算和热节流，完全缺失了对'二次故障概率与数据安全窗口'这一核心风险维度的独立分析。）

## Search Query

RAID 6 rebuild time calculation 500TB 24 drives NVMe
