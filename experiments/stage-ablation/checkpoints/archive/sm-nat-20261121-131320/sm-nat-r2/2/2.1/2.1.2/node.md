# N29: LRU 稳态字节命中率 H_LRU 的精确积分表达式：H_LRU = ∫_{x_min}^{S_max} f(s) * s * P(resident|s) ds

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N8

## Claim

LRU 稳态字节命中率 H_LRU 的精确积分表达式：H_LRU = ∫_{x_min}^{S_max} f(s) * s * P(resident|s) ds / Total_Bytes，其中 P(resident|s) 在 LRU 下取决于对象大小 s 是否小于当前缓存驱逐阈值 S_evict；S_evict 由缓存满时驱逐最小热度对象决定，需结合 N5 的下界模型与 N7 的相关性修正 K_ρ 进行数值积分。

## Corrected Claim

LRU 稳态字节命中率 H_LRU 的精确积分表达式：H_LRU = ∫_{x_min}^{S_max} f(s) * s * P(resident|s) ds / Total_Bytes，其中 P(resident|s) 在 LRU 下取决于对象大小 s 是否小于当前缓存驱逐阈值 S_evict；S_evict 由缓存满时驱逐最小热度对象决定，需结合 N5 的下界模型与 N7 的相关性修正 K_ρ 进行数值积分。

## Evidence

先验知识/题面给定，逻辑校验通过
