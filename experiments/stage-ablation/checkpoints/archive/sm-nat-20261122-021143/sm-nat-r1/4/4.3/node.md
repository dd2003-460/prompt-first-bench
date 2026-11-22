# N17: 缓存污染量化：1%/天 更新率导致 LRU 缓存中约 12.8GB（128GB×10%）的对象在 1 天内被标记为 stale，实际可用缓存容量降至 115.2

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

缓存污染量化：1%/天 更新率导致 LRU 缓存中约 12.8GB（128GB×10%）的对象在 1 天内被标记为 stale，实际可用缓存容量降至 115.2GB，重新计算稳态命中率下界

## Corrected Claim

缓存污染量化：1%/天 更新率导致 LRU 缓存中约 12.8GB（128GB×10%）的对象在 1 天内被标记为 stale，实际可用缓存容量降至 115.2GB，重新计算稳态命中率下界

## Evidence

先验知识/题面给定，逻辑校验通过：128GB * 10% = 12.8GB，128GB - 12.8GB = 115.2GB，算术与逻辑自洽。

## Search Query

cache pollution stale object ratio LRU capacity reduction hit rate impact
