# N208: 卖家LTV量化：LTV_seller = (Avg_GMV_per_seller * Commission_Rate * Gross_Margin) / Chu

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

卖家LTV量化：LTV_seller = (Avg_GMV_per_seller * Commission_Rate * Gross_Margin) / Churn_Rate_Monthly。若平均卖家月GMV为5000元，佣金率5%，毛利率80%，月流失率2%，则 LTV_seller ≈ (5000 * 0.05 * 0.8) / 0.02 = 10000元，用于计算迁移阻力成本。

## Corrected Claim

卖家LTV量化：LTV_seller = (Avg_GMV_per_seller * Commission_Rate * Gross_Margin) / Churn_Rate_Monthly。若平均卖家月GMV为5000元，佣金率5%，毛利率80%，月流失率2%，则 LTV_seller ≈ (5000 * 0.05 * 0.8) / 0.02 = 10000元，用于计算迁移阻力成本。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合LTV基本定义（单位时间贡献/流失率），数值计算 (5000*0.05*0.8)/0.02 = 10000 准确无误。
