# N49: Pareto(β=0.9)分布下，单对象请求频率 f_i 与排名 i 的关系为 f_i ∝ i^(-β)，用于推导 LRU 在时间局部性假设下，头部对象（i 较

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

Pareto(β=0.9)分布下，单对象请求频率 f_i 与排名 i 的关系为 f_i ∝ i^(-β)，用于推导 LRU 在时间局部性假设下，头部对象（i 较小）的平均驻留时间 T_res 与总请求率 R 的比例关系。

## Corrected Claim

Pareto(β=0.9)分布下，单对象请求频率 f_i 与排名 i 的关系为 f_i ∝ i^(-β)，用于推导 LRU 在时间局部性假设下，头部对象（i 较小）的平均驻留时间 T_res 与总请求率 R 的比例关系。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布定义及LRU驻留时间推导符合标准缓存理论模型
