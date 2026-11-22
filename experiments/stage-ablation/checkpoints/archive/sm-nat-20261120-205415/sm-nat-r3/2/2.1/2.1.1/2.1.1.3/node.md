# N116: 工作点3（极端负相关 ρ=-0.5）：若负相关更强，E[S|in_cache] ≈ 0.6MB，则 K_ext = 128GB/0.6MB ≈ 218,453；

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N40

## Claim

工作点3（极端负相关 ρ=-0.5）：若负相关更强，E[S|in_cache] ≈ 0.6MB，则 K_ext = 128GB/0.6MB ≈ 218,453；K_ext >> N=100,000，缓存容量相对于对象总数过剩，K_eff = 100,000；这表明在当前参数下，容量瓶颈不存在，命中率上限由热度分布的头部集中度决定。

## Corrected Claim

工作点3（极端负相关 ρ=-0.5）：若负相关更强，E[S|in_cache] ≈ 0.6MB，则 K_ext = 128GB/0.6MB ≈ 218,453；K_ext >> N=100,000，缓存容量相对于对象总数过剩，K_eff = 100,000；这表明在当前参数下，容量瓶颈不存在，命中率上限由热度分布的头部集中度决定。

## Evidence

先验知识/题面给定，逻辑校验通过：128GB/0.6MB ≈ 218,453 计算正确，且 K_ext > N 时 K_eff=N 符合缓存模型逻辑
