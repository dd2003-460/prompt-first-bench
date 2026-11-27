# N78: T_avg_resident 的解析近似表达式：T_avg_resident ≈ N_cap / (λ_total * P_resident)，其中 λ_tot

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N22, N23

## Claim

T_avg_resident 的解析近似表达式：T_avg_resident ≈ N_cap / (λ_total * P_resident)，其中 λ_total 是全局总请求率（50,000,000 次/天），P_resident 是对象在缓存中存活的概率（由热度分布决定）。

## Corrected Claim

T_avg_resident 的解析近似表达式：T_avg_resident ≈ N_cap / (λ_total * P_resident)，其中 λ_total 是全局总请求率（50,000,000 次/天），P_resident 是对象在缓存中存活的概率（由热度分布决定）。

## Evidence

先验知识/题面给定，逻辑校验通过
