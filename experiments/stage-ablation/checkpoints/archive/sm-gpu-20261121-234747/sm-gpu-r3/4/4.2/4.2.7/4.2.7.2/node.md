# N313: 解析法方差合成公式：TCO = P + E + M，假设P, E, M相互独立，则Var(TCO) = Var(P) + Var(E) + Var(M)；标准差

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N111

## Claim

解析法方差合成公式：TCO = P + E + M，假设P, E, M相互独立，则Var(TCO) = Var(P) + Var(E) + Var(M)；标准差σ_TCO = sqrt(σ_P^2 + σ_E^2 + σ_M^2)；对于4090方案，σ_P=$150, σ_E=$4.9, σ_M=$209，则σ_TCO ≈ sqrt(150^2 + 4.9^2 + 209^2) ≈ $256

## Corrected Claim

解析法方差合成公式：TCO = P + E + M，假设P, E, M相互独立，则Var(TCO) = Var(P) + Var(E) + Var(M)；标准差σ_TCO = sqrt(σ_P^2 + σ_E^2 + σ_M^2)；对于4090方案，σ_P=$150, σ_E=$4.9, σ_M=$209，则σ_TCO ≈ sqrt(150^2 + 4.9^2 + 209^2) ≈ $256

## Evidence

先验知识/题面给定，逻辑校验通过：方差合成公式在独立假设下成立，数值计算 sqrt(150^2 + 4.9^2 + 209^2) ≈ 256.03 准确无误。

## Search Query

analytical variance propagation TCO independent variables
