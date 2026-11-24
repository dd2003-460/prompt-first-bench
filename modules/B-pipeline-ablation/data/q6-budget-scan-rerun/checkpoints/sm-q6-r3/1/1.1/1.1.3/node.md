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

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于分布形态（重尾特性）对分位数比率的数学量化，子节点2和3分别聚焦于两个具体的业务/物理驱动因素（缓存命中率、网络路由）对P99的边际影响机制。三者分别对应'统计基础'、'缓存维度'和'网络维度'，逻辑清晰且互不重叠。父节点中提到的'P99主要由...主导'这一结论已被子节点2和3通过量化公式具体拆解覆盖，子节点1覆盖了'统计关系'部分。虽然子节点2和3都是对P99增加的量化，但驱动变量不同，不构成冗余。）

## Search Query

CDN latency P99 vs P95 vs P50 heavy tail distribution sensitivity cache miss
