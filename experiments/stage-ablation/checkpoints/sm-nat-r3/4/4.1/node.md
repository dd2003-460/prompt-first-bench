# N16: 更新导致的缓存失效比例 (Invalidation Rate) $R_{inv}$ 近似为 $1 - e^{-\lambda \cdot T_{LRU}}$，其

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

更新导致的缓存失效比例 (Invalidation Rate) $R_{inv}$ 近似为 $1 - e^{-\lambda \cdot T_{LRU}}$，其中 $\lambda=0.01/day$，$T_{LRU}$ 为对象在 LRU 队列中的平均驻留时间（由工作集大小和请求频率决定）。

## Corrected Claim

更新导致的缓存失效比例 (Invalidation Rate) $R_{inv}$ 近似为 $1 - e^{-\lambda \cdot T_{LRU}}$，其中 $\lambda=0.01/day$，$T_{LRU}$ 为对象在 LRU 队列中的平均驻留时间（由工作集大小和请求频率决定）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU cache invalidation rate update frequency formula
