# N74: LRU缓存内对象平均驻留时间 $T_{avg}$ 的计算公式为 $T_{avg} = \frac{K_{cap}}{\lambda_{total}}$，其中 $

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N25

## Claim

LRU缓存内对象平均驻留时间 $T_{avg}$ 的计算公式为 $T_{avg} = \frac{K_{cap}}{\lambda_{total}}$，其中 $K_{cap} = 128GB / E[S]$ 为缓存容量对象数，$\lambda_{total} = 5 \times 10^7 / 86400$ 为总请求率（req/s）

## Corrected Claim

LRU缓存内对象平均驻留时间 $T_{avg}$ 的计算公式为 $T_{avg} = \frac{K_{cap}}{\lambda_{total}}$，其中 $K_{cap} = 128GB / E[S]$ 为缓存容量对象数，$\lambda_{total} = 5 \times 10^7 / 86400$ 为总请求率（req/s）

## Evidence

先验知识/题面给定，逻辑校验通过：LRU缓存平均驻留时间等于缓存容量（对象数）除以总到达率（req/s），量纲为 [对象] / [1/s] = [s]，符合Little定律及排队论基本直觉。
