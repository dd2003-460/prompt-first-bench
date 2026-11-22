# N10: LRU 缓存容量约束下的 K 值计算：根据对象大小分布 Pareto(α=1.1)，计算满足 Sum_{i=1}^K S_i <= 128GB 的最大 K 值，

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

LRU 缓存容量约束下的 K 值计算：根据对象大小分布 Pareto(α=1.1)，计算满足 Sum_{i=1}^K S_i <= 128GB 的最大 K 值，这是 LRU 能容纳的热门对象数量上限。

## Corrected Claim

LRU 缓存容量约束下的 K 值计算：根据对象大小分布 Pareto(α=1.1)，计算满足 Sum_{i=1}^K S_i <= 128GB 的最大 K 值，这是 LRU 能容纳的热门对象数量上限。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU缓存容量约束下，通过累加按热度排序的对象大小直至超过总容量（128GB），其对应的最大对象数量K即为LRU能容纳的热门对象数量上限，该定义与计算逻辑在数学和工程直觉上均自洽。

## Search Query

Pareto distribution cumulative sum capacity constraint
