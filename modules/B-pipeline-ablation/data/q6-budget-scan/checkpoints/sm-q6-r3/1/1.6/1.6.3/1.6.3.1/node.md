# N158: 缓存命中率 hit_rate 的具体数值取决于工作集大小与缓存容量，对于日均 2TB 下载量，若热点对象占比 80%，hit_rate ≈ 70-85%；若热点

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

缓存命中率 hit_rate 的具体数值取决于工作集大小与缓存容量，对于日均 2TB 下载量，若热点对象占比 80%，hit_rate ≈ 70-85%；若热点对象占比 90%，hit_rate ≈ 85-95%；需根据实际对象访问分布确定。

## Corrected Claim

缓存命中率 hit_rate 的具体数值取决于工作集大小与缓存容量，对于日均 2TB 下载量，若热点对象占比 80%，hit_rate ≈ 70-85%；若热点对象占比 90%，hit_rate ≈ 85-95%；需根据实际对象访问分布确定。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN cache hit rate working set size
