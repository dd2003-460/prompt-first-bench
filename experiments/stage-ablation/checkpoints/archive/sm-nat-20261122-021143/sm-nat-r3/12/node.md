# N158: 对象更新率 u=1%/天 对 LRU 有效命中率的折损机制主要源于“陈旧命中”（Stale Hit）导致的无效缓存空间占用和一致性验证开销。折损系数 δ_u 可

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

对象更新率 u=1%/天 对 LRU 有效命中率的折损机制主要源于“陈旧命中”（Stale Hit）导致的无效缓存空间占用和一致性验证开销。折损系数 δ_u 可近似为 δ_u ≈ u * T_avg * (1 - H_stale_correction)，其中 T_avg 为平均驻留时间。若 T_avg << 1/u，则 δ_u 可忽略；若 T_avg >> 1/u，则 δ_u ≈ 1 - e^{-u*T_avg}。具体数值需基于 T_avg 的精确计算（约 0.15-1.2 天）确定折损百分比。

## Corrected Claim

对象更新率 u=1%/天 对 LRU 有效命中率的折损机制主要源于“陈旧命中”（Stale Hit）导致的无效缓存空间占用和一致性验证开销。折损系数 δ_u 可近似为 δ_u ≈ u * T_avg * (1 - H_stale_correction)，其中 T_avg 为平均驻留时间。若 T_avg << 1/u，则 δ_u 可忽略；若 T_avg >> 1/u，则 δ_u ≈ 1 - e^{-u*T_avg}。具体数值需基于 T_avg 的精确计算（约 0.15-1.2 天）确定折损百分比。

## Evidence

检索失败: no sources from any channel (all 5 failed)
