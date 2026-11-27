# N59: LFU 保留对象集合 Cache_LFU 的确定准则：在稳态下，LFU 保留访问频率最高的对象。具体而言，对象 i 被保留当且仅当其访问频率 f_i = λ_i

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N15

## Claim

LFU 保留对象集合 Cache_LFU 的确定准则：在稳态下，LFU 保留访问频率最高的对象。具体而言，对象 i 被保留当且仅当其访问频率 f_i = λ_i / Σ_j λ_j 大于第 N_cache 个对象的频率，其中 N_cache 为缓存可容纳的对象数量上限。

## Corrected Claim

LFU 保留对象集合 Cache_LFU 的确定准则：在稳态下，LFU 保留访问频率最高的对象。具体而言，对象 i 被保留当且仅当其访问频率 f_i = λ_i / Σ_j λ_j 大于第 N_cache 个对象的频率，其中 N_cache 为缓存可容纳的对象数量上限。

## Evidence

先验知识/题面给定，逻辑校验通过
