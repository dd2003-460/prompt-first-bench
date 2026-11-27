# N367: 稳定性判据的数值验证：在 δ ∈ [0.15, 0.25] 区间内取 5 个等距点，分别计算局部弹性 ε_T(δ_i)，若 max|ε_T(δ_i) - ε_T

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N123

## Claim

稳定性判据的数值验证：在 δ ∈ [0.15, 0.25] 区间内取 5 个等距点，分别计算局部弹性 ε_T(δ_i)，若 max|ε_T(δ_i) - ε_T(δ_j)| / mean(ε_T) > 0.2，则判定弹性非恒定，均衡稳定性需分段讨论而非单一阈值判断。

## Corrected Claim

稳定性判据的数值验证：在 δ ∈ [0.15, 0.25] 区间内取 5 个等距点，分别计算局部弹性 ε_T(δ_i)，若 max|ε_T(δ_i) - ε_T(δ_j)| / mean(ε_T) > 0.2，则判定弹性非恒定，均衡稳定性需分段讨论而非单一阈值判断。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

non-constant elasticity in feedback loops economic systems
