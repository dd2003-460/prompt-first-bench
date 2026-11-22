# N87: TopK 子集的累计字节占比 R_byte_TopK：R_byte_TopK = Σ_{i=1}^{K_max} S_i / Σ_{all} S_i；利用 Pa

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N28

## Claim

TopK 子集的累计字节占比 R_byte_TopK：R_byte_TopK = Σ_{i=1}^{K_max} S_i / Σ_{all} S_i；利用 Pareto(α=1.1) 的生存函数 P(S>S_th) 和负相关修正，计算头部 K_max 个对象（按热度降序）所占总字节数的比例，该值即为 H_LFU 的上界（假设 LFU 完美锁定 TopK）。

## Corrected Claim

TopK 子集的累计字节占比 R_byte_TopK：R_byte_TopK = Σ_{i=1}^{K_max} S_i / Σ_{all} S_i；利用 Pareto(α=1.1) 的生存函数 P(S>S_th) 和负相关修正，计算头部 K_max 个对象（按热度降序）所占总字节数的比例，该值即为 H_LFU 的上界（假设 LFU 完美锁定 TopK）。

## Evidence

先验知识/题面给定，逻辑校验通过：TopK 字节占比的定义符合数学逻辑，且作为 LFU 完美锁定假设下的上界，其推导符合缓存理论的基本直觉。
