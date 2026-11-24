# N456: RTO机会成本的精确公式：C_rto = T_RTO * (C_compute_idle + C_revenue_churn)。题目仅用 C_compute_i

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N153

## Claim

RTO机会成本的精确公式：C_rto = T_RTO * (C_compute_idle + C_revenue_churn)。题目仅用 C_compute_idle = ¥5,000/h。需加入 C_revenue_churn。若数据湖服务于内部研发，停滞导致工程师闲置，成本 = Engineers * Hourly_Rate * Utilization_Loss。假设50名工程师，时薪¥200，利用率损失100%，则 C_revenue_churn = 50 * 200 = ¥10,000/h。总 C_opportunity = ¥15,000/h。此时 C_rto_b = 1.1h * 15,000 = ¥16,500/次。

## Corrected Claim

RTO机会成本的精确公式：C_rto = T_RTO * (C_compute_idle + C_revenue_churn)。题目仅用 C_compute_idle = ¥5,000/h。需加入 C_revenue_churn。若数据湖服务于内部研发，停滞导致工程师闲置，成本 = Engineers * Hourly_Rate * Utilization_Loss。假设50名工程师，时薪¥200，利用率损失100%，则 C_revenue_churn = 50 * 200 = ¥10,000/h。总 C_opportunity = ¥15,000/h。此时 C_rto_b = 1.1h * 15,000 = ¥16,500/次。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合机会成本定义，数值计算（50*200=10000, 10000+5000=15000, 1.1*15000=16500）准确无误，量纲一致。

## Search Query

business impact analysis downtime cost calculation engineering team idle cost
