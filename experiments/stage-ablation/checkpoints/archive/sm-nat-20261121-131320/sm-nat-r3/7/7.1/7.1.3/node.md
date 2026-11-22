# N134: Pareto(β=0.9) 热度分布的逆 CDF 函数 F^{-1}(q)：F^{-1}(q) = f_min * (1-q)^(-1/β) = f_min *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

Pareto(β=0.9) 热度分布的逆 CDF 函数 F^{-1}(q)：F^{-1}(q) = f_min * (1-q)^(-1/β) = f_min * (1-q)^(-1/0.9)，用于将 Copula 输入 v ∈ [0,1] 映射回实际对象热度 f

## Corrected Claim

Pareto(β=0.9) 热度分布的逆 CDF 函数 F^{-1}(q)：F^{-1}(q) = f_min * (1-q)^(-1/β) = f_min * (1-q)^(-1/0.9)，用于将 Copula 输入 v ∈ [0,1] 映射回实际对象热度 f

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布的逆CDF公式推导正确，量纲与映射逻辑自洽
