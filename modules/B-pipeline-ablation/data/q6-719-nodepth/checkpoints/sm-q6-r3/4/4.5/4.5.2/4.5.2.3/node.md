# N298: 隐性运维成本规模效应指数 β 的推导：通过对比 N=10 时总成本 105k 元/月与 N=20 时的预估成本，若 C_total(N) = C_fixed +

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N103

## Claim

隐性运维成本规模效应指数 β 的推导：通过对比 N=10 时总成本 105k 元/月与 N=20 时的预估成本，若 C_total(N) = C_fixed + C_var_per_pop × N，则 β 并非严格 1/10，而是取决于 C_fixed 在总成本中的占比，需代入具体 C_fixed 和 C_var 值验证 116k 的估算是否成立。

## Corrected Claim

隐性运维成本规模效应指数 β 的推导：通过对比 N=10 时总成本 105k 元/月与 N=20 时的预估成本，若 C_total(N) = C_fixed + C_var_per_pop × N，则 β 并非严格 1/10，而是取决于 C_fixed 在总成本中的占比，需代入具体 C_fixed 和 C_var 值验证 116k 的估算是否成立。

## Evidence

先验知识/题面给定，逻辑校验通过：成本模型 C_total(N) = C_fixed + C_var_per_pop × N 中，若 C_fixed > 0，则边际成本递减，规模效应指数 β 确实不等于 1（或 1/10 等线性比例），而是取决于固定成本占比，推导逻辑自洽。

## Search Query

operational cost scaling law edge computing nodes sub-linear growth
