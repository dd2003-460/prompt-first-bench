# N615: 缓存命中率提升对 P99 延迟的贡献：ΔL_cache = L_backhaul * ΔH，其中 L_backhaul ≈ 50-200 ms（引用 N51），

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N202

## Claim

缓存命中率提升对 P99 延迟的贡献：ΔL_cache = L_backhaul * ΔH，其中 L_backhaul ≈ 50-200 ms（引用 N51），ΔH 为新增 POP 带来的缓存命中率增量，若 ΔH ≈ 1-2%，则 ΔL_cache ≈ 0.5-4 ms，结合传播延迟降低 0.19 ms，总 ΔL_per_pop ≈ 0.7-4.2 ms，仍低于 N202 声称的 8-12 ms

## Corrected Claim

缓存命中率提升对 P99 延迟的贡献：ΔL_cache = L_backhaul * ΔH，其中 L_backhaul ≈ 50-200 ms（引用 N51），ΔH 为新增 POP 带来的缓存命中率增量，若 ΔH ≈ 1-2%，则 ΔL_cache ≈ 0.5-4 ms，结合传播延迟降低 0.19 ms，总 ΔL_per_pop ≈ 0.7-4.2 ms，仍低于 N202 声称的 8-12 ms

## Evidence

先验知识/题面给定，逻辑校验通过：公式 ΔL = L_backhaul * ΔH 量纲正确，数值代入（50-200ms * 1-2% = 0.5-4ms）计算无误，且结论（总延迟降低 < 8-12ms）与前提条件逻辑自洽。

## Search Query

CDN cache hit rate backhaul latency P99 improvement
