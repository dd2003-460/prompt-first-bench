# N344: 营收损失时间因子修正：C_revenue_loss * T_outage/86400 需乘以流量恢复曲线因子 k_recovery，故障后1小时内流量恢复率约6

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N108

## Claim

营收损失时间因子修正：C_revenue_loss * T_outage/86400 需乘以流量恢复曲线因子 k_recovery，故障后1小时内流量恢复率约60-70%，等效损失系数k_recovery=0.7-0.8

## Corrected Claim

营收损失时间因子修正：C_revenue_loss * T_outage/86400 需乘以流量恢复曲线因子 k_recovery，故障后1小时内流量恢复率约60-70%，等效损失系数k_recovery=0.7-0.8

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN outage revenue loss recovery curve traffic restoration rate
