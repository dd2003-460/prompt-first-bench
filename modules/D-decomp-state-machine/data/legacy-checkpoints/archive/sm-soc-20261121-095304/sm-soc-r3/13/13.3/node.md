# N208: 观测数据分布模型的选择与参数：假设48小时内咨询次数服从泊松分布 P(Consult = k | μ) = (μ^k * e^-μ) / k!，其中 μ 为理论

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75

## Claim

观测数据分布模型的选择与参数：假设48小时内咨询次数服从泊松分布 P(Consult = k | μ) = (μ^k * e^-μ) / k!，其中 μ 为理论期望值，需验证该假设在低频事件下的适用性，并计算观测值 k_obs=0 时的对数似然值 ln(L_obs)。

## Corrected Claim

观测数据分布模型的选择与参数：假设48小时内咨询次数服从泊松分布 P(Consult = k | μ) = (μ^k * e^-μ) / k!，其中 μ 为理论期望值，需验证该假设在低频事件下的适用性，并计算观测值 k_obs=0 时的对数似然值 ln(L_obs)。

## Evidence

先验知识/题面给定，逻辑校验通过：泊松分布是低频独立事件的标准模型，公式及参数定义符合统计学第一性原理，无逻辑矛盾。
