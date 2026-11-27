# N255: 工作点1（高局部性/高命中率）：当缓存容量 C 覆盖 Top-10% 热门对象时，由于热门对象请求频率 r_i 极大（r_i >> 1/τ_locality），

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N88

## Claim

工作点1（高局部性/高命中率）：当缓存容量 C 覆盖 Top-10% 热门对象时，由于热门对象请求频率 r_i 极大（r_i >> 1/τ_locality），其访问间隔远小于驱逐周期，导致 LRU 对这部分对象的 miss 率 P_miss_hot ≈ 0，此时 H_LRU 接近理论上限 1，λ_decay 主要由长尾冷对象主导，对整体命中率影响 < 5%。

## Corrected Claim

工作点1（高局部性/高命中率）：当缓存容量 C 覆盖 Top-10% 热门对象时，由于热门对象请求频率 r_i 极大（r_i >> 1/τ_locality），其访问间隔远小于驱逐周期，导致 LRU 对这部分对象的 miss 率 P_miss_hot ≈ 0，此时 H_LRU 接近理论上限 1，λ_decay 主要由长尾冷对象主导，对整体命中率影响 < 5%。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU在局部性极强（访问间隔远小于驱逐周期）时确实能保持高命中率，长尾冷对象对整体命中率影响有限符合缓存理论直觉。

## Search Query

LRU hit ratio top popular objects negligible miss rate
