# N11: LRU 工作集大小估计：在热度 Pareto(β=0.9) 下，LRU 保留最近访问的对象，其有效工作集大小 W_LRU 近似为 N * (1 - (1 - p

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

LRU 工作集大小估计：在热度 Pareto(β=0.9) 下，LRU 保留最近访问的对象，其有效工作集大小 W_LRU 近似为 N * (1 - (1 - p)^{1/β})，其中 p 为缓存命中率目标，需通过迭代求解与 128GB 容量匹配的 p 值

## Corrected Claim

LRU 工作集大小估计：在热度 Pareto(β=0.9) 下，LRU 保留最近访问的对象，其有效工作集大小 W_LRU 近似为 N * (1 - (1 - p)^{1/β})，其中 p 为缓存命中率目标，需通过迭代求解与 128GB 容量匹配的 p 值

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU working set size estimation Pareto popularity distribution
