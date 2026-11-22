# N132: LRU 缓存覆盖的热度区间阈值 P_th 的解析表达式：P_th = (1 - R_k)^{1/(1-β)}，其中 R_k 为 LRU 字节命中率目标，β=0.

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

LRU 缓存覆盖的热度区间阈值 P_th 的解析表达式：P_th = (1 - R_k)^{1/(1-β)}，其中 R_k 为 LRU 字节命中率目标，β=0.9

## Corrected Claim

LRU 缓存覆盖的热度区间阈值 P_th 的解析表达式：P_th = (1 - R_k)^{1/(1-β)}，其中 R_k 为 LRU 字节命中率目标，β=0.9

## Evidence

先验知识/题面给定，逻辑校验通过
