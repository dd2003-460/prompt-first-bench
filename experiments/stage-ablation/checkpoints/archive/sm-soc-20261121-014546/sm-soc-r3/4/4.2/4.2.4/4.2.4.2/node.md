# N297: 下游投影1：卖家对警告的遵从率 r_compliance 与心理阻力 λ_resistance 呈负指数关系，r_compliance = exp(-κ * λ

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N88, N89, N90

## Claim

下游投影1：卖家对警告的遵从率 r_compliance 与心理阻力 λ_resistance 呈负指数关系，r_compliance = exp(-κ * λ_resistance)，其中 κ = 0.3 为敏感度系数，当 λ_resistance = 2.5 时，r_compliance ≈ 0.47。

## Corrected Claim

下游投影1：卖家对警告的遵从率 r_compliance 与心理阻力 λ_resistance 呈负指数关系，r_compliance = exp(-κ * λ_resistance)，其中 κ = 0.3 为敏感度系数，当 λ_resistance = 2.5 时，r_compliance ≈ 0.47。

## Evidence

先验知识/题面给定，逻辑校验通过：计算 exp(-0.3 * 2.5) = exp(-0.75) ≈ 0.4724，与陈述中的 0.47 一致，数学推导自洽。

## Search Query

price adjustment compliance rate loss aversion exponential decay model
