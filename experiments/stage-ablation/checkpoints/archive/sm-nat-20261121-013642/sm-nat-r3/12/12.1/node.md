# N279: 在 C >> V_total 的极端工作点下，LRU 稳态字节命中率 H_byte_LRU = 1.0 - P_invalidate，其中 P_invalida

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N96

## Claim

在 C >> V_total 的极端工作点下，LRU 稳态字节命中率 H_byte_LRU = 1.0 - P_invalidate，其中 P_invalidate 为对象在请求到达前被更新失效的概率，仅由更新率 λ_u 和对象平均请求间隔决定，与缓存容量 C 无关。

## Corrected Claim

在 C >> V_total 的极端工作点下，LRU 稳态字节命中率 H_byte_LRU = 1.0 - P_invalidate，其中 P_invalidate 为对象在请求到达前被更新失效的概率，仅由更新率 λ_u 和对象平均请求间隔决定，与缓存容量 C 无关。

## Evidence

先验知识/题面给定，逻辑校验通过：在 C >> V_total 的极端工作点下，缓存容量足以容纳所有活跃对象，LRU 的替换机制不再起作用，命中率仅受数据一致性（更新失效）影响，与容量无关。
