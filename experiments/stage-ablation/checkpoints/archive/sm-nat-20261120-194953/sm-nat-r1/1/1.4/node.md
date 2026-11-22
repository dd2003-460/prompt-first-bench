# N9: LRU 稳态字节命中率下界的核心公式：$H_{byte} \approx \frac{\sum_{i \in C_{LRU}} R_i S_i}{\sum_{i

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

LRU 稳态字节命中率下界的核心公式：$H_{byte} \approx \frac{\sum_{i \in C_{LRU}} R_i S_i}{\sum_{i=1}^{N} R_i S_i}$，其中 $C_{LRU}$ 为最近访问且未过期对象集合，下界估算需基于‘理想预知’或‘最坏情况’（如仅保留最新访问的 $K$ 个对象）进行积分或求和。

## Corrected Claim

LRU 稳态字节命中率下界的核心公式：$H_{byte} \approx \frac{\sum_{i \in C_{LRU}} R_i S_i}{\sum_{i=1}^{N} R_i S_i}$，其中 $C_{LRU}$ 为最近访问且未过期对象集合，下界估算需基于‘理想预知’或‘最坏情况’（如仅保留最新访问的 $K$ 个对象）进行积分或求和。

## Evidence

先验知识/题面给定，逻辑校验通过
