# N54: S_avg_cached 的计算：S_avg_cached = (∫_{k=1}^{K} 116.36 * k^{-0.1} dk) / K ≈ 116.36 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

S_avg_cached 的计算：S_avg_cached = (∫_{k=1}^{K} 116.36 * k^{-0.1} dk) / K ≈ 116.36 * (K^{0.9} / 0.9) / K = 116.36 * K^{-0.1} / 0.9，其中 K 是缓存容量对应的对象数，需从 N10 的 K 值代入。

## Corrected Claim

S_avg_cached 的计算：S_avg_cached = (∫_{k=1}^{K} 116.36 * k^{-0.1} dk) / K ≈ 116.36 * (K^{0.9} / 0.9) / K = 116.36 * K^{-0.1} / 0.9，其中 K 是缓存容量对应的对象数，需从 N10 的 K 值代入。

## Evidence

先验知识/题面给定，逻辑校验通过：积分计算 ∫k^{-0.1}dk = k^{0.9}/0.9，除以 K 后得到 K^{-0.1}/0.9，数学推导正确。

## Search Query

average object size in LRU cache Pareto distribution
