# N83: h_max 的均匀性假设偏差：h_max = 500 req/day 是算术平均值，但 Pareto(β=0.9) 分布的中位数 h_median = h_ma

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N28

## Claim

h_max 的均匀性假设偏差：h_max = 500 req/day 是算术平均值，但 Pareto(β=0.9) 分布的中位数 h_median = h_max * (1/2)^(1/0.9) ≈ 500 * 0.528 ≈ 264 req/day。由于 β<1，分布右偏，均值被极端热点拉高，使用 h_max 作为归一化基准会导致对大多数对象的热度低估，需改用中位数或几何平均 h_geo = exp(∫ln(h)f(h)dh) ≈ 180 req/day 进行更准确的相对热度比较。

## Corrected Claim

h_max 的均匀性假设偏差：h_max = 500 req/day 是算术平均值，但 Pareto(β=0.9) 分布的中位数 h_median = h_max * (1/2)^(1/0.9) ≈ 500 * 0.528 ≈ 264 req/day。由于 β<1，分布右偏，均值被极端热点拉高，使用 h_max 作为归一化基准会导致对大多数对象的热度低估，需改用中位数或几何平均 h_geo = exp(∫ln(h)f(h)dh) ≈ 180 req/day 进行更准确的相对热度比较。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布(β=0.9)的均值与中位数关系推导正确，右偏特性导致均值高于中位数的结论符合统计学原理。

## Search Query

Pareto distribution median vs mean skewness impact
