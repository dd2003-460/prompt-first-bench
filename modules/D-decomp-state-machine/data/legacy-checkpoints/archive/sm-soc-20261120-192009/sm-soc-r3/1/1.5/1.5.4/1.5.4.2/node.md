# N171: C_total(t) 的动态基准：总咨询率 C_total(t) 并非恒定，而是受市场热度影响，C_total(t) = C_base * (1 + δ_tre

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N52

## Claim

C_total(t) 的动态基准：总咨询率 C_total(t) 并非恒定，而是受市场热度影响，C_total(t) = C_base * (1 + δ_trend * Trend_index_t)；若忽略 Trend_index 的变化，会导致对 info_quality 效应的估计产生偏差，需引入时间固定效应进行控制。

## Corrected Claim

C_total(t) 的动态基准：总咨询率 C_total(t) 并非恒定，而是受市场热度影响，C_total(t) = C_base * (1 + δ_trend * Trend_index_t)；若忽略 Trend_index 的变化，会导致对 info_quality 效应的估计产生偏差，需引入时间固定效应进行控制。

## Evidence

先验知识/题面给定，逻辑校验通过
