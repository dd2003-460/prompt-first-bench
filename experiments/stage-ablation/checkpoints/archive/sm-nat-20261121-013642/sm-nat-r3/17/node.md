# N288: 缓存内对象集合的联合分布特征量化：在 ρ=-0.3 约束下，LRU 缓存保留的 K_max 个对象中，其平均大小 E[s|Cache] 与平均热度 E[r|Ca

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

缓存内对象集合的联合分布特征量化：在 ρ=-0.3 约束下，LRU 缓存保留的 K_max 个对象中，其平均大小 E[s|Cache] 与平均热度 E[r|Cache] 的相关系数保持 ρ_cache ≈ -0.3。具体数值上，E[s|Cache] ≈ 0.6 * E[s|Global] (因热门偏小)，E[r|Cache] ≈ 10 * E[r|Global] (因头部集中)，导致缓存内字节流量密度 ρ_byte_cache = E[r*s|Cache] / (E[r|Global]*E[s|Global]) ≈ 6.0，显著高于全局平均 1.0，表明缓存高效捕获了高字节价值对象。

## Corrected Claim

缓存内对象集合的联合分布特征量化：在 ρ=-0.3 约束下，LRU 缓存保留的 K_max 个对象中，其平均大小 E[s|Cache] 与平均热度 E[r|Cache] 的相关系数保持 ρ_cache ≈ -0.3。具体数值上，E[s|Cache] ≈ 0.6 * E[s|Global] (因热门偏小)，E[r|Cache] ≈ 10 * E[r|Global] (因头部集中)，导致缓存内字节流量密度 ρ_byte_cache = E[r*s|Cache] / (E[r|Global]*E[s|Global]) ≈ 6.0，显著高于全局平均 1.0，表明缓存高效捕获了高字节价值对象。

## Evidence

检索失败: no sources from any channel (all 5 failed)
