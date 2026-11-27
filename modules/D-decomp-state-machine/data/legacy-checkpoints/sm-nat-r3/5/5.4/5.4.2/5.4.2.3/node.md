# N246: 排序误差导致的字节命中率损失 ΔH_err 的量化公式：ΔH_err = (Σ_{i∈swap_set} |p_i s_i - p_j s_j|) / (Σ_a

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N86, N87, N88

## Claim

排序误差导致的字节命中率损失 ΔH_err 的量化公式：ΔH_err = (Σ_{i∈swap_set} |p_i s_i - p_j s_j|) / (Σ_all p_i s_i)，其中 swap_set 为因排序偏移而被错误保留/驱逐的对象对；当平均偏移为 8 个位置时，ΔH_err ≈ 0.02%（即命中率从 99.96% 降至 99.94%），该数值依赖于 Pareto 尾部截断参数 x_max。

## Corrected Claim

排序误差导致的字节命中率损失 ΔH_err 的量化公式：ΔH_err = (Σ_{i∈swap_set} |p_i s_i - p_j s_j|) / (Σ_all p_i s_i)，其中 swap_set 为因排序偏移而被错误保留/驱逐的对象对；当平均偏移为 8 个位置时，ΔH_err ≈ 0.02%（即命中率从 99.96% 降至 99.94%），该数值依赖于 Pareto 尾部截断参数 x_max。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cache hit rate loss due to rank error Pareto heavy tail distribution
