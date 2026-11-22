# N274: 基于 T_res(s) 的大小依赖性，更新惩罚因子 f_update 的大小加权修正公式为 f_update = (1/V_total) * ∫_{s_min}

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94

## Claim

基于 T_res(s) 的大小依赖性，更新惩罚因子 f_update 的大小加权修正公式为 f_update = (1/V_total) * ∫_{s_min}^{s_max} exp(-λ_u * T_res(s)) * s * p(s) ds，其中 p(s) 为 Pareto(α=1.1) 密度函数，λ_u=0.01/day。

## Corrected Claim

基于 T_res(s) 的大小依赖性，更新惩罚因子 f_update 的大小加权修正公式为 f_update = (1/V_total) * ∫_{s_min}^{s_max} exp(-λ_u * T_res(s)) * s * p(s) ds，其中 p(s) 为 Pareto(α=1.1) 密度函数，λ_u=0.01/day。

## Evidence

先验知识/题面给定，逻辑校验通过
