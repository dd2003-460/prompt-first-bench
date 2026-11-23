# N148: 混合策略中本地命中流量比例 θ 的确定公式：θ = η_coverage * H_cache_local，其中 η_coverage ≈ 0.80（10个POP

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N41

## Claim

混合策略中本地命中流量比例 θ 的确定公式：θ = η_coverage * H_cache_local，其中 η_coverage ≈ 0.80（10个POP覆盖80%流量，见N38），H_cache_local ≈ 0.90（本地缓存命中率），故 θ ≈ 0.72，剩余 28% 流量走公有云长尾

## Corrected Claim

混合策略中本地命中流量比例 θ 的确定公式：θ = η_coverage * H_cache_local，其中 η_coverage ≈ 0.80（10个POP覆盖80%流量，见N38），H_cache_local ≈ 0.90（本地缓存命中率），故 θ ≈ 0.72，剩余 28% 流量走公有云长尾

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN cache hit rate local edge node coverage ratio calculation
