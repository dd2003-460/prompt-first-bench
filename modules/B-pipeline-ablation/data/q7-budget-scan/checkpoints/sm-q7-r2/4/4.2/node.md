# N20: HDD+SSD 分层方案中，热数据 SSD 层故障仅影响 20% 数据，RTO 由 SSD 层重建主导；冷数据 HDD 层故障 RTO 由 HDD 重建时间决定

- **status**: pending
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

父节点级核验未通过：非正交, 有冗余（子节点3与子节点1存在逻辑重叠（均涉及HDD重建带宽及时间计算，且结论互相修正/依赖）；子节点4引入了父节点未明确提及的'100TB温数据'具体数值，虽在合理范围内但增加了非核心细节；子节点2和3紧密耦合，属于同一计算流程的不同步骤，难以完全正交。）
