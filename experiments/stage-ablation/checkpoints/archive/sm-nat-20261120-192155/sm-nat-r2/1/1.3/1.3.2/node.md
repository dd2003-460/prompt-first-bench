# N28: 相关性量化：ρ=-0.3在Pareto分布下的实现方式，通过Copula函数或线性混合模型 s_i = S_max * i^{-1.1} * (1 - 0.3 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

相关性量化：ρ=-0.3在Pareto分布下的实现方式，通过Copula函数或线性混合模型 s_i = S_max * i^{-1.1} * (1 - 0.3 * (r_i - E[r_i]) / σ_r) 实现，需验证该模型是否保持Pareto尾部特性

## Corrected Claim

相关性量化：ρ=-0.3在Pareto分布下的实现方式，通过Copula函数或线性混合模型 s_i = S_max * i^{-1.1} * (1 - 0.3 * (r_i - E[r_i]) / σ_r) 实现，需验证该模型是否保持Pareto尾部特性

## Evidence

先验知识/题面给定，逻辑校验通过
