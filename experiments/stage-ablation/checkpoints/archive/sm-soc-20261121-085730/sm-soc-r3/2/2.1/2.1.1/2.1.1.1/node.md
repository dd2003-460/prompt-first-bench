# N181: 信号强度系数 k 的估计需基于对数线性回归模型 ln(T) = α - k * ln(1 + Premium)，其中 Premium = (P - C_ref)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59

## Claim

信号强度系数 k 的估计需基于对数线性回归模型 ln(T) = α - k * ln(1 + Premium)，其中 Premium = (P - C_ref)/C_ref，k 的 MLE 估计值需通过最大似然估计法计算，而非简单最小二乘，以处理异方差性。

## Corrected Claim

信号强度系数 k 的估计需基于对数线性回归模型 ln(T) = α - k * ln(1 + Premium)，其中 Premium = (P - C_ref)/C_ref，k 的 MLE 估计值需通过最大似然估计法计算，而非简单最小二乘，以处理异方差性。

## Evidence

先验知识/题面给定，逻辑校验通过
