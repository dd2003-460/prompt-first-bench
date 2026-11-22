# N32: 条件期望修正系数：E[R_i | s_i < s_median] / E[R_i | s_i < s_median]_independent = 1 + ρ *

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

条件期望修正系数：E[R_i | s_i < s_median] / E[R_i | s_i < s_median]_independent = 1 + ρ * (Z_h_mean - Z_h_median) * σ_h / σ_R。由于 ρ=-0.3，小对象的期望请求率比独立假设下高约 15-20%，具体系数需通过积分 ∫_{-∞}^{z_median} φ(z) * E[Z_h | Z_s=z] dz 计算。

## Corrected Claim

条件期望修正系数可通过积分 ∫_{-∞}^{z_median} φ(z) * E[Z_h | Z_s=z] dz 计算。在正态分布假设下，由于 ρ=-0.3，小对象（s_i < s_median）的期望请求率通常比独立假设下高，具体增幅取决于分布参数，经验上可能在 10-20% 范围内，但需通过具体积分计算确定。

## Evidence

[质询]公式推导存在量纲与逻辑瑕疵：条件期望修正系数通常涉及标准化变量的均值偏移，公式中直接混合了原始变量标准差 σ_h 和 σ_R 以及标准化均值 Z_h_mean，且未明确 Z_h 和 Z_s 的标准化定义，导致量纲一致性存疑；此外，15-20% 的估计值依赖于具体的分布假设（如正态性）和 ρ 的具体作用机制，仅凭 ρ=-0.3 无法严格推导出该固定百分比区间，属于经验性估算而非严格数学推导。 | 先验知识/题面给定，但逻辑校验发现公式量纲及推导过程存在不严谨之处，且具体数值区间缺乏严格数学支撑，故降级。
