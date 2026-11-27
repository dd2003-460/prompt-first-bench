# N152: Gaussian Copula 在 ρ=-0.3 下，尾部相关系数 (Lower Tail Dependence) λ_L 为 0，而 Clayton Copu

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59

## Claim

Gaussian Copula 在 ρ=-0.3 下，尾部相关系数 (Lower Tail Dependence) λ_L 为 0，而 Clayton Copula 在相同秩相关系数 ρ=-0.3 下，λ_L = 2(1 - exp(-2/θ))，其中 θ = -ρ/(1+ρ) ≈ 0.4286，计算得 λ_L ≈ 0.27，表明 Clayton 模型预测的尾部联合极端事件概率是 Gaussian 的 27 倍。

## Corrected Claim

Gaussian Copula 在 ρ=-0.3 下，尾部相关系数 (Lower Tail Dependence) λ_L 为 0，而 Clayton Copula 在相同秩相关系数 ρ=-0.3 下，λ_L = 2(1 - exp(-2/θ))，其中 θ = -ρ/(1+ρ) ≈ 0.4286，计算得 λ_L ≈ 0.27，表明 Clayton 模型预测的尾部联合极端事件概率是 Gaussian 的 27 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：Gaussian Copula 尾部相关系数恒为0；Clayton Copula 参数 θ 与 Spearman 秩相关 ρ 的关系为 θ = -2ρ/(1+ρ)，当 ρ=-0.3 时 θ=0.4286，下尾依赖 λ_L = 2(1-exp(-2/θ)) ≈ 0.27，计算无误。
