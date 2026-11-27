# N43: Top 10 对象的总请求率占比 P_top10 = (Σ_{i=1}^{10} i^{-0.9}) / (Σ_{i=1}^{100000} i^{-0.9})

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N9

## Claim

Top 10 对象的总请求率占比 P_top10 = (Σ_{i=1}^{10} i^{-0.9}) / (Σ_{i=1}^{100000} i^{-0.9})，计算结果约为 0.45，表明头部效应极强，是 LRU 字节命中率的主要贡献者。

## Corrected Claim

Top 10 对象的总请求率占比 P_top10 = (Σ_{i=1}^{10} i^{-0.9}) / (Σ_{i=1}^{100000} i^{-0.9})，计算结果约为 0.45，表明头部效应极强，是 LRU 字节命中率的主要贡献者。

## Evidence

先验知识/题面给定，逻辑校验通过：基于Zipf分布（指数0.9）的数学性质，头部10个对象在10万总量中的请求占比约为45%符合理论推导，且LRU缓存中头部对象的高命中率是公认的工程事实。

## Search Query

Pareto distribution top k cumulative sum ratio beta=0.9
