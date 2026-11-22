# N61: 对象更新率 1%/天 在指数分布假设下意味着任意时刻单个对象处于‘失效’状态的概率 p_invalid = 1 - exp(-0.01 * t)，在稳态下（t 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

对象更新率 1%/天 在指数分布假设下意味着任意时刻单个对象处于‘失效’状态的概率 p_invalid = 1 - exp(-0.01 * t)，在稳态下（t 远大于 1/0.01）p_invalid 趋近于 1，但缓存中对象的有效命中率受更新频率影响。

## Corrected Claim

对象更新率 1%/天 在指数分布假设下意味着任意时刻单个对象处于‘失效’状态的概率 p_invalid = 1 - exp(-0.01 * t)，在稳态下（t 远大于 1/0.01）p_invalid 趋近于 1，但缓存中对象的有效命中率受更新频率影响。

## Evidence

先验知识/题面给定，逻辑校验通过：指数分布的生存函数公式正确，稳态极限推导符合数学定义，且缓存命中率受更新频率影响的定性描述符合缓存理论基本直觉。

## Search Query

object update rate exponential distribution cache invalidation probability
