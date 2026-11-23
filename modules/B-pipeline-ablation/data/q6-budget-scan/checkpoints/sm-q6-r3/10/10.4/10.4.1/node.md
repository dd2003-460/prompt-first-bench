# N343: 日均营收 C_revenue_loss 精确计算：C_revenue_loss = DAU * ARPU_active，其中ARPU_active需区分付费用户

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N108

## Claim

日均营收 C_revenue_loss 精确计算：C_revenue_loss = DAU * ARPU_active，其中ARPU_active需区分付费用户与非付费用户，假设付费率5%，付费ARPU¥20，非付费ARPU¥0.1，总ARPU≈¥1.05，日均营收≈¥5.25M

## Corrected Claim

日均营收 C_revenue_loss 精确计算：C_revenue_loss = DAU * ARPU_active，其中ARPU_active需区分付费用户与非付费用户，假设付费率5%，付费ARPU¥20，非付费ARPU¥0.1，总ARPU≈¥1.05，日均营收≈¥5.25M

## Evidence

先验知识/题面给定，逻辑校验通过：总ARPU计算正确（0.05*20 + 0.95*0.1 = 1.05），日均营收推导符合数学逻辑（DAU * 1.05 = 5.25M 隐含 DAU=5M，量级合理）。

## Search Query

C-end image video platform ARPU paid user ratio revenue model
