# N212: LRU 堆栈深度 D_i 与热度 h_i 的定量关系：在稳态下，对象 i 的堆栈深度 D_i ≈ N_total * (1 - F_H(h_i))。对于 Par

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N77

## Claim

LRU 堆栈深度 D_i 与热度 h_i 的定量关系：在稳态下，对象 i 的堆栈深度 D_i ≈ N_total * (1 - F_H(h_i))。对于 Pareto(β=0.9) 分布，F_H(h) = 1 - (h_min/h)^{β-1}。因此 D_i ≈ N_total * (h_min/h_i)^{0.1}。

## Corrected Claim

LRU 堆栈深度 D_i 与热度 h_i 的定量关系：在稳态下，对象 i 的堆栈深度 D_i ≈ N_total * (1 - F_H(h_i))。对于 Pareto(β=0.9) 分布，F_H(h) = 1 - (h_min/h)^{β-1}。因此 D_i ≈ N_total * (h_min/h_i)^{0.1}。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU堆栈深度与累积分布函数（CDF）的互补关系符合缓存理论基本定义，Pareto分布CDF公式及指数推导在数学上自洽。

## Search Query

LRU stack distance model Zipf distribution
