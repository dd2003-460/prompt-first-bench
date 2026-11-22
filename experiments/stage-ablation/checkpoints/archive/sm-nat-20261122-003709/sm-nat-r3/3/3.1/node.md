# N13: 容量未命中与一致性未命中的正交分解：总未命中率 M_total = M_capacity + M_invalidation - M_capacity * M_i

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N3

## Claim

容量未命中与一致性未命中的正交分解：总未命中率 M_total = M_capacity + M_invalidation - M_capacity * M_invalidation，其中 M_capacity 为纯容量限制导致的未命中，M_invalidation 为因对象更新导致的缓存失效未命中。

## Corrected Claim

容量未命中与一致性未命中的正交分解：总未命中率 M_total = M_capacity + M_invalidation - M_capacity * M_invalidation，其中 M_capacity 为纯容量限制导致的未命中，M_invalidation 为因对象更新导致的缓存失效未命中。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合概率论中两个独立事件并集的概率计算逻辑（P(A∪B) = P(A) + P(B) - P(A)P(B)），在缓存理论中常假设容量未命中与一致性未命中在统计上近似独立或正交，公式量纲与逻辑自洽。
