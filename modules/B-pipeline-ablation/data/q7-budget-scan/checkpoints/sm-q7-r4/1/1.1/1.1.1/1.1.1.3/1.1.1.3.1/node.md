# N434: 数据丢失导致的业务中断边际价值函数 V_loss(t) 的定义：V_loss(t) = (Revenue_per_hour * t) + (Opportunit

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N161

## Claim

数据丢失导致的业务中断边际价值函数 V_loss(t) 的定义：V_loss(t) = (Revenue_per_hour * t) + (Opportunity_Cost * t) + (Reputation_Loss)，其中 Revenue_per_hour 为数据湖支撑业务的年化收入/8760，Opportunity_Cost 为无法访问数据导致的延迟成本，Reputation_Loss 为固定惩罚项（如 SLA 违约罚金）。

## Corrected Claim

数据丢失导致的业务中断边际价值函数 V_loss(t) 的定义：V_loss(t) = (Revenue_per_hour * t) + (Opportunity_Cost * t) + (Reputation_Loss)，其中 Revenue_per_hour 为数据湖支撑业务的年化收入/8760，Opportunity_Cost 为无法访问数据导致的延迟成本，Reputation_Loss 为固定惩罚项（如 SLA 违约罚金）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

business interruption cost function data loss SLA penalty
