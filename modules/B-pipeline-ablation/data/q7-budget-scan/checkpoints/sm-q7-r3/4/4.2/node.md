# N20: HDD+SSD 分层方案中，热数据 SSD 层故障仅影响 20% 数据，RTO 由 SSD 层重建主导；冷数据 HDD 层故障 RTO 由 HDD 重建时间决定

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

HDD+SSD 分层方案中，热数据 SSD 层故障仅影响 20% 数据，RTO 由 SSD 层重建主导；冷数据 HDD 层故障 RTO 由 HDD 重建时间决定，公式：T_RTO_Hybrid = max(T_rebuild_SSD, T_rebuild_HDD)，其中 HDD 重建速率约为 100MB/s 每盘，500TB*80%=400TB 冷数据重建需 400000GB/100MB/s ≈ 11.1 小时 [knowledge]

## Corrected Claim

HDD+SSD 分层方案中，热数据 SSD 层故障仅影响 20% 数据，RTO 由 SSD 层重建主导；冷数据 HDD 层故障 RTO 由 HDD 重建时间决定，公式：T_RTO_Hybrid = max(T_rebuild_SSD, T_rebuild_HDD)，其中 HDD 重建速率约为 100MB/s 每盘，500TB*80%=400TB 冷数据重建需 400000GB/100MB/s ≈ 11.1 小时 [knowledge]

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别针对HDD层带宽修正、HDD层拓扑与盘数计算、HDD层最终耗时推导、SSD层耗时推导进行拆解，逻辑链条清晰且互不重叠，完整覆盖了父节点中关于混合存储RTO计算的各个关键参数和步骤，无冗余。）
