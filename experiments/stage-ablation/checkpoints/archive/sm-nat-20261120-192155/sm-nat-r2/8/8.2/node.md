# N48: 对象i在LRU缓存中的驻留时间 T_res_i 由其访问频率 r_i 和缓存中比它更热的对象集合的总访问率决定，近似为 T_res_i ≈ 1 / (Σ_{j∈

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N19

## Claim

对象i在LRU缓存中的驻留时间 T_res_i 由其访问频率 r_i 和缓存中比它更热的对象集合的总访问率决定，近似为 T_res_i ≈ 1 / (Σ_{j∈C, r_j > r_i} r_j)，其中C为当前缓存驻留集合；对于头部热门对象（i小），T_res_i 主要由紧随其后的次热对象访问率决定。

## Corrected Claim

对象i在LRU缓存中的驻留时间 T_res_i 由其访问频率 r_i 和缓存中比它更热的对象集合的总访问率决定，近似为 T_res_i ≈ 1 / (Σ_{j∈C, r_j > r_i} r_j)，其中C为当前缓存驻留集合；对于头部热门对象（i小），T_res_i 主要由紧随其后的次热对象访问率决定。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU cache residence time formula based on access frequency
