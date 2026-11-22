# N228: 流失率系数 α 的回归估计模型：Churn_rate_t = β0 + α * PU_t + δ * Price_Volatility_t + ε_t，其中 α

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75

## Claim

流失率系数 α 的回归估计模型：Churn_rate_t = β0 + α * PU_t + δ * Price_Volatility_t + ε_t，其中 α 为待估系数，需使用面板数据（Panel Data）以控制卖家固定效应，避免遗漏变量偏差。

## Corrected Claim

流失率系数 α 的回归估计模型：Churn_rate_t = β0 + α * PU_t + δ * Price_Volatility_t + ε_t，其中 α 为待估系数，需使用面板数据（Panel Data）以控制卖家固定效应，避免遗漏变量偏差。

## Evidence

先验知识/题面给定，逻辑校验通过：面板数据模型是控制固定效应和遗漏变量偏差的标准计量经济学方法，模型设定符合因果推断逻辑。
