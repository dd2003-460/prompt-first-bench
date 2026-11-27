# N113: Top 10 对象在 LRU 缓存中的实际驻留概率 P_resident 并非恒为 1.0，而是取决于其最小访问间隔 T_min 与 LRU 队列中其他对象访问

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

Top 10 对象在 LRU 缓存中的实际驻留概率 P_resident 并非恒为 1.0，而是取决于其最小访问间隔 T_min 与 LRU 队列中其他对象访问间隔的分布；若 T_min > T_LRU_evict（驱逐时间阈值），则 P_resident < 1.0，需计算 T_LRU_evict = C_bytes / (Σ_{j∈Queue} s_j * λ_j) 以验证是否溢出

## Corrected Claim

Top 10 对象在 LRU 缓存中的实际驻留概率 P_resident 并非恒为 1.0，而是取决于其最小访问间隔 T_min 与 LRU 队列中其他对象访问间隔的分布；若 T_min > T_LRU_evict（驱逐时间阈值），则 P_resident < 1.0，需计算 T_LRU_evict = C_bytes / (Σ_{j∈Queue} s_j * λ_j) 以验证是否溢出

## Evidence

先验知识/题面给定，逻辑校验通过：LRU 驱逐机制基于最近访问时间，若对象最小访问间隔超过缓存容量对应的平均驻留时间（由总字节数除以总访问速率估算），则必然发生驱逐，概率小于1，公式量纲与逻辑自洽。
