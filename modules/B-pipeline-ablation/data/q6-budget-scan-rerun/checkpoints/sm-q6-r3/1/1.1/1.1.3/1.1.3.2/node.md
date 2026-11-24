# N151: 缓存命中率 (CHR) 对 P99 延迟的边际敏感度：每降低 1% CHR，回源请求占比增加 1%，P99 延迟增加 ΔP99_miss = (1/CHR) ×

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

缓存命中率 (CHR) 对 P99 延迟的边际敏感度：每降低 1% CHR，回源请求占比增加 1%，P99 延迟增加 ΔP99_miss = (1/CHR) × (RTT_origin - RTT_edge) × P_miss_weight，其中 P_miss_weight 为 P99 分位中由 Miss 主导的概率质量（典型值 0.3-0.5）

## Corrected Claim

缓存命中率 (CHR) 对 P99 延迟的边际敏感度：每降低 1% CHR，回源请求占比增加 1%，P99 延迟增加 ΔP99_miss = (1/CHR) × (RTT_origin - RTT_edge) × P_miss_weight，其中 P_miss_weight 为 P99 分位中由 Miss 主导的概率质量（典型值 0.3-0.5）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cache hit ratio impact on P99 latency origin server RTT
