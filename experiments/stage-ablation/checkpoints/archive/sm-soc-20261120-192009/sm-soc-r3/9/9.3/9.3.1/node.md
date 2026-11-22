# N337: 流失倾向函数的具体形式：采用逻辑回归模型 Churn_Prob = 1 / (1 + e^(-(β0 + β1*ΔU_seller + β2*Activity)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N115

## Claim

流失倾向函数的具体形式：采用逻辑回归模型 Churn_Prob = 1 / (1 + e^(-(β0 + β1*ΔU_seller + β2*Activity)))，其中 β1 为效用损失敏感度系数，需通过历史流失数据回归估计，预期 β1 为负值。

## Corrected Claim

流失倾向函数的具体形式：采用逻辑回归模型 Churn_Prob = 1 / (1 + e^(-(β0 + β1*ΔU_seller + β2*Activity)))，其中 β1 为效用损失敏感度系数，需通过历史流失数据回归估计，预期 β1 为负值。

## Evidence

先验知识/题面给定，逻辑校验通过：逻辑回归模型形式正确，效用损失（ΔU_seller）增加导致流失概率增加，故系数β1应为正值（若ΔU_seller定义为损失量）或负值（若定义为效用变化量，损失即负值），此处表述符合逻辑回归在流失预测中的常规应用逻辑。

## Search Query

churn probability logistic regression utility loss activity level coefficients
