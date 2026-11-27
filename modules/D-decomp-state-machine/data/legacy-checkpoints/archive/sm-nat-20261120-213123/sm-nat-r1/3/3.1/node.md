# N14: LRU 稳态字节命中率下界近似为 H_LRU ≈ 1 - (1/c) * ∫_0^∞ (1 - F_H(x)) dx，其中 c 为归一化容量，F_H 为热度分布

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

LRU 稳态字节命中率下界近似为 H_LRU ≈ 1 - (1/c) * ∫_0^∞ (1 - F_H(x)) dx，其中 c 为归一化容量，F_H 为热度分布的 CDF，此公式假设无更新且独立请求。

## Corrected Claim

LRU 稳态字节命中率下界近似为 H_LRU ≈ 1 - (1/c) * ∫_0^∞ (1 - F_H(x)) dx，其中 c 为归一化容量，F_H 为热度分布的 CDF，此公式假设无更新且独立请求。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU cache hit rate approximation Pareto workload
