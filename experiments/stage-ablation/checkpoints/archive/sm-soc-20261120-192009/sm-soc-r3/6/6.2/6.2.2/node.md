# N301: 剩余买家的购买意愿提升量化：过滤后剩余买家（σ_price < 1.5）的平均购买意愿 Propensity_high = 0.4；转化率提升幅度 = (Pro

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N103

## Claim

剩余买家的购买意愿提升量化：过滤后剩余买家（σ_price < 1.5）的平均购买意愿 Propensity_high = 0.4；转化率提升幅度 = (Propensity_high / Propensity_baseline) - 1，其中 Propensity_baseline 为混合群体的加权平均意愿 0.22；计算得提升幅度 ≈ (0.4/0.22) - 1 = 81%，远高于 20% 的观测值，表明除筛选外还需考虑其他抑制因素（如信任成本）。

## Corrected Claim

剩余买家的购买意愿提升量化：过滤后剩余买家（σ_price < 1.5）的平均购买意愿 Propensity_high = 0.4；转化率提升幅度 = (Propensity_high / Propensity_baseline) - 1，其中 Propensity_baseline 为混合群体的加权平均意愿 0.22；计算得提升幅度 ≈ (0.4/0.22) - 1 = 81%，远高于 20% 的观测值，表明除筛选外还需考虑其他抑制因素（如信任成本）。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 (0.4/0.22 - 1 ≈ 0.818) 正确，且结论逻辑自洽（理论筛选提升远高于观测值，故推断存在其他抑制因素）。

## Search Query

conversion rate lift after price filtering effect
