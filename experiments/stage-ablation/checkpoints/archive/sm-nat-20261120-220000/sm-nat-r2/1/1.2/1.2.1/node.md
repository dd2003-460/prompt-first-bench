# N22: LRU 稳态字节命中率下界的计算需基于字节加权热度分布：设对象 i 的大小为 S_i，热度为 F_i，总字节请求量 B_total = Σ S_i F_i。LR

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N6

## Claim

LRU 稳态字节命中率下界的计算需基于字节加权热度分布：设对象 i 的大小为 S_i，热度为 F_i，总字节请求量 B_total = Σ S_i F_i。LRU 缓存容量 C 对应的字节命中率 H_LRU(C) = (Σ_{i ∈ Cache} S_i F_i) / B_total，其中 Cache 为最近访问过的、累积大小不超过 C 的对象集合。

## Corrected Claim

LRU 稳态字节命中率下界的计算需基于字节加权热度分布：设对象 i 的大小为 S_i，热度为 F_i，总字节请求量 B_total = Σ S_i F_i。LRU 缓存容量 C 对应的字节命中率 H_LRU(C) = (Σ_{i ∈ Cache} S_i F_i) / B_total，其中 Cache 为最近访问过的、累积大小不超过 C 的对象集合。

## Evidence

先验知识/题面给定，逻辑校验通过
