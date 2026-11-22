# N42: 工作点 1 与真实 LRU 行为的偏差修正：真实 LRU 基于‘最近访问’而非‘累计热度’，在 Pareto 分布下，高频对象的访问间隔短，更容易保持在缓存顶部

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

工作点 1 与真实 LRU 行为的偏差修正：真实 LRU 基于‘最近访问’而非‘累计热度’，在 Pareto 分布下，高频对象的访问间隔短，更容易保持在缓存顶部。因此，H_base 使用 h_median 作为阈值是保守下界，真实 LRU 命中率应略高，因为 LRU 能动态适应访问间隔的波动，而静态热度阈值不能。

## Corrected Claim

工作点 1 与真实 LRU 行为的偏差修正：真实 LRU 基于‘最近访问’而非‘累计热度’，在 Pareto 分布下，高频对象的访问间隔短，更容易保持在缓存顶部。因此，H_base 使用 h_median 作为阈值是保守下界，真实 LRU 命中率应略高，因为 LRU 能动态适应访问间隔的波动，而静态热度阈值不能。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU基于最近访问，在Pareto分布下高频对象访问间隔短，确实比静态热度阈值更能适应波动，因此静态阈值作为保守下界是合理的。

## Search Query

LRU vs LFU static threshold approximation error Pareto workload
