# N289: LRU 稳态字节命中率下界的保守估算公式：H_LRU_lower = (Σ_{i=1}^{K_max} r_i * s_i) / (Σ_{j=1}^{N} r_

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LRU 稳态字节命中率下界的保守估算公式：H_LRU_lower = (Σ_{i=1}^{K_max} r_i * s_i) / (Σ_{j=1}^{N} r_j * s_j)。利用 Pareto 积分近似，分子 ≈ C * E[r|Cache] * E[s|Cache] / E[s|Cache] (简化为容量*热度密度)，分母为总字节流量 R_total。代入 K_max≈5,000, E[r|Cache]≈500/day, E[s|Cache]≈3KB, C=128GB，分子 ≈ 128GB * 500/day * 3KB / 1KB (单位换算后) ≈ 192,000 GB/day (需精确单位统一)，分母 R_total ≈ 5000 GB/day (基于 N176)，此估算显示 H_LRU_lower 接近 100% 存在单位错误，修正后：分子为缓存内命中字节量，应计算为 Σ(r_i*s_i for i in Cache)。若 Cache 覆盖 50% 字节流量 (N230)，则 H_LRU_lower ≈ 0.50。

## Corrected Claim

LRU 稳态字节命中率下界的保守估算公式：H_LRU_lower = (Σ_{i=1}^{K_max} r_i * s_i) / (Σ_{j=1}^{N} r_j * s_j)。利用 Pareto 积分近似，分子 ≈ C * E[r|Cache] * E[s|Cache] / E[s|Cache] (简化为容量*热度密度)，分母为总字节流量 R_total。代入 K_max≈5,000, E[r|Cache]≈500/day, E[s|Cache]≈3KB, C=128GB，分子 ≈ 128GB * 500/day * 3KB / 1KB (单位换算后) ≈ 192,000 GB/day (需精确单位统一)，分母 R_total ≈ 5000 GB/day (基于 N176)，此估算显示 H_LRU_lower 接近 100% 存在单位错误，修正后：分子为缓存内命中字节量，应计算为 Σ(r_i*s_i for i in Cache)。若 Cache 覆盖 50% 字节流量 (N230)，则 H_LRU_lower ≈ 0.50。

## Evidence

检索失败: no sources from any channel (all 5 failed)
