# N132: 共享随机源：商品真实质量分布 Q 的先验方差 Var(Q) = σ_quality_total²，其数值取决于品类，假设 σ_quality_total = 0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N33

## Claim

共享随机源：商品真实质量分布 Q 的先验方差 Var(Q) = σ_quality_total²，其数值取决于品类，假设 σ_quality_total = 0.2 * μ_price（即变异系数20%），且买家对 Q 的观测噪声服从 N(0, σ_obs²)，其中 σ_obs = 0.1 * μ_price。

## Corrected Claim

共享随机源：商品真实质量分布 Q 的先验方差 Var(Q) = σ_quality_total²，其数值取决于品类，假设 σ_quality_total = 0.2 * μ_price（即变异系数20%），且买家对 Q 的观测噪声服从 N(0, σ_obs²)，其中 σ_obs = 0.1 * μ_price。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

used goods quality variance standard deviation empirical data
