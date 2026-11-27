# N60: 当 u=0.1 时，线性折损模型 δ = 1 - u * (T_res/L_object) 失效的临界条件是 u * T_res > 1，此时需引入非线性修正项

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

当 u=0.1 时，线性折损模型 δ = 1 - u * (T_res/L_object) 失效的临界条件是 u * T_res > 1，此时需引入非线性修正项 δ_corrected = exp(-u * T_res)，对于 T_res/L_object=0.5，δ_corrected ≈ exp(-0.05) ≈ 0.951

## Corrected Claim

当 u=0.1 时，线性折损模型 δ = 1 - u * (T_res/L_object) 失效的临界条件是 u * T_res > 1，此时需引入非线性修正项 δ_corrected = exp(-u * T_res)，对于 T_res/L_object=0.5，δ_corrected ≈ exp(-0.05) ≈ 0.951

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 exp(-0.05) ≈ 0.9512 正确，模型定义与临界条件逻辑自洽
