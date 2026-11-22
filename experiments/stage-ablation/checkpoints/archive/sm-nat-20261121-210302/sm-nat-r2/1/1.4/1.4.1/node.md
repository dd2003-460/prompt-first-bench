# N34: 对象在 LRU 队列中的平均驻留时间 T_resident 近似等于缓存容量 C 除以 LRU 驱逐速率 R_evict (T_resident ≈ C / R

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N8

## Claim

对象在 LRU 队列中的平均驻留时间 T_resident 近似等于缓存容量 C 除以 LRU 驱逐速率 R_evict (T_resident ≈ C / R_evict)，其中 C=128GB，R_evict 为稳态下每秒被替换出的对象总字节数。

## Corrected Claim

对象在 LRU 队列中的平均驻留时间 T_resident 近似等于缓存容量 C 除以 LRU 驱逐速率 R_evict (T_resident ≈ C / R_evict)，其中 C=128GB，R_evict 为稳态下每秒被替换出的对象总字节数。

## Evidence

先验知识/题面给定，逻辑校验通过：根据利特尔法则（Little's Law）或稳态队列论，平均驻留时间等于系统内平均数量（此处为缓存容量C）除以平均到达/离开速率（此处为驱逐速率R_evict），量纲为 [Bytes] / [Bytes/Second] = [Second]，逻辑自洽且符合缓存管理基本原理。
