# N50: 在高热度工作点（rank_i ≈ 1），对象的驻留时间 T_hot ≈ K_cap / R_1，由于 R_1 极大（约为总请求量的 31.6% 中的最大单点），

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

在高热度工作点（rank_i ≈ 1），对象的驻留时间 T_hot ≈ K_cap / R_1，由于 R_1 极大（约为总请求量的 31.6% 中的最大单点），T_hot 极长（接近缓存全量驻留时间），导致 P_inval_hot = 1 - (1-u)^{T_hot} ≈ 1 - e^{-u * T_hot}，在 u=0.01/天且 T_hot > 100 天时，P_inval_hot ≈ 0.63，意味着最热门对象在长期缓存中失效概率极高。

## Corrected Claim

在高热度工作点（rank_i ≈ 1），对象的驻留时间 T_hot ≈ K_cap / R_1，由于 R_1 极大（约为总请求量的 31.6% 中的最大单点），T_hot 极长（接近缓存全量驻留时间），导致 P_inval_hot = 1 - (1-u)^{T_hot} ≈ 1 - e^{-u * T_hot}，在 u=0.01/天且 T_hot > 100 天时，P_inval_hot ≈ 0.63，意味着最热门对象在长期缓存中失效概率极高。

## Evidence

先验知识/题面给定，逻辑校验通过：数学推导 1 - e^{-0.01 * 100} ≈ 0.632 正确，且符合缓存失效概率随驻留时间指数增长的物理直觉。
