# N154: 工作点 3（高流失低敏感）：当 ΔChurn = 8% 时，假设流失卖家为低活跃度长尾用户，Sensitivity_L 取低值 0.3，计算 ΔL = 0.08

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

工作点 3（高流失低敏感）：当 ΔChurn = 8% 时，假设流失卖家为低活跃度长尾用户，Sensitivity_L 取低值 0.3，计算 ΔL = 0.08 * 0.3 = 0.024，对应月度 GTV 下降幅度 ΔGTV = 2.4%，验证即使流失率较高，若用户质量低，对 GTV 的边际影响仍可能低于中流失场景，从而界定‘伤害显著’的非线性边界。

## Corrected Claim

工作点 3（高流失低敏感）：当 ΔChurn = 8% 时，假设流失卖家为低活跃度长尾用户，Sensitivity_L 取低值 0.3，计算 ΔL = 0.08 * 0.3 = 0.024，对应月度 GTV 下降幅度 ΔGTV = 2.4%，验证即使流失率较高，若用户质量低，对 GTV 的边际影响仍可能低于中流失场景，从而界定‘伤害显著’的非线性边界。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 0.08 * 0.3 = 0.024 (2.4%) 数学正确，且符合‘低敏感度流失对GTV影响较小’的经济直觉。

## Search Query

seller churn rate 8 percent platform liquidity sensitivity GTV impact high churn low sensitivity scenario
