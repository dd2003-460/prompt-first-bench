# N100: ΔH_max的分子上界：在单对象交换假设下，ΔH_max的分子为r_1 s_1 - r_{k+1} s_{k+1}；由于r_i ∝ i^{-0.9}且s_i ∝

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N38

## Claim

ΔH_max的分子上界：在单对象交换假设下，ΔH_max的分子为r_1 s_1 - r_{k+1} s_{k+1}；由于r_i ∝ i^{-0.9}且s_i ∝ i^{-1.1}，r_1 s_1 = C_r C_s * 1^{-2.0} = C_r C_s，而r_{k+1} s_{k+1} = C_r C_s * (k+1)^{-2.0}，故分子 = C_r C_s * (1 - (k+1)^{-2.0})。

## Corrected Claim

ΔH_max的分子上界：在单对象交换假设下，ΔH_max的分子为r_1 s_1 - r_{k+1} s_{k+1}；由于r_i ∝ i^{-0.9}且s_i ∝ i^{-1.1}，r_1 s_1 = C_r C_s * 1^{-2.0} = C_r C_s，而r_{k+1} s_{k+1} = C_r C_s * (k+1)^{-2.0}，故分子 = C_r C_s * (1 - (k+1)^{-2.0})。

## Evidence

先验知识/题面给定，逻辑校验通过：代数推导正确，r_i s_i 的指数叠加为 -2.0，分子表达式符合定义。
