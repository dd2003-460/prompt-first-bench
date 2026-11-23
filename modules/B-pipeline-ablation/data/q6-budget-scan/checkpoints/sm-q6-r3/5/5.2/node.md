# N23: 缓存失效策略：TTL (Time-To-Live) 设置影响命中率与新鲜度；典型 TTL 为 1-24 小时，需平衡存储成本与回源率

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

缓存失效策略：TTL (Time-To-Live) 设置影响命中率与新鲜度；典型 TTL 为 1-24 小时，需平衡存储成本与回源率

## Corrected Claim

缓存失效策略：TTL (Time-To-Live) 设置影响命中率与新鲜度；典型 TTL 为 1-24 小时，需平衡存储成本与回源率

## Evidence

父节点级核验未通过：不完备（子节点分别量化了命中率、存储成本和回源率，三者目标不同，正交性良好且无冗余。但父节点明确提到需平衡'新鲜度'（Freshness/Staleness），而子节点仅覆盖了命中率（Hit Rate）、存储成本（Storage Cost）和回源率（Origin Hit Rate/Cache Miss Rate），遗漏了'新鲜度'这一关键维度。在缓存失效策略中，新鲜度通常通过平均滞后时间（Average Staleness）或最大滞后时间来衡量，是独立于命中率的重要指标。）

## Search Query

CDN cache TTL best practices image video platform
