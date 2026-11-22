# N44: 缓存内对象平均大小 E[S|in_cache] 的量化估计：假设缓存保留前 K 个最热门对象，且大小与热度负相关 ρ=-0.3，E[S|in_cache] ≈ 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

缓存内对象平均大小 E[S|in_cache] 的量化估计：假设缓存保留前 K 个最热门对象，且大小与热度负相关 ρ=-0.3，E[S|in_cache] ≈ E[S] * (1 + ρ * (Z_h - Z_s))，其中 Z 为标准化分数；简化估计下，若热门对象平均大小为全局平均的 0.8 倍，则 E[S|in_cache] ≈ 0.8 MB。

## Corrected Claim

缓存内对象平均大小 E[S|in_cache] 的量化估计：假设缓存保留前 K 个最热门对象，且大小与热度负相关 ρ=-0.3，E[S|in_cache] ≈ E[S] * (1 + ρ * (Z_h - Z_s))，其中 Z 为标准化分数；简化估计下，若热门对象平均大小为全局平均的 0.8 倍，则 E[S|in_cache] ≈ 0.8 MB。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于基础参数E[S]在Pareto分布下的定义与计算（分母/基准值），子节点2聚焦于修正因子(1 + ρ...)在偏态分布下的有效性及替代模型（分子/修正逻辑）。两者分别处理公式中的两个独立组成部分，无重叠且无矛盾，共同构成了对父节点简化估计方法的完整批判与修正。）

## Search Query

correlation between object size and popularity CDN cache average size
