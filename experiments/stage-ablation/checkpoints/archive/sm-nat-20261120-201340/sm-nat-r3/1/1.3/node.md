# N8: LRU 策略在稳态下缓存的对象集合由访问间隔决定，对于 Pareto(β=0.9) 的请求热度，LRU 缓存命中率的下界近似等于前 k 个最热门对象覆盖的请求比

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

LRU 策略在稳态下缓存的对象集合由访问间隔决定，对于 Pareto(β=0.9) 的请求热度，LRU 缓存命中率的下界近似等于前 k 个最热门对象覆盖的请求比例，其中 k 为缓存能容纳的对象数量（受大小分布影响）

## Corrected Claim

LRU 策略在稳态下缓存的对象集合由访问间隔决定，对于 Pareto(β=0.9) 的请求热度，LRU 缓存命中率的下界近似等于前 k 个最热门对象覆盖的请求比例，其中 k 为缓存能容纳的对象数量（受大小分布影响）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU cache hit rate steady state Pareto request popularity
