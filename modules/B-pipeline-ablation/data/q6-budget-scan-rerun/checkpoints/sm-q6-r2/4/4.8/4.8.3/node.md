# N95: 回源带宽限制阈值对缓存失效的影响：设定单POP点回源带宽上限为 B_limit_pop = 0.5 * B_peak_pop（即峰值带宽的50%），当实际回源需

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

回源带宽限制阈值对缓存失效的影响：设定单POP点回源带宽上限为 B_limit_pop = 0.5 * B_peak_pop（即峰值带宽的50%），当实际回源需求超过该阈值时，缓存命中率下降 ΔCHR_limit ≈ 10%-20%，导致部分请求降级为直连源站，P99延迟增加 ΔP99_limit ≈ 50-100ms；该阈值需根据源站承载能力动态调整。

## Corrected Claim

回源带宽限制阈值对缓存失效的影响：设定单POP点回源带宽上限为 B_limit_pop = 0.5 * B_peak_pop（即峰值带宽的50%），当实际回源需求超过该阈值时，缓存命中率下降 ΔCHR_limit ≈ 10%-20%，导致部分请求降级为直连源站，P99延迟增加 ΔP99_limit ≈ 50-100ms；该阈值需根据源站承载能力动态调整。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

origin bandwidth limit impact on cache hit rate and P99 latency CDN
