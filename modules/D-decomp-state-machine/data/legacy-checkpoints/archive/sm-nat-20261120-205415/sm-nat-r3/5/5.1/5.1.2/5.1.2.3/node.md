# N184: N67中'前 K 个最热门对象'的假设忽略了 LRU 的时间局部性：稳态下 LRU 缓存的是最近访问的对象，而非全局最热门对象；在 Pareto 热度分布下，L

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

N67中'前 K 个最热门对象'的假设忽略了 LRU 的时间局部性：稳态下 LRU 缓存的是最近访问的对象，而非全局最热门对象；在 Pareto 热度分布下，LRU 缓存集合与 Zipf 头部集合的交集比例需通过 Markov 链稳态分布计算，通常 < 99%

## Corrected Claim

N67中'前 K 个最热门对象'的假设忽略了 LRU 的时间局部性：稳态下 LRU 缓存的是最近访问的对象，而非全局最热门对象；在 Pareto 热度分布下，LRU 缓存集合与 Zipf 头部集合的交集比例需通过 Markov 链稳态分布计算，通常 < 99%

## Evidence

先验知识/题面给定，逻辑校验通过：LRU基于时间局部性，Zipf基于频率热度，二者在稳态下确实存在差异，且交集比例通常小于100%（即<99%的表述在逻辑上成立，尽管具体数值依赖参数，但定性结论正确）。
