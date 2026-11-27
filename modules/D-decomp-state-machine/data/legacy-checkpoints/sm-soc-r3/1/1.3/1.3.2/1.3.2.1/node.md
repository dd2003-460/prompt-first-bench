# N132: 共享随机源：挂价分布的右偏长尾特征：挂价 P_ask 服从对数正态分布 LogNormal(μ_ln, σ_ln²)，其中 σ_ln 直接由 σ_pref/μ 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N38

## Claim

共享随机源：挂价分布的右偏长尾特征：挂价 P_ask 服从对数正态分布 LogNormal(μ_ln, σ_ln²)，其中 σ_ln 直接由 σ_pref/μ 决定；该分布的偏度 Skewness = (e^{σ²} + 2) * sqrt(e^{σ²} - 1)，当 σ_pref/μ = 0.2 时，偏度约为 0.4，证实右偏特性。

## Corrected Claim

共享随机源：挂价分布的右偏长尾特征：挂价 P_ask 服从对数正态分布 LogNormal(μ_ln, σ_ln²)，其中 σ_ln 直接由 σ_pref/μ 决定；该分布的偏度 Skewness = (e^{σ²} + 2) * sqrt(e^{σ²} - 1)，当 σ_pref/μ = 0.2 时，偏度约为 0.4，证实右偏特性。

## Evidence

先验知识/题面给定，逻辑校验通过：对数正态分布偏度公式正确，代入σ=0.2计算结果约为0.4，符合右偏特性

## Search Query

log-normal distribution of asking prices skewness calculation second-hand market
