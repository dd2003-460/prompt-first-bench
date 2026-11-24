# N343: 公有云CDN服务中断导致的业务损失 L_outage 量化公式：L_outage = (Monthly_Revenue × Downtime_Ratio) × 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N119

## Claim

公有云CDN服务中断导致的业务损失 L_outage 量化公式：L_outage = (Monthly_Revenue × Downtime_Ratio) × (1 - Churn_Rate_Factor)，其中 Monthly_Revenue = DAU × ARPU × 30 = 5,000,000 × ¥2 × 30 = ¥300,000,000（假设ARPU=¥2/月），Downtime_Ratio 为故障时长占月度总时长的比例，Churn_Rate_Factor 为故障期间用户永久流失系数（通常取0.05-0.1）。

## Corrected Claim

公有云CDN服务中断导致的业务损失 L_outage 量化公式：L_outage = (Monthly_Revenue × Downtime_Ratio) × (1 - Churn_Rate_Factor)，其中 Monthly_Revenue = DAU × ARPU × 30 = 5,000,000 × ¥2 × 30 = ¥300,000,000（假设ARPU=¥2/月），Downtime_Ratio 为故障时长占月度总时长的比例，Churn_Rate_Factor 为故障期间用户永久流失系数（通常取0.05-0.1）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合业务损失估算的基本逻辑（收入×中断比例×留存系数），数值计算 5,000,000 × 2 × 30 = 300,000,000 准确无误，量纲合理。

## Search Query

business loss estimation formula for CDN outage monthly revenue downtime ratio
