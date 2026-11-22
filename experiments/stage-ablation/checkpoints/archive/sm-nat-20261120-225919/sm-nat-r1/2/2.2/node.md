# N11: LRU 命中率下界的另一个代表性工作点是‘中容量利用率’场景：考虑对象大小差异，缓存实际存储的对象数量 K' < K，命中率下界 = Σ_{i∈C'} R_i 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

LRU 命中率下界的另一个代表性工作点是‘中容量利用率’场景：考虑对象大小差异，缓存实际存储的对象数量 K' < K，命中率下界 = Σ_{i∈C'} R_i / 5×10^7，其中 C' 是满足 Σ_{i∈C'} S_i ≤ 128GB 的最大热度集合。

## Corrected Claim

LRU 命中率下界的另一个代表性工作点是‘中容量利用率’场景：考虑对象大小差异，缓存实际存储的对象数量 K' < K，命中率下界 = Σ_{i∈C'} R_i / 5×10^7，其中 C' 是满足 Σ_{i∈C'} S_i ≤ 128GB 的最大热度集合。

## Evidence

先验知识/题面给定，逻辑校验通过
