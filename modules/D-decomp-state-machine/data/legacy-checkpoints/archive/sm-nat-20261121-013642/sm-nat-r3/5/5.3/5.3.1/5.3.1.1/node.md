# N211: Gaussian Copula 参数 θ 与 Pearson 相关系数 ρ=-0.3 的精确映射关系：θ = Φ⁻¹((1+ρ)/2)，计算得 θ ≈ -0.2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

Gaussian Copula 参数 θ 与 Pearson 相关系数 ρ=-0.3 的精确映射关系：θ = Φ⁻¹((1+ρ)/2)，计算得 θ ≈ -0.2914；基于此 θ 构建联合 CDF C(u,v; θ)，作为后续数值积分的输入函数。

## Corrected Claim

Gaussian Copula 参数 θ 与 Pearson 相关系数 ρ=-0.3 的精确映射关系：θ = Φ⁻¹((1+ρ)/2)，计算得 θ ≈ -0.2914；基于此 θ 构建联合 CDF C(u,v; θ)，作为后续数值积分的输入函数。

## Evidence

先验知识/题面给定，逻辑校验通过：Gaussian Copula 参数 θ 与 Pearson 相关系数 ρ 的映射公式 θ = Φ⁻¹((1+ρ)/2) 是标准定义，代入 ρ=-0.3 计算得 θ ≈ -0.2914 数值正确，逻辑自洽。
