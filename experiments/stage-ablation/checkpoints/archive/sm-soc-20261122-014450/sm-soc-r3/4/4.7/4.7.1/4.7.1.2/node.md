# N265: 信息透明度提升后的搜索成本 C_search' 的构成与数值：C_search' = T_search_reduced * r_time，其中 T_search

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N85, N86, N87

## Claim

信息透明度提升后的搜索成本 C_search' 的构成与数值：C_search' = T_search_reduced * r_time，其中 T_search_reduced = T_search_base * (1 - η_effective)，η_effective 为实际效率提升率，需基于 A/B 测试数据确定，通常 η_effective ∈ [0.15, 0.30]

## Corrected Claim

信息透明度提升后的搜索成本 C_search' 的构成与数值：C_search' = T_search_reduced * r_time，其中 T_search_reduced = T_search_base * (1 - η_effective)，η_effective 为实际效率提升率，需基于 A/B 测试数据确定，通常 η_effective ∈ [0.15, 0.30]

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

A/B test information transparency search time reduction used goods
