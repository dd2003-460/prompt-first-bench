# N566: 多线 BGP 接入的 P99 延迟降低量 ΔT_p99_bgp (ms)：部署 BGP 多线接入后，跨网 P99 延迟从 40-60ms 降至 30-45ms，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N185

## Claim

多线 BGP 接入的 P99 延迟降低量 ΔT_p99_bgp (ms)：部署 BGP 多线接入后，跨网 P99 延迟从 40-60ms 降至 30-45ms，平均降低 10-20ms，主要源于 BGP 路由优化选择最优 Peering 路径，消除跨网调度延迟，但 P99 降低量在高峰时段（晚 8-11 点）可能缩小至 5-10ms。

## Corrected Claim

部署 BGP 多线接入通常能优化跨网路由路径，从而降低 P99 延迟，具体降低幅度取决于网络环境与高峰负载情况。

## Evidence

[质询]具体数值区间（40-60ms降至30-45ms）及高峰时段衰减幅度（5-10ms）属于高度依赖具体网络拓扑、ISP策略及业务负载的经验数据，缺乏通用性，且无来源支持其作为普遍规律。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

BGP multi-line access P99 latency reduction cross-network peak hour measurement China
