# N153: 价格敏感度系数 β1 的估计方法：采用逻辑回归模型 ln(P(buy)/(1-P(buy))) = β0 + β1*(Price - intrinsic_val

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N46

## Claim

价格敏感度系数 β1 的估计方法：采用逻辑回归模型 ln(P(buy)/(1-P(buy))) = β0 + β1*(Price - intrinsic_value)/intrinsic_value + ε，β1 的估计值需报告标准误和 95% 置信区间；若置信区间包含 0，则 β1 不显著，需检查样本量或协变量设定。

## Corrected Claim

价格敏感度系数 β1 的估计方法：采用逻辑回归模型 ln(P(buy)/(1-P(buy))) = β0 + β1*(Price - intrinsic_value)/intrinsic_value + ε，β1 的估计值需报告标准误和 95% 置信区间；若置信区间包含 0，则 β1 不显著，需检查样本量或协变量设定。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述描述了标准的Logistic回归模型设定及统计推断规范（报告标准误、置信区间、显著性检验），符合计量经济学与统计学的基本原理，无逻辑矛盾。
