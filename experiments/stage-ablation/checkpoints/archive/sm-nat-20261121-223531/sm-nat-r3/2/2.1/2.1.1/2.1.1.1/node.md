# N119: 若假设容量受限（例如 C_eff = 10% * S_total），则保留比例 k_retention = 0.1，对应热度阈值 h_ref = h_min *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

若假设容量受限（例如 C_eff = 10% * S_total），则保留比例 k_retention = 0.1，对应热度阈值 h_ref = h_min * (1/0.1)^{1/(1-β)} = h_min * 10^{10}。此时 HitRate_base 的下界由未被缓存的 90% 对象的字节占比决定，需计算 ∫_{s_min}^{s_max} s * f_S(s) * F_H(h_ref) ds / E[S]_trunc，其中 F_H(h_ref) = 0.9。

## Corrected Claim

若假设容量受限（例如 C_eff = 10% * S_total），则保留比例 k_retention = 0.1，对应热度阈值 h_ref = h_min * (1/0.1)^{1/(1-β)} = h_min * 10^{10}。此时 HitRate_base 的下界由未被缓存的 90% 对象的字节占比决定，需计算 ∫_{s_min}^{s_max} s * f_S(s) * F_H(h_ref) ds / E[S]_trunc，其中 F_H(h_ref) = 0.9。

## Evidence

先验知识/题面给定，逻辑校验通过：保留比例 k=0.1 对应热度阈值推导符合幂律分布性质，HitRate 下界由未缓存对象字节占比决定的积分表达式在逻辑和量纲上自洽。
