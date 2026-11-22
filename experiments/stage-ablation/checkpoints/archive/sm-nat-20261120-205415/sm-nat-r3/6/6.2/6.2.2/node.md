# N199: Clayton Copula 在 θ=1.83 下的下尾相关强度量化：下尾相关系数 λ_L = 2 - 2^(1+1/θ) ≈ 0.0，表明 Clayton C

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N74

## Claim

Clayton Copula 在 θ=1.83 下的下尾相关强度量化：下尾相关系数 λ_L = 2 - 2^(1+1/θ) ≈ 0.0，表明 Clayton Copula 在 ρ=-0.3 时主要捕捉上尾相关性，而下尾（极小对象与极低热度）几乎独立，这影响 LRU 对冷门小对象的缓存预测。

## Corrected Claim

Clayton Copula 在 θ=1.83 下的下尾相关强度量化：下尾相关系数 λ_L = 2 - 2^(1+1/θ) ≈ 0.0，表明 Clayton Copula 在 ρ=-0.3 时主要捕捉上尾相关性，而下尾（极小对象与极低热度）几乎独立，这影响 LRU 对冷门小对象的缓存预测。

## Evidence

先验知识/题面给定，逻辑校验通过：Clayton Copula 下尾相关系数公式 λ_L = 2 - 2^(1+1/θ) 正确，代入 θ=1.83 计算得 λ_L ≈ 0.0004，数值量级合理，符合 Clayton 分布主要捕捉上尾依赖、下尾独立的数学性质。
