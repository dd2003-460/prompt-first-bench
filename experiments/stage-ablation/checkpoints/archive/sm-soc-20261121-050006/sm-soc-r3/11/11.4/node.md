# N354: 边界条件修正项：在有限样本或离散价格网格下，连续正态假设失效，需引入离散修正因子 δ_discrete，修正后的 ESS 条件为 σ²_pref > (C_in

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N114

## Claim

边界条件修正项：在有限样本或离散价格网格下，连续正态假设失效，需引入离散修正因子 δ_discrete，修正后的 ESS 条件为 σ²_pref > (C_info + δ_discrete) / (2 * V_match)，其中 δ_discrete 取决于最小价格步进单位（如 1 元）相对于 σ_pref 的比例。

## Corrected Claim

边界条件修正项：在有限样本或离散价格网格下，连续正态假设失效，需引入离散修正因子 δ_discrete，修正后的 ESS 条件为 σ²_pref > (C_info + δ_discrete) / (2 * V_match)，其中 δ_discrete 取决于最小价格步进单位（如 1 元）相对于 σ_pref 的比例。

## Evidence

先验知识/题面给定，逻辑校验通过
