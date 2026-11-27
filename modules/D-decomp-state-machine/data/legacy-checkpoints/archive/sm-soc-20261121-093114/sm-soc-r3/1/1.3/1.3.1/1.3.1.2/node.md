# N107: 感知噪声与真实质量 Q_true 的独立性检验：在正态分布假设下，ε_buyer 与 Q_true 的协方差 Cov(ε_buyer, Q_true) 应接近 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N33

## Claim

感知噪声与真实质量 Q_true 的独立性检验：在正态分布假设下，ε_buyer 与 Q_true 的协方差 Cov(ε_buyer, Q_true) 应接近 0，若 |Cov|/σ_perception > 0.1，则需引入相关项修正模型，量化为修正后的噪声分布 N(ρ * Q_true, σ_perception^2)，其中 ρ 为相关系数。

## Corrected Claim

感知噪声与真实质量 Q_true 的独立性检验：在正态分布假设下，ε_buyer 与 Q_true 的协方差 Cov(ε_buyer, Q_true) 应接近 0，若 |Cov|/σ_perception > 0.1，则需引入相关项修正模型，量化为修正后的噪声分布 N(ρ * Q_true, σ_perception^2)，其中 ρ 为相关系数。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

perception noise independence true quality covariance correction
