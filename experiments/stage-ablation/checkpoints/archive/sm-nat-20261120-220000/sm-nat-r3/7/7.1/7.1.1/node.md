# N133: LRU 稳态字节命中率下界公式中，$q^*$ 为被缓存对象的热度占比，$S_{uncovered}$ 为未缓存对象的字节占比。在 C/S_total >> 1 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N52

## Claim

LRU 稳态字节命中率下界公式中，$q^*$ 为被缓存对象的热度占比，$S_{uncovered}$ 为未缓存对象的字节占比。在 C/S_total >> 1 时，$S_{uncovered} \to 0$，因此 $H_{LRU} \to 1$。若 C 仅覆盖前 $K$ 个对象，则 $H_{LRU} = 1 - (1 - q_K) \times (S_{tail}/S_{total})$ 不适用，因为未缓存对象的请求也会产生 miss，正确公式为 $H_{LRU} = \frac{\sum_{i \in Cache} S_i F_i}{\sum_{i=1}^{N} S_i F_i}$。

## Corrected Claim

LRU 稳态字节命中率下界公式中，$q^*$ 为被缓存对象的热度占比，$S_{uncovered}$ 为未缓存对象的字节占比。在 C/S_total >> 1 时，$S_{uncovered} \to 0$，因此 $H_{LRU} \to 1$。若 C 仅覆盖前 $K$ 个对象，则 $H_{LRU} = 1 - (1 - q_K) \times (S_{tail}/S_{total})$ 不适用，因为未缓存对象的请求也会产生 miss，正确公式为 $H_{LRU} = \frac{\sum_{i \in Cache} S_i F_i}{\sum_{i=1}^{N} S_i F_i}$。

## Evidence

先验知识/题面给定，逻辑校验通过
