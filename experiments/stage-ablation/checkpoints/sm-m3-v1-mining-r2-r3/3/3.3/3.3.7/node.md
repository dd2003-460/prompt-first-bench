# N29: 定义置信度降级映射函数：Confidence_Score = Base_Score * (1 - Deviation_Ratio^2)，其中 Deviation

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13, N15, N16

## Claim

定义置信度降级映射函数：Confidence_Score = Base_Score * (1 - Deviation_Ratio^2)，其中 Deviation_Ratio = |k_given - k_ref|/k_ref = 1.239，导致得分大幅下降

## Corrected Claim

定义置信度降级映射函数：Confidence_Score = Base_Score * (1 - Deviation_Ratio^2)，其中 Deviation_Ratio = |k_given - k_ref|/k_ref = 1.239，导致得分大幅下降

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构合理，代入数值计算显示得分显著下降，符合描述

## Search Query

confidence score degradation model based on input deviation
