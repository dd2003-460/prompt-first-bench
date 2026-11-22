# N63: 混淆变量控制方程：为剥离季节性影响，需构建回归模型 T_short = β0 + β1*High_Price_Flag + β2*Season_Dummy + 

- **status**: pending
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

父节点级核验未通过：不完备（子节点正交性良好，分别针对季节性变量构造、库存变量量化及多重共线性检验，无重叠。但完备性不足：父节点明确提到‘当前缺乏该回归系数估计值’且目标是‘验证信号筛选机制’，这意味着核心任务是执行回归并评估 β1 的显著性。现有子节点仅覆盖了模型构建中的变量定义和诊断步骤，缺失了‘执行回归分析以获取 β1 估计值及其 p 值’这一核心行动步骤，也未涉及模型误差项 ε 的独立性/正态性检验（对于时间序列数据尤为重要）。）
