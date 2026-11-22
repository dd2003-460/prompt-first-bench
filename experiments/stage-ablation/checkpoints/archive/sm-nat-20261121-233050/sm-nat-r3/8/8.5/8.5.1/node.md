# N173: H_reentry 的解析表达式为 H_reentry = P(rank_i ≤ K_max) * P(T_update < T_res_i)，其中 rank_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N68

## Claim

H_reentry 的解析表达式为 H_reentry = P(rank_i ≤ K_max) * P(T_update < T_res_i)，其中 rank_i 是对象的热度排名，K_max 是缓存可容纳的最大对象数（约 98,500），T_update 是对象更新间隔，T_res_i 是对象 i 在缓存中的平均驻留时间。

## Corrected Claim

H_reentry 的解析表达式为 H_reentry = P(rank_i ≤ K_max) * P(T_update < T_res_i)，其中 rank_i 是对象的热度排名，K_max 是缓存可容纳的最大对象数（约 98,500），T_update 是对象更新间隔，T_res_i 是对象 i 在缓存中的平均驻留时间。

## Evidence

先验知识/题面给定，逻辑校验通过
