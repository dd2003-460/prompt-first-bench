# N325: Consistency_Index 的分母 Var(σ_noise) 需通过残差分析估算：在回归模型 T_close = α + β*ΔP_ask + ε 中，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N112

## Claim

Consistency_Index 的分母 Var(σ_noise) 需通过残差分析估算：在回归模型 T_close = α + β*ΔP_ask + ε 中，σ_noise 对应残差 ε 的标准差，Var(σ_noise) 即为残差方差，需报告其标准误以评估估计精度。

## Corrected Claim

Consistency_Index 的分母 Var(σ_noise) 需通过残差分析估算：在回归模型 T_close = α + β*ΔP_ask + ε 中，σ_noise 对应残差 ε 的标准差，Var(σ_noise) 即为残差方差，需报告其标准误以评估估计精度。

## Evidence

先验知识/题面给定，逻辑校验通过：在标准线性回归模型中，残差的标准差确实对应噪声标准差，其方差即为残差方差，且报告标准误是评估估计精度的标准统计实践。
