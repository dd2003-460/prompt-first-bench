# N27: Pareto(α=1.1) 分布下，累积分布函数 F(s) = (s_min/s)^1.1。缓存中驻留对象的大小总和 S_cached 需满足 S_cached

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Pareto(α=1.1) 分布下，累积分布函数 F(s) = (s_min/s)^1.1。缓存中驻留对象的大小总和 S_cached 需满足 S_cached ≤ 128GB。由于 α 接近 1，大对象对总存储占用贡献显著，前 1% 最大的对象可能占据总存储的 50% 以上，导致 LRU 在字节命中率上的表现严重依赖于大对象的驻留情况。

## Corrected Claim

Pareto(α=1.1) 分布下，累积分布函数 F(s) = (s_min/s)^1.1。缓存中驻留对象的大小总和 S_cached 需满足 S_cached ≤ 128GB。由于 α 接近 1，大对象对总存储占用贡献显著，前 1% 最大的对象可能占据总存储的 50% 以上，导致 LRU 在字节命中率上的表现严重依赖于大对象的驻留情况。

## Evidence

检索失败: no sources from any channel (all 5 failed)
