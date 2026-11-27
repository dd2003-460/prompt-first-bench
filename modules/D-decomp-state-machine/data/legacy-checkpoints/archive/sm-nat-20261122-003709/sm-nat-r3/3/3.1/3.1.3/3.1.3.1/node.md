# N156: 独立性假设失效的偏差项 δ_independence 量化：δ = P(CapMiss ∩ InvalMiss) - P(CapMiss)P(InvalMiss

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

独立性假设失效的偏差项 δ_independence 量化：δ = P(CapMiss ∩ InvalMiss) - P(CapMiss)P(InvalMiss)，在 ρ=-0.3 且更新率与热度正相关（假设 λ_i = λ_base * (p_i / E[p])^0.5）场景下，需计算协方差项，若 δ < 0.005 则公式 M_total ≈ M_cap + M_inv 误差可忽略。

## Corrected Claim

独立性假设失效的偏差项 δ_independence 量化：δ = P(CapMiss ∩ InvalMiss) - P(CapMiss)P(InvalMiss)，在 ρ=-0.3 且更新率与热度正相关（假设 λ_i = λ_base * (p_i / E[p])^0.5）场景下，需计算协方差项，若 δ < 0.005 则公式 M_total ≈ M_cap + M_inv 误差可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过
