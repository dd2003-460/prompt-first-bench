# N44: 缓存内对象平均大小 E[S|in_cache] 的量化估计：假设缓存保留前 K 个最热门对象，且大小与热度负相关 ρ=-0.3，E[S|in_cache] ≈ 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

缓存内对象平均大小 E[S|in_cache] 的量化估计：假设缓存保留前 K 个最热门对象，且大小与热度负相关 ρ=-0.3，E[S|in_cache] ≈ E[S] * (1 + ρ * (Z_h - Z_s))，其中 Z 为标准化分数；简化估计下，若热门对象平均大小为全局平均的 0.8 倍，则 E[S|in_cache] ≈ 0.8 MB。

## Corrected Claim

缓存内对象平均大小 E[S|in_cache] 的量化估计：假设缓存保留前 K 个最热门对象，且大小与热度负相关 ρ=-0.3，E[S|in_cache] ≈ E[S] * (1 + ρ * (Z_h - Z_s))，其中 Z 为标准化分数；简化估计下，若热门对象平均大小为全局平均的 0.8 倍，则 E[S|in_cache] ≈ 0.8 MB。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

correlation between object size and popularity CDN cache average size
