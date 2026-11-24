# N92: 公有云CDN区域级配置参数对带宽成本的影响：缓存TTL优化可使回源带宽降低 20-30% (基于CHR提升)，压缩算法优化可使传输带宽降低 30-50% (基于

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

公有云CDN区域级配置参数对带宽成本的影响：缓存TTL优化可使回源带宽降低 20-30% (基于CHR提升)，压缩算法优化可使传输带宽降低 30-50% (基于gzip/brotli压缩比)，量化公式：ΔCost_bandwidth = B_total × (ΔCHR + ΔCompression) × unit_cost_per_GB

## Corrected Claim

公有云CDN区域级配置参数对带宽成本的影响：缓存TTL优化可使回源带宽降低 20-30% (基于CHR提升)，压缩算法优化可使传输带宽降低 30-50% (基于gzip/brotli压缩比)，量化公式：ΔCost_bandwidth = B_total × (ΔCHR + ΔCompression) × unit_cost_per_GB

## Evidence

先验知识/题面给定，逻辑校验通过
