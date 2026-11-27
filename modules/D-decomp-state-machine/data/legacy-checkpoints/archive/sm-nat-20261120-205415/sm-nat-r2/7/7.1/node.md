# N75: LRU稳态驻留集合L在稳态下等效于按热度降序排列的前K个对象，其中K由缓存容量C与对象大小分布决定：K ≈ C / E[S | S ≤ S_max]，S_max

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

LRU稳态驻留集合L在稳态下等效于按热度降序排列的前K个对象，其中K由缓存容量C与对象大小分布决定：K ≈ C / E[S | S ≤ S_max]，S_max为Pareto(α=1.1)分布下满足累积大小等于C的第K个对象的截断大小。

## Corrected Claim

LRU稳态驻留集合L在稳态下等效于按热度降序排列的前K个对象，其中K由缓存容量C与对象大小分布决定：K ≈ C / E[S | S ≤ S_max]，S_max为Pareto(α=1.1)分布下满足累积大小等于C的第K个对象的截断大小。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU在稳态下确实等效于保留热度最高的K个对象，且K由容量C与对象大小分布的期望值决定，公式推导符合缓存理论基本逻辑。
