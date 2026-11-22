# N246: 置信度阈值 C3 > 0.7 的敏感性分析：需计算 C3 对 ΔEquilibrium 分布参数（μ_Δ, σ_Δ）和流失率分布参数（μ_churn, σ_ch

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N88

## Claim

置信度阈值 C3 > 0.7 的敏感性分析：需计算 C3 对 ΔEquilibrium 分布参数（μ_Δ, σ_Δ）和流失率分布参数（μ_churn, σ_churn）的偏导数 ∂C3/∂θ，若任一参数的 95% 置信区间导致 C3 跨越 0.7 阈值，则该断言的稳健性置信度降级，需标注为 [待核验] 并给出临界参数值。

## Corrected Claim

置信度阈值 C3 > 0.7 的敏感性分析：需计算 C3 对 ΔEquilibrium 分布参数（μ_Δ, σ_Δ）和流失率分布参数（μ_churn, σ_churn）的偏导数 ∂C3/∂θ，若任一参数的 95% 置信区间导致 C3 跨越 0.7 阈值，则该断言的稳健性置信度降级，需标注为 [待核验] 并给出临界参数值。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

sensitivity analysis of confidence threshold for intervention strategy
