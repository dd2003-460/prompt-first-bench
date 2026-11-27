# N144: 在高波动工作点（ρ_rank ≈ 0.5），热度排名变化率 v ≈ 0.5 > v_crit，LFU 增益 ΔH < 1%，即 ΔH < 0.001，此时 LF

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

在高波动工作点（ρ_rank ≈ 0.5），热度排名变化率 v ≈ 0.5 > v_crit，LFU 增益 ΔH < 1%，即 ΔH < 0.001，此时 LFU 的累计频率统计严重滞后于实际访问模式，其保留集合与 LRU 几乎重合，增益可忽略不计，甚至因计数器开销略低于 LRU。

## Corrected Claim

在高波动工作点（ρ_rank ≈ 0.5），热度排名变化率 v ≈ 0.5 > v_crit，LFU 增益 ΔH < 1%，即 ΔH < 0.001，此时 LFU 的累计频率统计严重滞后于实际访问模式，其保留集合与 LRU 几乎重合，增益可忽略不计，甚至因计数器开销略低于 LRU。

## Evidence

先验知识/题面给定，逻辑校验通过：在高波动（ρ_rank≈0.5）下，LFU计数器更新滞后导致其保留集合与LRU高度重合，理论推导支持增益趋近于零或为负（因开销），符合缓存替换算法的基本原理。
