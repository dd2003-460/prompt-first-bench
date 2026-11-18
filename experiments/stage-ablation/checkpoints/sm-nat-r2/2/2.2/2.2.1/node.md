# N41: LRU 缓存中对象 i 的驻留时间 W_i 近似等于 LRU 队列中第 i 个对象的平均等待时间，在稳态下 W_i ≈ K / (Σ_{j=1}^K λ_j)，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N12

## Claim

LRU 缓存中对象 i 的驻留时间 W_i 近似等于 LRU 队列中第 i 个对象的平均等待时间，在稳态下 W_i ≈ K / (Σ_{j=1}^K λ_j)，其中 K 为缓存容量内的对象数量

## Corrected Claim

LRU 缓存中对象 i 的驻留时间 W_i 近似等于 LRU 队列中第 i 个对象的平均等待时间，在稳态下 W_i ≈ K / (Σ_{j=1}^K λ_j)，其中 K 为缓存容量内的对象数量

## Evidence

先验知识/题面给定，逻辑校验通过
