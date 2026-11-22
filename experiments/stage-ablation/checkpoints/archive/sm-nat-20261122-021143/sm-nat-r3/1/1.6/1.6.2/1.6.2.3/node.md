# N93: 该 11.23% 是请求数（request count）占比，但题目问的是字节命中率（byte hit rate）；由于冷对象（k>K）的平均大小 S_k 小于

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N34

## Claim

该 11.23% 是请求数（request count）占比，但题目问的是字节命中率（byte hit rate）；由于冷对象（k>K）的平均大小 S_k 小于热门对象，其字节占比 P_cold_byte = Σ_{k>K} R_k S_k / Σ_{k=1}^{N} R_k S_k 会低于 11.23%

## Corrected Claim

该 11.23% 是请求数（request count）占比，但题目问的是字节命中率（byte hit rate）；由于冷对象（k>K）的平均大小 S_k 小于热门对象，其字节占比 P_cold_byte = Σ_{k>K} R_k S_k / Σ_{k=1}^{N} R_k S_k 会低于 11.23%

## Evidence

先验知识/题面给定，逻辑校验通过：在缓存系统中，若冷对象（k>K）的平均大小 S_k 小于热门对象，则其字节占比必然低于请求数占比（11.23%），符合加权平均的基本数学逻辑。
