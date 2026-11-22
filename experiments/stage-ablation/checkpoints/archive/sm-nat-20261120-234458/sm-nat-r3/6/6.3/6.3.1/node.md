# N180: N_miss (必然未命中对象数) 的最小值计算：在 Pareto(β=0.9) 分布下，若所有 100,000 对象在观察窗口内至少被请求一次，则 N_mis

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N59

## Claim

N_miss (必然未命中对象数) 的最小值计算：在 Pareto(β=0.9) 分布下，若所有 100,000 对象在观察窗口内至少被请求一次，则 N_miss = 0；否则 N_miss = N_total - |{i: Request_i > 0}|，需通过泊松分布 P(λ=500, T=1day) 估算从未被请求的对象数

## Corrected Claim

N_miss (必然未命中对象数) 的最小值计算：在 Pareto(β=0.9) 分布下，若所有 100,000 对象在观察窗口内至少被请求一次，则 N_miss = 0；否则 N_miss = N_total - |{i: Request_i > 0}|，需通过泊松分布 P(λ=500, T=1day) 估算从未被请求的对象数

## Evidence

先验知识/题面给定，逻辑校验通过：N_miss 的定义（总对象数减去至少被请求一次的对象数）在逻辑上自洽，且当所有对象至少被请求一次时 N_miss=0 的推导符合集合论基本逻辑；泊松分布用于估算低频访问对象是合理的统计近似方法。
