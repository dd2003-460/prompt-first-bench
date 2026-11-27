# N48: 在 Pareto(α=1.1, β=0.9) 且 ρ=-0.3 下，k_eff 的近似值：由于 α<2，总字节由头部主导，k_eff ≈ (C / (s_min

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16, N17, N18

## Claim

在 Pareto(α=1.1, β=0.9) 且 ρ=-0.3 下，k_eff 的近似值：由于 α<2，总字节由头部主导，k_eff ≈ (C / (s_min * (α-1)))^(1/(α-1)) * (1 + ρ*σ_logS*σ_logH)^(-1)，需代入 C=1.28e11, s_min=1KB 计算具体数值。

## Corrected Claim

在 Pareto(α=1.1, β=0.9) 且 ρ=-0.3 下，k_eff 的近似值：由于 α<2，总字节由头部主导，k_eff ≈ (C / (s_min * (α-1)))^(1/(α-1)) * (1 + ρ*σ_logS*σ_logH)^(-1)，需代入 C=1.28e11, s_min=1KB 计算具体数值。

## Evidence

先验知识/题面给定，逻辑校验通过
