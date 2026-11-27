# N153: 工作点 2（中流失中敏感）：当 ΔChurn = 5% 时，假设流失卖家为平均活跃度，Sensitivity_L 取中值 0.5，计算 ΔL = 0.05 * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

工作点 2（中流失中敏感）：当 ΔChurn = 5% 时，假设流失卖家为平均活跃度，Sensitivity_L 取中值 0.5，计算 ΔL = 0.05 * 0.5 = 0.025，对应月度 GTV 下降幅度 ΔGTV = 2.5%，需对比该数值是否超过平台设定的‘显著伤害’阈值（如 3%）。

## Corrected Claim

工作点 2（中流失中敏感）：当 ΔChurn = 5% 时，假设流失卖家为平均活跃度，Sensitivity_L 取中值 0.5，计算 ΔL = 0.05 * 0.5 = 0.025，对应月度 GTV 下降幅度 ΔGTV = 2.5%，需对比该数值是否超过平台设定的‘显著伤害’阈值（如 3%）。

## Evidence

先验知识/题面给定，逻辑校验通过：0.05 * 0.5 = 0.025 即 2.5%，计算无误，且 2.5% < 3% 的阈值对比逻辑自洽。

## Search Query

seller churn rate 5 percent platform liquidity sensitivity GTV impact medium churn scenario
