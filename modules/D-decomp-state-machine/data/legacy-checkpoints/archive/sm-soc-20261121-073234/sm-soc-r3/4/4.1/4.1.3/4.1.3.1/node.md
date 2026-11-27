# N248: 证据相关性系数 ρ_E 的量化定义：ρ_E = Cov(T_match, C_consult) / (σ_T * σ_C)，其中 T_match 为成交周期，C

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

证据相关性系数 ρ_E 的量化定义：ρ_E = Cov(T_match, C_consult) / (σ_T * σ_C)，其中 T_match 为成交周期，C_consult 为降价后48小时咨询数。若 |ρ_E| > 0.6，则需使用联合概率 P(E1, E2|H) 而非独立乘积。

## Corrected Claim

证据相关性系数 ρ_E 的量化定义：ρ_E = Cov(T_match, C_consult) / (σ_T * σ_C)，其中 T_match 为成交周期，C_consult 为降价后48小时咨询数。若 |ρ_E| > 0.6，则需使用联合概率 P(E1, E2|H) 而非独立乘积。

## Evidence

先验知识/题面给定，逻辑校验通过
