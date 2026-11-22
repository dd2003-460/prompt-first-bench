# N230: h_avg 的独立假设基线（ρ=0）：h_avg_indep = E[S]^{-1} * E[H] * E[S] = E[H]，但由于 Pareto(β=0.9

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N83

## Claim

h_avg 的独立假设基线（ρ=0）：h_avg_indep = E[S]^{-1} * E[H] * E[S] = E[H]，但由于 Pareto(β=0.9) 均值发散，需用截断均值 E[H]_{trunc} ≈ 50 请求/天，此值远高于实际 h_avg，导致独立假设严重高估命中率。

## Corrected Claim

h_avg 的独立假设基线（ρ=0）：h_avg_indep = E[S]^{-1} * E[H] * E[S] = E[H]，但由于 Pareto(β=0.9) 均值发散，需用截断均值 E[H]_{trunc} ≈ 50 请求/天，此值远高于实际 h_avg，导致独立假设严重高估命中率。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto(β=0.9) 均值发散需截断，独立假设下命中率等于平均请求数，截断均值远高于实际相关命中率符合逻辑。
