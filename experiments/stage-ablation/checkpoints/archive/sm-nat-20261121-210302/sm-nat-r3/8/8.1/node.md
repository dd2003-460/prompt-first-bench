# N78: T_avg_resident 的解析近似表达式：T_avg_resident ≈ N_cap / (λ_total * P_resident)，其中 λ_tot

- **status**: pending
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

父节点级核验未通过：不完备, 有冗余（子节点并非对公式的独立分解，而是同一公式的两个具体数值实例（不同参数取值），存在高度冗余；且仅通过两个点无法完备覆盖公式中变量（N_cap, P_resident, λ_total）的解析关系、边界条件或敏感性分析等关键方面。）
