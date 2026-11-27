# N8: 大小-热度相关性量化：ρ=-0.3 意味着热门对象 (rank<1000) 的平均大小比整体均值低约 15%，即 E[Size | rank<1000] ≈ 0

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

大小-热度相关性量化：ρ=-0.3 意味着热门对象 (rank<1000) 的平均大小比整体均值低约 15%，即 E[Size | rank<1000] ≈ 0.85 × E[Size]，用于修正 LRU 驱逐时的空间占用偏差。

## Corrected Claim

大小-热度相关性量化：ρ=-0.3 意味着热门对象 (rank<1000) 的平均大小比整体均值低约 15%，即 E[Size | rank<1000] ≈ 0.85 × E[Size]，用于修正 LRU 驱逐时的空间占用偏差。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

correlation between object size and popularity in CDN cache negative correlation impact
