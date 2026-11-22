# N56: 前1%对象的请求占比计算修正：基于 Pareto(β=0.9) 分布，前1%对象占据的请求比例应为 1 - (0.01)^{1-0.9} = 1 - 0.01^

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

前1%对象的请求占比计算修正：基于 Pareto(β=0.9) 分布，前1%对象占据的请求比例应为 1 - (0.01)^{1-0.9} = 1 - 0.01^{0.1} ≈ 20.6%，而非原陈述中的 1 - 0.9^{0.1}，原公式符号错误导致计算失效。

## Corrected Claim

前1%对象的请求占比计算修正：基于 Pareto(β=0.9) 分布，前1%对象占据的请求比例应为 1 - (0.01)^{1-0.9} = 1 - 0.01^{0.1} ≈ 20.6%，而非原陈述中的 1 - 0.9^{0.1}，原公式符号错误导致计算失效。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布CDF为 $1-x^{1-\beta}$，代入 $x=0.01, \beta=0.9$ 得 $1-0.01^{0.1} \approx 0.206$，计算正确且原公式 $1-0.9^{0.1}$ 确实错误。

## Search Query

Pareto distribution top 1 percent request share beta 0.9
