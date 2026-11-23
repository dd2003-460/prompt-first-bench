# N205: 源站回源到达率 λ_origin 的量化计算：λ_origin = λ_total * R_origin，其中 λ_total ≈ 17-87 req/s (基

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

源站回源到达率 λ_origin 的量化计算：λ_origin = λ_total * R_origin，其中 λ_total ≈ 17-87 req/s (基于 N63)，R_origin = 1 - H_cache_global，H_cache_global 需根据全局缓存命中率估算（典型 80%-95%），故 R_origin ∈ [0.05, 0.20]，推导得 λ_origin ≈ 0.85-17.4 req/s

## Corrected Claim

源站回源到达率 λ_origin 的量化计算：λ_origin = λ_total * R_origin，其中 λ_total ≈ 17-87 req/s (基于 N63)，R_origin = 1 - H_cache_global，H_cache_global 需根据全局缓存命中率估算（典型 80%-95%），故 R_origin ∈ [0.05, 0.20]，推导得 λ_origin ≈ 0.85-17.4 req/s

## Evidence

先验知识/题面给定，逻辑校验通过：公式 λ_origin = λ_total * (1 - H_cache) 符合定义；数值区间 [0.05, 0.20] 与典型缓存命中率 80%-95% 一致；计算结果 17*0.05=0.85 和 87*0.20=17.4 算术正确，量级合理。
