# N235: LRU 下界公式的 LRU 堆栈距离修正：原公式假设 Cold 对象完全未缓存，但 LRU 会缓存部分 Cold 对象（堆栈深度 < C），修正后 H_LRU_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N85

## Claim

LRU 下界公式的 LRU 堆栈距离修正：原公式假设 Cold 对象完全未缓存，但 LRU 会缓存部分 Cold 对象（堆栈深度 < C），修正后 H_LRU_lb = 1 - (1 - k)^{1-β} * (E[S|Evicted] / E[S])，其中 E[S|Evicted] 需通过堆栈距离分布 P(D_i > C) 加权计算。

## Corrected Claim

LRU 下界公式的 LRU 堆栈距离修正：原公式假设 Cold 对象完全未缓存，但 LRU 会缓存部分 Cold 对象（堆栈深度 < C），修正后 H_LRU_lb = 1 - (1 - k)^{1-β} * (E[S|Evicted] / E[S])，其中 E[S|Evicted] 需通过堆栈距离分布 P(D_i > C) 加权计算。

## Evidence

先验知识/题面给定，逻辑校验通过
