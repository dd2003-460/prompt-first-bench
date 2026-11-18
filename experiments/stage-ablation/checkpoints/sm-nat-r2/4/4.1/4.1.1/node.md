# N54: 对象在 LRU 队列中的平均驻留时间 T_LRU 的计算公式：T_LRU = K_LRU / R_total，其中 K_LRU 为 LRU 缓存的对象数量，R_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

对象在 LRU 队列中的平均驻留时间 T_LRU 的计算公式：T_LRU = K_LRU / R_total，其中 K_LRU 为 LRU 缓存的对象数量，R_total 为总请求率（50,000,000/day）；对于热门对象，T_LRU 远小于全局平均值，需按热度分层计算。

## Corrected Claim

对象在 LRU 队列中的平均驻留时间 T_LRU 的计算公式：T_LRU = K_LRU / R_total，其中 K_LRU 为 LRU 缓存的对象数量，R_total 为总请求率（50,000,000/day）；对于热门对象，T_LRU 远小于全局平均值，需按热度分层计算。

## Evidence

先验知识/题面给定，逻辑校验通过
