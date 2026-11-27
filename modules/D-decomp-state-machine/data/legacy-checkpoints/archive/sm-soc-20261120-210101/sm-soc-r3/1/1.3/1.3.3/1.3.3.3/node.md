# N159: 剩余搜索成本 C_search_remaining 的动态计算：基于 N39 的 k 值。C_search_remaining(t) = (C_0/k) * e

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N40

## Claim

剩余搜索成本 C_search_remaining 的动态计算：基于 N39 的 k 值。C_search_remaining(t) = (C_0/k) * e^(-kt)。在 t=0 时，C_rem(0) = C_0/k。若 C_0=100, k=0.046，则 C_rem(0) ≈ 2174元（时间价值折算）。该值作为 θ_stop 的基准项，需确认 C_0 的时间价值折算系数（如 10元/分钟）是否合理。

## Corrected Claim

剩余搜索成本 C_search_remaining 的动态计算：基于 N39 的 k 值。C_search_remaining(t) = (C_0/k) * e^(-kt)。在 t=0 时，C_rem(0) = C_0/k。若 C_0=100, k=0.046，则 C_rem(0) ≈ 2174元（时间价值折算）。该值作为 θ_stop 的基准项，需确认 C_0 的时间价值折算系数（如 10元/分钟）是否合理。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 100/0.046 ≈ 2173.9 与陈述一致，公式推导自洽。

## Search Query

consumer search cost time value monetization rate per minute
