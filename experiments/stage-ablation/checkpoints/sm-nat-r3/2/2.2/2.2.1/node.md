# N41: LRU 缓存中对象 i 的驻留时间 W_i 近似等于 LRU 队列中第 i 个对象的平均等待时间，在稳态下 W_i ≈ K / (Σ_{j=1}^K λ_j)，

- **status**: pending
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

父节点级核验未通过：不完备（子节点之间存在逻辑依赖而非正交（子节点2依赖子节点1的定义），且未涵盖父节点公式中分母 Σλ_j 的推导过程，仅给出了基于单对象频率 λ_i 的近似，导致完备性不足。）
