# N10: LRU 稳态字节命中率下界 = (缓存中对象的请求字节数) / (总请求字节数)；在 Pareto 热度分布下，LRU 缓存前 k 个最频繁访问的对象，k 由 

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N2

## Claim

LRU 稳态字节命中率下界 = (缓存中对象的请求字节数) / (总请求字节数)；在 Pareto 热度分布下，LRU 缓存前 k 个最频繁访问的对象，k 由 C/平均大小 决定；命中率下界 ≈ ∑_{i=1}^k h_i * s_i / ∑_{i=1}^N h_i * s_i，其中 h_i 为第 i 个对象的请求频率

## Corrected Claim

LRU 稳态字节命中率下界 = (缓存中对象的请求字节数) / (总请求字节数)；在 Pareto 热度分布下，LRU 缓存前 k 个最频繁访问的对象，k 由 C/平均大小 决定；命中率下界 ≈ ∑_{i=1}^k h_i * s_i / ∑_{i=1}^N h_i * s_i，其中 h_i 为第 i 个对象的请求频率

## Evidence

父节点级核验失败（LLM 错误）：Invalid \escape: line 5 column 461 (char 528)
