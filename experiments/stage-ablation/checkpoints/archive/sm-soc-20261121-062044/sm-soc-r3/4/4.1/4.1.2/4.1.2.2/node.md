# N196: 小样本修正项的线性系数验证：检验公式 Cap_conf = 0.5 + (n-30)/100 * 0.4 中的斜率 0.004 是否与贝叶斯收缩系数一致；若实际

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N70

## Claim

小样本修正项的线性系数验证：检验公式 Cap_conf = 0.5 + (n-30)/100 * 0.4 中的斜率 0.004 是否与贝叶斯收缩系数一致；若实际数据中 n=20 时观测置信度上限 < 0.5，则需引入非线性修正项 λ_correction = 1 - exp(-(n-30)/k)，k 为衰减常数，需通过最大似然估计校准。

## Corrected Claim

小样本修正项的线性系数验证：检验公式 Cap_conf = 0.5 + (n-30)/100 * 0.4 中的斜率是否与贝叶斯收缩系数一致；若实际数据中 n=20 时观测置信度上限低于基准值，则需引入非线性修正项 λ_correction = 1 - exp(-(n-30)/k)，k 为衰减常数，需通过最大似然估计校准。

## Evidence

[质询]该陈述包含具体的经验性参数（如斜率0.004、阈值n=20、置信度上限0.5）和特定的统计模型假设（贝叶斯收缩一致性、非线性修正形式），这些属于经验事实或特定模型设定，无法从第一性原理严格推导，且缺乏外部来源支持其具体数值和逻辑关联的准确性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Bayesian shrinkage coefficient small sample confidence interval correction linear vs exponential
