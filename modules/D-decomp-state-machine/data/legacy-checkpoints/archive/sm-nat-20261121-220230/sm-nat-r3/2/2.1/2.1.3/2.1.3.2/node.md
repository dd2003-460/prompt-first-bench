# N143: 在中波动工作点（ρ_rank ≈ 0.75），热度排名变化率 v ≈ 0.25，接近临界阈值 v_crit ≈ 0.3，LFU 增益 ΔH 显著衰减至 LRU 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

在中波动工作点（ρ_rank ≈ 0.75），热度排名变化率 v ≈ 0.25，接近临界阈值 v_crit ≈ 0.3，LFU 增益 ΔH 显著衰减至 LRU 基准的 5-8%，即 ΔH ≈ 0.006-0.010，因为频率统计滞后导致 LFU 保留集与 LRU 保留集的对称差集 K_diff 扩大，驱逐决策错误率上升。

## Corrected Claim

在中波动工作点（ρ_rank ≈ 0.75），热度排名变化率 v ≈ 0.25，接近临界阈值 v_crit ≈ 0.3，LFU 增益 ΔH 显著衰减至 LRU 基准的 5-8%，即 ΔH ≈ 0.006-0.010，因为频率统计滞后导致 LFU 保留集与 LRU 保留集的对称差集 K_diff 扩大，驱逐决策错误率上升。

## Evidence

先验知识/题面给定，逻辑校验通过
