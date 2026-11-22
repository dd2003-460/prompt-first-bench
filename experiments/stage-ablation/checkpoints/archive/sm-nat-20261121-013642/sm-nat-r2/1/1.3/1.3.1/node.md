# N36: Copula 参数 θ 的数值求解：通过离散化后的 Pearson 相关系数约束 ρ = -0.3，反解 Gaussian Copula 的相关系数参数 ρ_c

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

Copula 参数 θ 的数值求解：通过离散化后的 Pearson 相关系数约束 ρ = -0.3，反解 Gaussian Copula 的相关系数参数 ρ_copula，需满足 ρ = (1/π) * arcsin(ρ_copula) 或数值积分求解，得到具体的 θ 值用于联合分布采样。

## Corrected Claim

Copula 参数 θ 的数值求解：通过离散化后的 Pearson 相关系数约束 ρ = -0.3，反解 Gaussian Copula 的相关系数参数 ρ_copula，需满足 ρ = (1/π) * arcsin(ρ_copula) 或数值积分求解，得到具体的 θ 值用于联合分布采样。

## Evidence

先验知识/题面给定，逻辑校验通过：Gaussian Copula 的 Pearson 相关系数与参数 ρ_copula 的关系确实由公式 ρ = (1/π) * arcsin(ρ_copula) 定义（即 ρ_copula = sin(πρ/2)），该数学关系是 Copula 理论中的标准结论，逻辑自洽且数值量级合理。
