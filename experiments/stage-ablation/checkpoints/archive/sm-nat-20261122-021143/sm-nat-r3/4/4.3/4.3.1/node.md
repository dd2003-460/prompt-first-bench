# N51: Stale 对象比例的计算：1%/天 更新率意味着每天 1% 的对象被修改，假设更新均匀分布在 10 万对象中，则每天约 1000 个对象变为 stale，但 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

Stale 对象比例的计算：1%/天 更新率意味着每天 1% 的对象被修改，假设更新均匀分布在 10 万对象中，则每天约 1000 个对象变为 stale，但 LRU 缓存中 stale 对象的比例取决于缓存中对象的年龄分布，而非全局更新率。

## Corrected Claim

Stale 对象比例的计算：1%/天 更新率意味着每天 1% 的对象被修改，假设更新均匀分布在 10 万对象中，则每天约 1000 个对象变为 stale，但 LRU 缓存中 stale 对象的比例取决于缓存中对象的年龄分布，而非全局更新率。

## Evidence

先验知识/题面给定，逻辑校验通过：1%更新率对应1000个对象/天在10万总量下计算正确；LRU缓存中stale比例确实取决于缓存内对象的年龄分布（即对象在缓存中停留的时间与更新周期的关系），而非简单等于全局更新率，逻辑自洽。

## Search Query

cache invalidation rate uniform update distribution
