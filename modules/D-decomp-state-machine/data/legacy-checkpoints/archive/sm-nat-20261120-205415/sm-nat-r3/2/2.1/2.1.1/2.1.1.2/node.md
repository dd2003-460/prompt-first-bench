# N115: 工作点2（负相关 ρ=-0.3）：由于热门对象较小，LRU 缓存内的对象平均大小 E[S|in_cache] ≈ 0.85MB，则 K_neg = 128GB/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N40

## Claim

工作点2（负相关 ρ=-0.3）：由于热门对象较小，LRU 缓存内的对象平均大小 E[S|in_cache] ≈ 0.85MB，则 K_neg = 128GB/0.85MB ≈ 154,200；K_neg > N=100,000，缓存仍可容纳全部对象，K_eff = 100,000，负相关并未改变 K 的上限，但改变了缓存内对象的组成（更多小对象）。

## Corrected Claim

工作点2（负相关 ρ=-0.3）：由于热门对象较小，LRU 缓存内的对象平均大小 E[S|in_cache] ≈ 0.85MB，则 K_neg = 128GB/0.85MB ≈ 154,200；K_neg > N=100,000，缓存仍可容纳全部对象，K_eff = 100,000，负相关并未改变 K 的上限，但改变了缓存内对象的组成（更多小对象）。

## Evidence

先验知识/题面给定，逻辑校验通过：128GB/0.85MB ≈ 154,200 计算正确，且 154,200 > 100,000 符合逻辑，结论自洽。
