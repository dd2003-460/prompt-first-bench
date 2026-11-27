# N24: k值求解方程：128GB = Σ_{i=1}^{k} s_i，其中s_i = S_max * i^{-1.1} * exp(-0.3 * z_i)，z_i为对象

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

k值求解方程：128GB = Σ_{i=1}^{k} s_i，其中s_i = S_max * i^{-1.1} * exp(-0.3 * z_i)，z_i为对象i在热度排序中的标准化残差，需数值求解k ≈ 500-2000（基于Pareto头部集中性估算）

## Corrected Claim

k值求解方程：128GB = Σ_{i=1}^{k} s_i，其中s_i = S_max * i^{-1.1} * exp(-0.3 * z_i)，z_i为对象i在热度排序中的标准化残差，需数值求解k ≈ 500-2000（基于Pareto头部集中性估算）

## Evidence

先验知识/题面给定，逻辑校验通过
