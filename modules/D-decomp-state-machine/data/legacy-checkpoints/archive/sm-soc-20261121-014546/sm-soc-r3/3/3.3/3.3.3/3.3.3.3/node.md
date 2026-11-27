# N241: 投影2-长期净收益损失 LTV_loss 量化：假设基准流失率 churn_base = 20%，β 导致流失率增加 5%（绝对值），则 retention_r

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N71

## Claim

投影2-长期净收益损失 LTV_loss 量化：假设基准流失率 churn_base = 20%，β 导致流失率增加 5%（绝对值），则 retention_rate 从 0.8 降至 0.75。若 C_acquisition = $20，则 LTV_loss = (1 - 0.75) * 20 - (1 - 0.8) * 20 = $5 - $4 = $1（每用户单位时间内的净收益调整项，需结合用户生命周期价值 LTV_user 进一步年化）。

## Corrected Claim

投影2-长期净收益损失 LTV_loss 量化：假设基准流失率 churn_base = 20%，β 导致流失率增加 5%（绝对值），则 retention_rate 从 0.8 降至 0.75。若 C_acquisition = $20，则 LTV_loss = (1 - 0.75) * 20 - (1 - 0.8) * 20 = $5 - $4 = $1（每用户单位时间内的净收益调整项，需结合用户生命周期价值 LTV_user 进一步年化）。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (1-0.75)*20 - (1-0.8)*20 = 5 - 4 = 1 数学正确，量纲一致，符合LTV损失的基本定义逻辑。

## Search Query

lifetime value loss due to increased churn rate calculation
