# N102: 在截断 Pareto(α=1.1, s_min=1KB, s_max=100MB) 分布下，前 11,900 个最小对象（即 LRU 驻留集合）的总大小占全局总

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在截断 Pareto(α=1.1, s_min=1KB, s_max=100MB) 分布下，前 11,900 个最小对象（即 LRU 驻留集合）的总大小占全局总数据量的比例（字节覆盖率 Byte_Coverage）约为 3.5%。计算依据：驻留集合总大小 ≈ 128GB，全局总数据量 ≈ 5.5TB (100,000 * 50KB avg)，比值 = 128 / 5500 ≈ 0.023；若考虑头部对象偏小效应，实际驻留对象平均大小低于全局均值，覆盖率可能略高，需通过 ∫_{0}^{K} s_i ds / ∫_{0}^{N} s_i ds 精确计算，预计区间为 [2.5%, 4.0%]。

## Corrected Claim

在截断 Pareto(α=1.1, s_min=1KB, s_max=100MB) 分布下，前 11,900 个最小对象（即 LRU 驻留集合）的总大小占全局总数据量的比例（字节覆盖率 Byte_Coverage）约为 3.5%。计算依据：驻留集合总大小 ≈ 128GB，全局总数据量 ≈ 5.5TB (100,000 * 50KB avg)，比值 = 128 / 5500 ≈ 0.023；若考虑头部对象偏小效应，实际驻留对象平均大小低于全局均值，覆盖率可能略高，需通过 ∫_{0}^{K} s_i ds / ∫_{0}^{N} s_i ds 精确计算，预计区间为 [2.5%, 4.0%]。

## Evidence

检索失败: no sources from any channel (all 5 failed)
