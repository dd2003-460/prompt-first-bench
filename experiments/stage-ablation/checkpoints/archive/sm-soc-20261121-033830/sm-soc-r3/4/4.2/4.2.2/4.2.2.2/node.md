# N224: 候选A下的总成交概率 P(Sale|Intervention_A) 计算式：P(Sale|Intervention_A) = P(Sale|P_max) * M

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

候选A下的总成交概率 P(Sale|Intervention_A) 计算式：P(Sale|Intervention_A) = P(Sale|P_max) * M_clipped + ∫_{P_min}^{P_max} P(Sale|P) * f(P) dP，其中 P(Sale|P) 沿用 N78 的弹性模型 P(Sale|P) ≈ P(Sale|P_ref) * (P_ref / P)^η，η ∈ [0.3, 0.5]。

## Corrected Claim

候选A下的总成交概率 P(Sale|Intervention_A) 计算式：P(Sale|Intervention_A) = P(Sale|P_max) * M_clipped + ∫_{P_min}^{P_max} P(Sale|P) * f(P) dP，其中 P(Sale|P) 沿用 N78 的弹性模型 P(Sale|P) ≈ P(Sale|P_ref) * (P_ref / P)^η，η ∈ [0.3, 0.5]。

## Evidence

先验知识/题面给定，逻辑校验通过
