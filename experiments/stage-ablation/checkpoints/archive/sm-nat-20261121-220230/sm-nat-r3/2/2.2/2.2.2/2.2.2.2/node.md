# N149: 在弱局部性工作点（β=0.9，长窗口 δ=24 小时），缓存污染率 P_short_term 上升至 10-15%，因为长时间窗口内访问模式漂移导致 LRU 驱

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

在弱局部性工作点（β=0.9，长窗口 δ=24 小时），缓存污染率 P_short_term 上升至 10-15%，因为长时间窗口内访问模式漂移导致 LRU 驱逐边界处的对象热度变化显著，污染率与窗口长度 δ 和热度变化率 v 的乘积相关，即 P_short_term ≈ k * v * δ，其中 v≈0.25，δ=1 天。

## Corrected Claim

在弱局部性工作点（β=0.9，长窗口 δ=24 小时），缓存污染率 P_short_term 上升至 10-15%，因为长时间窗口内访问模式漂移导致 LRU 驱逐边界处的对象热度变化显著，污染率与窗口长度 δ 和热度变化率 v 的乘积相关，即 P_short_term ≈ k * v * δ，其中 v≈0.25，δ=1 天。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU cache pollution rate long-term locality drift Pareto
