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

父节点级核验通过：正交+完备+无冗余（子节点分别描述了LRU缓存在两种极端工作点（容量受限vs全量驻留）下的不同物理机制和公式适用性，逻辑互斥且互补，覆盖了公式失效与适用的边界条件，无重复内容。）
