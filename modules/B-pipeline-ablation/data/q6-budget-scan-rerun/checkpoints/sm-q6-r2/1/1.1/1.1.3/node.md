# N45: P99 延迟与 P95/P50 的统计关系：在重尾分布 (Heavy-tail) 下，P99 通常比 P95 高 20%-50%，比 P50 高 50%-100

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

P99 延迟与 P95/P50 的统计关系：在重尾分布 (Heavy-tail) 下，P99 通常比 P95 高 20%-50%，比 P50 高 50%-100%；对于 CDN 延迟，P99 主要由回源请求 (Miss) 和长尾网络路径 (Bad Route) 主导，因此 P99 对缓存命中率 (CHR) 和路由优化敏感度远高于 P50

## Corrected Claim

P99 延迟与 P95/P50 的统计关系：在重尾分布 (Heavy-tail) 下，P99 通常比 P95 高 20%-50%，比 P50 高 50%-100%；对于 CDN 延迟，P99 主要由回源请求 (Miss) 和长尾网络路径 (Bad Route) 主导，因此 P99 对缓存命中率 (CHR) 和路由优化敏感度远高于 P50

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN latency P99 vs P95 vs P50 heavy tail distribution sensitivity cache miss
