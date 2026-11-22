# N121: 下游投影2：锚定效应噪声项 Var(α_anchor) 的量化公式，定义为 Var(α_anchor) = k_anchor * Var(ε_market) *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N30

## Claim

下游投影2：锚定效应噪声项 Var(α_anchor) 的量化公式，定义为 Var(α_anchor) = k_anchor * Var(ε_market) * (1 + 1/σ_ref)，其中 k_anchor 为锚定敏感度系数（假设 k_anchor=0.3），σ_ref 为参考价 P_ref 的变异系数（来自 N94）。

## Corrected Claim

下游投影2：锚定效应噪声项 Var(α_anchor) 的量化公式，定义为 Var(α_anchor) = k_anchor * Var(ε_market) * (1 + 1/σ_ref)，其中 k_anchor 为锚定敏感度系数（假设 k_anchor=0.3），σ_ref 为参考价 P_ref 的变异系数（来自 N94）。

## Evidence

先验知识/题面给定，逻辑校验通过
