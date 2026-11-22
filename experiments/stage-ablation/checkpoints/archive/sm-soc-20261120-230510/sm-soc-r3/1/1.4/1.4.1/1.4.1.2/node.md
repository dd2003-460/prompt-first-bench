# N137: 截断正态分布条件均值公式：E[Z|Z∈[θ,k]] = (φ(θ) - φ(k)) / (Φ(k) - Φ(θ))，其中 φ 为标准正态密度函数，Φ 为累积分布

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N41

## Claim

截断正态分布条件均值公式：E[Z|Z∈[θ,k]] = (φ(θ) - φ(k)) / (Φ(k) - Φ(θ))，其中 φ 为标准正态密度函数，Φ 为累积分布函数，该值直接决定 μ_U_resid 的数值大小。

## Corrected Claim

截断正态分布条件均值公式：E[Z|Z∈[θ,k]] = (φ(θ) - φ(k)) / (Φ(k) - Φ(θ))，其中 φ 为标准正态密度函数，Φ 为累积分布函数，该值直接决定 μ_U_resid 的数值大小。

## Evidence

先验知识/题面给定，逻辑校验通过
