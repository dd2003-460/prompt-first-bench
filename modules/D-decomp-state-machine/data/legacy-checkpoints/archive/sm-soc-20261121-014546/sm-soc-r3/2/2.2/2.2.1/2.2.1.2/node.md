# N198: 高挂价落入上尾90%分位的概率密度函数值 f(P_90) 的具体数值，需结合历史成交价均值 μ 和标准差 σ 计算：f(P_90) = (1/σ) * f_st

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N56

## Claim

高挂价落入上尾90%分位的概率密度函数值 f(P_90) 的具体数值，需结合历史成交价均值 μ 和标准差 σ 计算：f(P_90) = (1/σ) * f_standardized(1.28)，其中 f_standardized 为标准正态或对应偏态分布的PDF值。

## Corrected Claim

高挂价落入上尾90%分位的概率密度函数值 f(P_90) 的具体数值，需结合历史成交价均值 μ 和标准差 σ 计算：f(P_90) = (1/σ) * f_standardized(1.28)，其中 f_standardized 为标准正态或对应偏态分布的PDF值。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述正确描述了正态分布（或标准化分布）PDF的缩放性质，即 f(x) = (1/σ) * φ((x-μ)/σ)，其中 P_90 对应标准化值 1.28（90%分位），公式推导符合概率论基本定义。
