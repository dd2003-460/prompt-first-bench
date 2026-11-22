# N174: PSM 匹配的平衡性检验指标：计算匹配前后协变量 X_i 的标准化均值差 (SMD)，定义 SMD_i = |Mean_X_treat - Mean_X_con

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

PSM 匹配的平衡性检验指标：计算匹配前后协变量 X_i 的标准化均值差 (SMD)，定义 SMD_i = |Mean_X_treat - Mean_X_control| / Pooled_Std_X；若匹配后所有协变量的 |SMD_i| < 0.1，则认为匹配成功，反事实估计有效；否则需调整匹配算法或协变量集合。

## Corrected Claim

PSM 匹配的平衡性检验指标：计算匹配前后协变量 X_i 的标准化均值差 (SMD)，定义 SMD_i = |Mean_X_treat - Mean_X_control| / Pooled_Std_X；若匹配后所有协变量的 |SMD_i| < 0.1，则认为匹配成功，反事实估计有效；否则需调整匹配算法或协变量集合。

## Evidence

先验知识/题面给定，逻辑校验通过
