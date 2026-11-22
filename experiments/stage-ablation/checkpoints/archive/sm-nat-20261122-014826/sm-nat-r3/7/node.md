# N20: 稳态时间窗口 T_stable 估算：LRU 达到稳态所需时间取决于缓存中对象的平均驻留时间（Average Residency Time, ART）。在 50

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

稳态时间窗口 T_stable 估算：LRU 达到稳态所需时间取决于缓存中对象的平均驻留时间（Average Residency Time, ART）。在 5000 万请求/天、Top-1% 对象承载 95% 流量的情况下，热门对象（Top-1000）的请求间隔约为 5000万 / (0.95 * 1000) ≈ 5263 次/对象/天，即每 17 秒一次。LRU 稳态建立时间通常需覆盖 2-3 个最大对象驻留周期，对于小对象（1KB）驻留时间极短，但大冷对象可能驻留数天。保守估计 T_stable ≈ 3 * T_max_cold_object_residency，若冷对象平均访问间隔为 1 天，则 T_stable ≈ 3 天。

## Corrected Claim

稳态时间窗口 T_stable 估算：LRU 达到稳态所需时间取决于缓存中对象的平均驻留时间（Average Residency Time, ART）。在 5000 万请求/天、Top-1% 对象承载 95% 流量的情况下，热门对象（Top-1000）的请求间隔约为 5000万 / (0.95 * 1000) ≈ 5263 次/对象/天，即每 17 秒一次。LRU 稳态建立时间通常需覆盖 2-3 个最大对象驻留周期，对于小对象（1KB）驻留时间极短，但大冷对象可能驻留数天。保守估计 T_stable ≈ 3 * T_max_cold_object_residency，若冷对象平均访问间隔为 1 天，则 T_stable ≈ 3 天。

## Evidence

父节点级核验未通过：不完备（子节点之间正交（一个关注稳态判据/定义，一个关注冷对象驻留时间推导），无冗余。但存在不完备性：父节点明确给出了基于“Top-1%对象承载95%流量”的热门对象间隔估算（17秒/次）以及最终保守估计 T_stable ≈ 3天的逻辑链条，而子节点仅覆盖了“稳态判据定义”和“冷对象T_max_cold推导”，缺失了“热门对象稳态时间估算”或“T_stable最终综合计算逻辑”这一关键组成部分。父节点中的核心估算步骤（从对象间隔到T_stable的3倍系数应用）未被任何子节点显式覆盖。）
