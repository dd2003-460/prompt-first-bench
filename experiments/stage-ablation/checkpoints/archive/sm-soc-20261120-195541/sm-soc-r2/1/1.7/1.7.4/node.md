# N43: 平台流动性指标 L 的下降幅度 ΔL 并非固定为 0.05，而是与卖家流失率 Churn_Rate 正相关，公式为 ΔL = Churn_Rate * Sens

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11, N12, N13

## Claim

平台流动性指标 L 的下降幅度 ΔL 并非固定为 0.05，而是与卖家流失率 Churn_Rate 正相关，公式为 ΔL = Churn_Rate * Sensitivity_L，其中 Sensitivity_L 为流动性对流失率的敏感系数，需通过历史数据回归分析确定。

## Corrected Claim

平台流动性指标 L 的下降幅度 ΔL 并非固定为 0.05，而是与卖家流失率 Churn_Rate 正相关，公式为 ΔL = Churn_Rate * Sensitivity_L，其中 Sensitivity_L 为流动性对流失率的敏感系数，需通过历史数据回归分析确定。

## Evidence

先验知识/题面给定，逻辑校验通过
