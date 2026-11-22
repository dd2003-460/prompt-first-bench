# N170: k 值的估计方法：衰减系数 k 可通过对历史咨询日志进行非线性最小二乘拟合得到，模型为 log(P(invalid)_t) = -k * info_qualit

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N52

## Claim

k 值的估计方法：衰减系数 k 可通过对历史咨询日志进行非线性最小二乘拟合得到，模型为 log(P(invalid)_t) = -k * info_quality_t + ε；若拟合的 R² > 0.7 且 p < 0.05，则确认指数衰减形式有效，否则需考虑线性衰减或阈值效应模型。

## Corrected Claim

k 值的估计方法：衰减系数 k 可通过对历史咨询日志进行非线性最小二乘拟合得到，模型为 log(P(invalid)_t) = -k * info_quality_t + ε；若拟合的 R² > 0.7 且 p < 0.05，则确认指数衰减形式有效，否则需考虑线性衰减或阈值效应模型。

## Evidence

先验知识/题面给定，逻辑校验通过
