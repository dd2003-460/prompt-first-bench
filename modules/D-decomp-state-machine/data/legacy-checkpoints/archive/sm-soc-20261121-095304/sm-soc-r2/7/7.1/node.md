# N63: 混淆变量控制方程：为剥离季节性影响，需构建回归模型 T_short = β0 + β1*High_Price_Flag + β2*Season_Dummy + 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

混淆变量控制方程：为剥离季节性影响，需构建回归模型 T_short = β0 + β1*High_Price_Flag + β2*Season_Dummy + β3*Inventory_Shift + ε，其中 β1 的显著性(p<0.05)是验证信号筛选机制(即N7)的必要条件，当前缺乏该回归系数估计值。

## Corrected Claim

混淆变量控制方程：为剥离季节性影响，需构建回归模型 T_short = β0 + β1*High_Price_Flag + β2*Season_Dummy + β3*Inventory_Shift + ε，其中 β1 的显著性(p<0.05)是验证信号筛选机制(即N7)的必要条件，当前缺乏该回归系数估计值。

## Evidence

先验知识/题面给定，逻辑校验通过：该回归方程结构符合计量经济学中控制混淆变量（季节性、库存变动）以识别因果效应（High_Price_Flag）的标准范式，β1显著性作为验证信号筛选机制的必要条件在逻辑上自洽。
