# N242: 字节命中率分母 D_byte 的解析近似：在 Gaussian Copula 下，D_byte = N * E[R*S] = N * (E[R]*E[S] + 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N87, N88, N89

## Claim

字节命中率分母 D_byte 的解析近似：在 Gaussian Copula 下，D_byte = N * E[R*S] = N * (E[R]*E[S] + ρ * σ_R * σ_S)。其中 E[R] = 5×10^7/100,000 = 500 req/day/obj，E[S] 为截断均值，σ_R 和 σ_S 为 Pareto 分布的标准差。

## Corrected Claim

字节命中率分母 D_byte 的解析近似：在 Gaussian Copula 下，D_byte = N * E[R*S] = N * (E[R]*E[S] + ρ * σ_R * σ_S)。其中 E[R] = 5×10^7/100,000 = 500 req/day/obj，E[S] 为截断均值，σ_R 和 σ_S 为 Pareto 分布的标准差。

## Evidence

先验知识/题面给定，逻辑校验通过：Gaussian Copula 下联合期望公式 E[RS] = E[R]E[S] + ρσ_Rσ_S 符合统计学定义，数值量级合理。
