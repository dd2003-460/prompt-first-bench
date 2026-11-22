# N192: SensitivityFactor 的回归估计量：基于历史A/B测试数据，模型设定为 ΔT/T_old = β * ΔWeight + ε，其中 β 即为 Se

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

SensitivityFactor 的回归估计量：基于历史A/B测试数据，模型设定为 ΔT/T_old = β * ΔWeight + ε，其中 β 即为 SensitivityFactor，需报告 95% 置信区间及样本量 n_min ≥ 30 组以通过显著性检验 (p < 0.05)。

## Corrected Claim

SensitivityFactor 的回归估计量：基于历史A/B测试数据，模型设定为 ΔT/T_old = β * ΔWeight + ε，其中 β 即为 SensitivityFactor，需报告 95% 置信区间及样本量 n_min ≥ 30 组以通过显著性检验 (p < 0.05)。

## Evidence

先验知识/题面给定，逻辑校验通过：线性回归模型设定符合统计学常规，n≥30满足中心极限定理近似正态分布要求，p<0.05为标准显著性水平，量纲与逻辑自洽。
