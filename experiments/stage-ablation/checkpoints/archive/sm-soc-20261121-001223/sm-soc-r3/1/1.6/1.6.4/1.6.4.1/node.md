# N135: 解释力 R² 的残差方差 Var(Residual) 计算：Residual = T_deal_observed - T_deal_predicted，其中 T

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N50

## Claim

解释力 R² 的残差方差 Var(Residual) 计算：Residual = T_deal_observed - T_deal_predicted，其中 T_deal_predicted 由信号+启发式模型生成；Var(Residual) = Σ(Residual_i - Mean_Residual)² / (n-1)，需排除离群值（>3σ）后重新计算以稳健估计。

## Corrected Claim

解释力 R² 的残差方差 Var(Residual) 计算：Residual = T_deal_observed - T_deal_predicted，其中 T_deal_predicted 由信号+启发式模型生成；Var(Residual) = Σ(Residual_i - Mean_Residual)² / (n-1)，需排除离群值（>3σ）后重新计算以稳健估计。

## Evidence

先验知识/题面给定，逻辑校验通过：残差定义、样本方差公式（n-1）及离群值处理均为标准统计学方法，逻辑自洽。

## Search Query

residual variance calculation for model fit R-squared
