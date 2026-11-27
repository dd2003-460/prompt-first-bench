# N153: 共享随机源 R_p 的方差 σ_R² 定义为卖家对市场需求预测的基础不确定性，其数值可通过历史同类商品成交周期的预测残差平方和除以样本量估计，σ_R² = Va

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N43

## Claim

共享随机源 R_p 的方差 σ_R² 定义为卖家对市场需求预测的基础不确定性，其数值可通过历史同类商品成交周期的预测残差平方和除以样本量估计，σ_R² = Var(ε_p_residual)。

## Corrected Claim

共享随机源 R_p 的方差 σ_R² 定义为卖家对市场需求预测的基础不确定性，其数值可通过历史同类商品成交周期的预测残差平方和除以样本量估计，σ_R² = Var(ε_p_residual)。

## Evidence

先验知识/题面给定，逻辑校验通过：方差定义为预测残差的二阶中心矩，用样本残差平方和除以样本量（或自由度）进行无偏估计符合统计学基本原理，量纲与逻辑自洽。

## Search Query

estimation of demand forecast uncertainty variance for second-hand goods sellers
