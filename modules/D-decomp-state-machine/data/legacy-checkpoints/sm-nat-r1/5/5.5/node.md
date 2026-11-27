# N29: 主要不确定性来源 3：1%/天 更新率是否均匀分布在所有对象上，还是集中在某些对象（如动态内容），影响 Cache Thrashing 的局部化程度，估计误差范

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N5

## Claim

主要不确定性来源 3：1%/天 更新率是否均匀分布在所有对象上，还是集中在某些对象（如动态内容），影响 Cache Thrashing 的局部化程度，估计误差范围 ±10-15% [待核验]。

## Corrected Claim

主要不确定性来源 3：1%/天 更新率是否均匀分布在所有对象上，还是集中在某些对象（如动态内容），影响 Cache Thrashing 的局部化程度。具体误差范围需进一步实证数据支持，当前估计为 ±10-15%（待核验）。

## Evidence

[质询]该陈述包含具体的经验性数值估计（±10-15%误差范围）和关于更新分布模式的假设，属于经验事实，无法从第一性原理严格推导，且缺乏外部来源支持。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。

## Search Query

non-uniform object update rate distribution impact on LRU cache invalidation CDN
