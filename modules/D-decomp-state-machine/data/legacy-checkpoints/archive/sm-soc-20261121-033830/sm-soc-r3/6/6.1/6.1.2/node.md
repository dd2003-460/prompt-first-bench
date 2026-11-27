# N300: 分段回归 (Piecewise Regression) 模型设定：定义断点 T = 1.2 * P_median，模型为 Y = β0 + β1 * (P - 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N97

## Claim

分段回归 (Piecewise Regression) 模型设定：定义断点 T = 1.2 * P_median，模型为 Y = β0 + β1 * (P - P_median) * I(P < T) + β2 * (P - P_median) * I(P >= T) + ε，其中 Y 为咨询率，需检验 β1 和 β2 的显著性差异

## Corrected Claim

分段回归 (Piecewise Regression) 模型设定：定义断点 T = 1.2 * P_median，模型为 Y = β0 + β1 * (P - P_median) * I(P < T) + β2 * (P - P_median) * I(P >= T) + ε，其中 Y 为咨询率，需检验 β1 和 β2 的显著性差异

## Evidence

先验知识/题面给定，逻辑校验通过
