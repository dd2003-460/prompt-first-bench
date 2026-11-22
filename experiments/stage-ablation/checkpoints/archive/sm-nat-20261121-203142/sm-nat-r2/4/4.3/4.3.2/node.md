# N56: u=0.001 时缓存失效的稳态概率 P_invalidation 近似等于更新率 u，即 0.001，前提是对象更新事件在时间上均匀分布且独立于访问模式

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

u=0.001 时缓存失效的稳态概率 P_invalidation 近似等于更新率 u，即 0.001，前提是对象更新事件在时间上均匀分布且独立于访问模式

## Corrected Claim

u=0.001 时缓存失效的稳态概率 P_invalidation 近似等于更新率 u，即 0.001，前提是对象更新事件在时间上均匀分布且独立于访问模式

## Evidence

先验知识/题面给定，逻辑校验通过：在更新率极低（u=0.001）且更新事件独立均匀分布的假设下，缓存项在两次访问间被更新的概率近似等于更新率，符合泊松过程或独立事件概率的基本推导。
