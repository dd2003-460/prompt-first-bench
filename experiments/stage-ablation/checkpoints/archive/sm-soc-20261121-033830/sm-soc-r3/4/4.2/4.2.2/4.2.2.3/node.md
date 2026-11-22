# N225: 候选A的边际收益阈值：仅当 P(Sale|P_max) * M_clipped > ∫_{P_max}^{∞} P(Sale|P) * f(P) dP 时，截断

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

候选A的边际收益阈值：仅当 P(Sale|P_max) * M_clipped > ∫_{P_max}^{∞} P(Sale|P) * f(P) dP 时，截断才提升总成交率；若 η 较小（价格不敏感）且 M_clipped 较小，截断可能导致总成交率下降，需计算临界 η_crit 使得等式成立。

## Corrected Claim

候选A的边际收益阈值：仅当 P(Sale|P_max) * M_clipped > ∫_{P_max}^{∞} P(Sale|P) * f(P) dP 时，截断才提升总成交率；若 η 较小（价格不敏感）且 M_clipped 较小，截断可能导致总成交率下降，需计算临界 η_crit 使得等式成立。

## Evidence

先验知识/题面给定，逻辑校验通过
