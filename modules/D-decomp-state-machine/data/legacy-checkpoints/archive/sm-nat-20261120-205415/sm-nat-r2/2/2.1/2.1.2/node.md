# N41: 分子（缓存内请求字节数）的解析近似为 Num = Q_total * P(Hit_LRU)，其中 Q_total 为总请求字节数；在 Pareto(β=0.9)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

分子（缓存内请求字节数）的解析近似为 Num = Q_total * P(Hit_LRU)，其中 Q_total 为总请求字节数；在 Pareto(β=0.9) 热度下，前 K 个最热门对象的请求概率占比 P_topK = 1 - (K/N)^(1-β)（若按 Zipf 排名近似）。

## Corrected Claim

分子（缓存内请求字节数）的解析近似为 Num = Q_total * P(Hit_LRU)，其中 Q_total 为总请求字节数；在 Pareto(β=0.9) 热度下，前 K 个最热门对象的请求概率占比 P_topK = 1 - (K/N)^(1-β)（若按 Zipf 排名近似）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Zipf law cumulative probability top k items
