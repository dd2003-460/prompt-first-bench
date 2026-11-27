# N126: 卖家流失率 Churn_Rate 在干预后的预测值需基于价格敏感度分布计算，假设 Churn_Rate = P(ΔU_S < 0 | Price_Sensiti

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42, N43, N44

## Claim

卖家流失率 Churn_Rate 在干预后的预测值需基于价格敏感度分布计算，假设 Churn_Rate = P(ΔU_S < 0 | Price_Sensitivity)，其中 Price_Sensitivity 为卖家对价格变动的敏感程度，需结合卖家历史行为数据估计

## Corrected Claim

卖家流失率 Churn_Rate 在干预后的预测值需基于价格敏感度分布计算，假设 Churn_Rate = P(ΔU_S < 0 | Price_Sensitivity)，其中 Price_Sensitivity 为卖家对价格变动的敏感程度，需结合卖家历史行为数据估计

## Evidence

先验知识/题面给定，逻辑校验通过：流失率定义为效用变化为负的条件概率，且依赖敏感度分布和历史数据估计符合经济学与数据科学基本逻辑。

## Search Query

predicting seller churn rate based on price intervention impact
