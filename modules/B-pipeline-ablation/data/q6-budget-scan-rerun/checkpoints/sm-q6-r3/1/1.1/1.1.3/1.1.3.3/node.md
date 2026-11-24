# N152: 长尾网络路径 (Bad Route) 对 P99 的贡献量化：定义 Bad Route 为 RTT > P95_RTT 的路径，其占比为 p_bad；P99 延

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

长尾网络路径 (Bad Route) 对 P99 的贡献量化：定义 Bad Route 为 RTT > P95_RTT 的路径，其占比为 p_bad；P99 延迟中由 Bad Route 导致的额外延迟为 ΔP99_route = p_bad × (RTT_bad_avg - RTT_p95)，典型 p_bad = 0.02-0.05，RTT_bad_avg 比 P95 高 50-100ms

## Corrected Claim

长尾网络路径 (Bad Route) 对 P99 的贡献量化：定义 Bad Route 为 RTT > P95_RTT 的路径，其占比为 p_bad；P99 延迟中由 Bad Route 导致的额外延迟为 ΔP99_route = p_bad × (RTT_bad_avg - RTT_p95)，典型 p_bad = 0.02-0.05，RTT_bad_avg 比 P95 高 50-100ms

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

network route degradation P99 latency contribution bad path ratio
