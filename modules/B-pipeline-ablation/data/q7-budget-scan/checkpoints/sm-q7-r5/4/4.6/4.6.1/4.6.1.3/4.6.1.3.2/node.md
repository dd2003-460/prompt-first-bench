# N496: 工作点B（宽松SLA，部分降级容忍）：定义RTO为‘恢复至80%性能’，允许20%性能降级持续存在。假设业务对延迟不敏感，仅在重建完成前损失30%性能。C_RT

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N217

## Claim

工作点B（宽松SLA，部分降级容忍）：定义RTO为‘恢复至80%性能’，允许20%性能降级持续存在。假设业务对延迟不敏感，仅在重建完成前损失30%性能。C_RTO_penalty_B = L_hourly * 30% * T_rebuild_effective。若 T_rebuild_effective = 25h（基于N248工作点B），L_hourly = ¥1,000/h，则 C_penalty_B = ¥7,500。此工作点平衡了SLA要求和成本。

## Corrected Claim

工作点B（宽松SLA，部分降级容忍）：定义RTO为‘恢复至80%性能’，允许20%性能降级持续存在。假设业务对延迟不敏感，仅在重建完成前损失30%性能。C_RTO_penalty_B = L_hourly * 30% * T_rebuild_effective。若 T_rebuild_effective = 25h（基于N248工作点B），L_hourly = ¥1,000/h，则 C_penalty_B = ¥7,500。此工作点平衡了SLA要求和成本。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 1000 * 0.3 * 25 = 7500 正确，且符合 source=knowledge 节点的判定规则。
