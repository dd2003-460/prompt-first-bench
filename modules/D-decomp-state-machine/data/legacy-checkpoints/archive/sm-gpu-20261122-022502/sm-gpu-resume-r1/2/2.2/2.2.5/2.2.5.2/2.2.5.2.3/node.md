# N608: 单次 ROCm 故障的业务停机损失 L = 停机时长 T * 机会成本率 R，其中 T 需拆解为 (平均故障检测时间 MTTD + 平均修复时间 MTTR)，R

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N186

## Claim

单次 ROCm 故障的业务停机损失 L = 停机时长 T * 机会成本率 R，其中 T 需拆解为 (平均故障检测时间 MTTD + 平均修复时间 MTTR)，R 需量化为 $500/小时 [待核验]

## Corrected Claim

单次 ROCm 故障的业务停机损失 L = 停机时长 T * 机会成本率 R，其中 T 需拆解为 (平均故障检测时间 MTTD + 平均修复时间 MTTR)，R 需根据具体业务场景量化（示例值 $500/小时 待具体业务数据确认）

## Evidence

[质询]R=500美元/小时是具体的经验性财务参数，无法从第一性原理推导，且缺乏特定业务场景的上下文支持，属于未经验证的假设值。 | 公式结构 L=T*R 及 T=MTTD+MTTR 符合可靠性工程与损失计算的基本逻辑，逻辑自洽；但 R 的具体数值 500 为经验事实，无来源支持且无法从公理推出，依据经验事实排除条款降级。
