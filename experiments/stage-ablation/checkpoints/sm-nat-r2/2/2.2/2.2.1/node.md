# N49: 对象 i 的访问间隔分布：对于 Pareto(β=0.9) 热度分布，对象 i 的请求间隔 T_i 服从指数分布，其均值 E[T_i] = 1 / λ_i，其中

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

对象 i 的访问间隔分布：对于 Pareto(β=0.9) 热度分布，对象 i 的请求间隔 T_i 服从指数分布，其均值 E[T_i] = 1 / λ_i，其中 λ_i = r_i * (5000万/天) / N_total，r_i 为对象 i 的相对热度。

## Corrected Claim

对象 i 的访问间隔分布：对于 Pareto(β=0.9) 热度分布，对象 i 的请求间隔 T_i 服从指数分布，其均值 E[T_i] = 1 / λ_i，其中 λ_i = r_i * (5000万/天) / N_total，r_i 为对象 i 的相对热度。

## Evidence

先验知识/题面给定，逻辑校验通过：在泊松过程假设下，请求间隔服从指数分布，均值与速率成反比，公式推导自洽。
