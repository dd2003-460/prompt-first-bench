# N47: LRU 的‘污染’损失量化为：在时间窗口 T 内，被驱逐但随后再次被访问的对象集合 E 的总请求率占比 P_pollution = (Σ_{i∈E} λ_i) 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

LRU 的‘污染’损失量化为：在时间窗口 T 内，被驱逐但随后再次被访问的对象集合 E 的总请求率占比 P_pollution = (Σ_{i∈E} λ_i) / R_total，该值越大，LFU 相比 LRU 的潜在增益越大。

## Corrected Claim

LRU 的‘污染’损失量化为：在时间窗口 T 内，被驱逐但随后再次被访问的对象集合 E 的总请求率占比 P_pollution = (Σ_{i∈E} λ_i) / R_total，该值越大，LFU 相比 LRU 的潜在增益越大。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU cache pollution rate quantification Pareto workload
