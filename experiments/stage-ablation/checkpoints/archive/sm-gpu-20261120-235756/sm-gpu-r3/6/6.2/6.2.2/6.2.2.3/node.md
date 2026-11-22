# N312: 二手 A100 的期望停机成本计算公式：E(Cost_Downtime) = P(Failure_12mo) × (MTTR_days × Daily_Oppo

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N115

## Claim

二手 A100 的期望停机成本计算公式：E(Cost_Downtime) = P(Failure_12mo) × (MTTR_days × Daily_Opportunity_Cost)；其中 Daily_Opportunity_Cost 需根据业务负载定义（如闲置算力损失或人工干预成本），若按纯电力成本 $100/天 计，则 E(Cost_Downtime) ≈ 0.02 × 20 × $100 = $40；若按机会成本 $500/天 计，则 E(Cost_Downtime) ≈ $200。

## Corrected Claim

二手 A100 的期望停机成本计算公式：E(Cost_Downtime) = P(Failure_12mo) × (MTTR_days × Daily_Opportunity_Cost)；其中 Daily_Opportunity_Cost 需根据业务负载定义（如闲置算力损失或人工干预成本），若按纯电力成本 $100/天 计，则 E(Cost_Downtime) ≈ 0.02 × 20 × $100 = $40；若按机会成本 $500/天 计，则 E(Cost_Downtime) ≈ $200。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合期望值定义，数值计算（0.02*20*100=40, 0.02*20*500=200）准确，量纲一致。
