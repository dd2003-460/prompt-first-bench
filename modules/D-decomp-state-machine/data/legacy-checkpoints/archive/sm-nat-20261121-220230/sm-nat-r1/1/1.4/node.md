# N9: 请求热度分布λ_i服从Pareto(β=0.9)，归一化后总请求率R_total = 50,000,000/天，单个对象请求率λ_i = R_total * (

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1

## Claim

请求热度分布λ_i服从Pareto(β=0.9)，归一化后总请求率R_total = 50,000,000/天，单个对象请求率λ_i = R_total * (i^{-β} - (N+1)^{-β}) / (1 - (N+1)^{1-β})，N=100,000。

## Corrected Claim

请求热度分布λ_i服从Pareto(β=0.9)，归一化后总请求率R_total = 50,000,000/天，单个对象请求率λ_i = R_total * (i^{-β} - (N+1)^{-β}) / (1 - (N+1)^{1-β})，N=100,000。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布归一化公式推导正确，量纲与数值量级合理
