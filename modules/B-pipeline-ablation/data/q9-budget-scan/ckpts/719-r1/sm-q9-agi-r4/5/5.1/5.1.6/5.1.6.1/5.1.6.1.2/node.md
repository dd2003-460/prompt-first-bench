# N666: 幻觉率与复杂度评分的线性回归模型：Hallucination_Rate = a + b*Complexity_Score，需采集 N≥50 个样本点进行最小二乘

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N243

## Claim

幻觉率与复杂度评分的线性回归模型：Hallucination_Rate = a + b*Complexity_Score，需采集 N≥50 个样本点进行最小二乘拟合，得到斜率 b 和截距 a，R²>0.8 视为有效模型

## Corrected Claim

幻觉率与复杂度评分的线性回归模型：Hallucination_Rate = a + b*Complexity_Score，需采集 N≥50 个样本点进行最小二乘拟合，得到斜率 b 和截距 a，R²>0.8 视为有效模型

## Evidence

先验知识/题面给定，逻辑校验通过：线性回归模型定义及最小二乘法拟合标准流程符合统计学基本原理，N≥50满足大数定律下的估计稳定性要求，R²>0.8作为模型有效性阈值在工程实践中属于合理且常见的经验标准。
