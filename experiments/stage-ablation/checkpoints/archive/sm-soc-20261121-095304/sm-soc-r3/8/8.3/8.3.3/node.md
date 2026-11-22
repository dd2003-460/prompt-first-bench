# N191: 算法惩罚强度 k_penalty 的反推公式：通过 Bias = |f(ΔP) * λ_base * (1 - k_penalty) - Observed_ΔC

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N68

## Claim

算法惩罚强度 k_penalty 的反推公式：通过 Bias = |f(ΔP) * λ_base * (1 - k_penalty) - Observed_ΔConsult| = 0 反解 k_penalty。若 Observed_ΔConsult ≈ 0 且 f(ΔP)*λ_base > 0，则 k_penalty ≈ 1，表明算法完全抑制了降价带来的流量增量。

## Corrected Claim

算法惩罚强度 k_penalty 的反推公式：通过 Bias = |f(ΔP) * λ_base * (1 - k_penalty) - Observed_ΔConsult| = 0 反解 k_penalty。若 Observed_ΔConsult ≈ 0 且 f(ΔP)*λ_base > 0，则 k_penalty ≈ 1，表明算法完全抑制了降价带来的流量增量。

## Evidence

先验知识/题面给定，逻辑校验通过：方程 Bias = 0 意味着 f(ΔP)*λ_base*(1-k_penalty) = Observed_ΔConsult。若 Observed_ΔConsult ≈ 0 且 f(ΔP)*λ_base > 0，则 (1-k_penalty) 必须趋近于 0，即 k_penalty ≈ 1。推导在数学上自洽，且符合‘完全抑制’的语义解释。

## Search Query

algorithm penalty coefficient estimation from counterfactual data
