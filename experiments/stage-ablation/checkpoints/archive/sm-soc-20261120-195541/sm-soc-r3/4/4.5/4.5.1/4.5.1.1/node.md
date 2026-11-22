# N152: 工作点 1（低流失高敏感）：当 ΔChurn = 2% 时，假设卖家流失主要影响高活跃度用户，Sensitivity_L 取高值 0.8，计算 ΔL = 0.0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

工作点 1（低流失高敏感）：当 ΔChurn = 2% 时，假设卖家流失主要影响高活跃度用户，Sensitivity_L 取高值 0.8，计算 ΔL = 0.02 * 0.8 = 0.016，对应月度 GTV 下降幅度 ΔGTV = 1.6%，判断该损失是否低于平台月度波动噪声（如 2%）。

## Corrected Claim

工作点 1（低流失高敏感）：当 ΔChurn = 2% 时，假设卖家流失主要影响高活跃度用户，Sensitivity_L 取高值 0.8，计算 ΔL = 0.02 * 0.8 = 0.016，对应月度 GTV 下降幅度 ΔGTV = 1.6%，判断该损失是否低于平台月度波动噪声（如 2%）。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 0.02 * 0.8 = 0.016 (1.6%) 数学正确，且 1.6% < 2% 的判断符合逻辑。

## Search Query

seller churn rate 2 percent platform liquidity sensitivity GTV impact low churn scenario
