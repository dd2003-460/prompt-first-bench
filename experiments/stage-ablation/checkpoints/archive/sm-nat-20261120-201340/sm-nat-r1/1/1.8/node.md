# N13: LFU 策略在稳态下缓存的对象集合由访问频率决定，对于 Pareto(β=0.9) 的请求热度，LFU 缓存命中率的上界近似等于前 k 个最高频率对象覆盖的请求

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

LFU 策略在稳态下缓存的对象集合由访问频率决定，对于 Pareto(β=0.9) 的请求热度，LFU 缓存命中率的上界近似等于前 k 个最高频率对象覆盖的请求比例，其中 k 为缓存能容纳的对象数量（受大小分布影响）

## Corrected Claim

LFU 策略在稳态下缓存的对象集合由访问频率决定，对于 Pareto(β=0.9) 的请求热度，LFU 缓存命中率的上界近似等于前 k 个最高频率对象覆盖的请求比例，其中 k 为缓存能容纳的对象数量（受大小分布影响）

## Evidence

先验知识/题面给定，逻辑校验通过：LFU 的核心机制即保留访问频率最高的对象，在稳态下其缓存集合趋近于频率最高的 k 个对象，因此命中率上界由这些对象覆盖的请求比例决定，符合缓存理论基本逻辑。

## Search Query

LFU cache hit rate steady state Pareto request popularity
