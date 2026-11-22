# N122: Clayton Copula 参数 θ 的可行域为 θ > 0，其对应的 Pearson 相关系数 ρ 的理论取值范围为 [0, 1)，因此无法通过反解公式 ρ

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

Clayton Copula 参数 θ 的可行域为 θ > 0，其对应的 Pearson 相关系数 ρ 的理论取值范围为 [0, 1)，因此无法通过反解公式 ρ = θ / (2θ + 1) 得到负值，直接证实了无法用标准 Clayton Copula 建模 ρ ≈ -0.3 的负相关结构。

## Corrected Claim

Clayton Copula 参数 θ 的可行域为 θ > 0，其对应的 Pearson 相关系数 ρ 的理论取值范围为 [0, 1)，因此无法通过反解公式 ρ = θ / (2θ + 1) 得到负值，直接证实了无法用标准 Clayton Copula 建模 ρ ≈ -0.3 的负相关结构。

## Evidence

先验知识/题面给定，逻辑校验通过：Clayton Copula 定义域 θ>0 且单调递增，ρ 范围 [0,1) 符合数学推导，无法表示负相关。
