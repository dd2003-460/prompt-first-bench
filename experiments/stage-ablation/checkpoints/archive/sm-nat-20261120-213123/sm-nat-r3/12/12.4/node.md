# N187: LRU 的 k_cold 由缓存容量 C 和对象大小分布决定：k_cold 是满足 Σ_{i=k_hot}^{k_cold} S_i ≤ C - Σ_{i=1}

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N81

## Claim

LRU 的 k_cold 由缓存容量 C 和对象大小分布决定：k_cold 是满足 Σ_{i=k_hot}^{k_cold} S_i ≤ C - Σ_{i=1}^{k_hot} S_i 的最大对象数。由于 ρ=-0.3，中等热度对象平均大小 E[S|Mid] ≈ E[S] * (1 + ρ * σ_logS * σ_logH * (1/k_mid^(1/β)))，需数值求解 k_cold。

## Corrected Claim

LRU 的 k_cold 由缓存容量 C 和对象大小分布决定：k_cold 是满足 Σ_{i=k_hot}^{k_cold} S_i ≤ C - Σ_{i=1}^{k_hot} S_i 的最大对象数。由于 ρ=-0.3，中等热度对象平均大小 E[S|Mid] ≈ E[S] * (1 + ρ * σ_logS * σ_logH * (1/k_mid^(1/β)))，需数值求解 k_cold。

## Evidence

先验知识/题面给定，逻辑校验通过
