# N28: 主要不确定性来源 2：热门对象与大小的负相关（ρ≈-0.3）的具体函数形式未指定（线性/对数/其他），影响 LRU 队列中对象排序的精确性，估计误差范围 ±3-

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N5

## Claim

主要不确定性来源 2：热门对象与大小的负相关（ρ≈-0.3）的具体函数形式未指定（线性/对数/其他），影响 LRU 队列中对象排序的精确性，估计误差范围 ±3-7% [待核验]。

## Corrected Claim

主要不确定性来源 2：热门对象与大小的负相关的具体函数形式未指定，影响 LRU 队列中对象排序的精确性，具体相关系数及误差范围需进一步实证确定。

## Evidence

[质询]该陈述包含具体的经验性数值（ρ≈-0.3）和误差范围（±3-7%），属于经验事实而非第一性原理可推导内容，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

negative correlation between object popularity and size impact on LRU cache hit rate Pareto distribution
