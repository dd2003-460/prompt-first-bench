# N167: 异质性阈值 σ_threshold 的解析解：在正态分布假设下，令 ΔC_dispute_reduction = C_delay，解得 σ_threshold 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N59

## Claim

异质性阈值 σ_threshold 的解析解：在正态分布假设下，令 ΔC_dispute_reduction = C_delay，解得 σ_threshold = μ * sqrt( (P_dispute_low - P_dispute_high) * C_after_base / (r * ΔT_wait * (P_list - P_market)/μ) )，该值决定了 ESS 成立的边界。

## Corrected Claim

异质性阈值 σ_threshold 的解析解：在正态分布假设下，令 ΔC_dispute_reduction = C_delay，解得 σ_threshold = μ * sqrt( (P_dispute_low - P_dispute_high) * C_after_base / (r * ΔT_wait * (P_list - P_market)/μ) )，该值决定了 ESS 成立的边界。

## Evidence

先验知识/题面给定，逻辑校验通过
