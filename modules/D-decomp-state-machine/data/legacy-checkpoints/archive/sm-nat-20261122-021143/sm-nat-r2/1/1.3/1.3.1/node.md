# N22: 对象大小与请求热度的联合分布参数化：假设 log S 和 log R 服从二元正态分布，协方差矩阵由 ρ=-0.3 确定，具体为 Cov(log S, log 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

对象大小与请求热度的联合分布参数化：假设 log S 和 log R 服从二元正态分布，协方差矩阵由 ρ=-0.3 确定，具体为 Cov(log S, log R) = -0.3 * σ_logS * σ_logR，其中 σ_logS 和 σ_logR 分别由 Pareto 参数 α=1.1 和 β=0.9 决定

## Corrected Claim

对象大小与请求热度的联合分布参数化：假设 log S 和 log R 服从二元正态分布，协方差矩阵由 ρ=-0.3 确定，具体为 Cov(log S, log R) = -0.3 * σ_logS * σ_logR，其中 σ_logS 和 σ_logR 分别由 Pareto 参数 α=1.1 和 β=0.9 决定

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布的对数形式服从指数分布，其标准差与形状参数成反比（σ=1/α），因此σ_logS和σ_logR由α和β决定在数学上成立；二元正态分布的协方差定义与给定公式一致，量纲和逻辑自洽。
