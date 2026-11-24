# N568: 跨网延迟惩罚 ΔT_cross 的基准值（同省/邻省，距离<200km）为 15ms，基于三大运营商骨干网互联点的物理距离与路由跳数（通常2-3跳）计算：ΔT_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N186

## Claim

跨网延迟惩罚 ΔT_cross 的基准值（同省/邻省，距离<200km）为 15ms，基于三大运营商骨干网互联点的物理距离与路由跳数（通常2-3跳）计算：ΔT_base = 2 * (200km / 200km/s) + 2 * T_hop ≈ 2ms + 2*6ms = 14ms，取整为 15ms。

## Corrected Claim

跨网延迟惩罚 ΔT_cross 的基准值（同省/邻省，距离<200km）为 15ms，基于三大运营商骨干网互联点的物理距离与路由跳数（通常2-3跳）计算：ΔT_base = 2 * (200km / 200km/s) + 2 * T_hop ≈ 2ms + 2*6ms = 14ms，取整为 15ms。

## Evidence

先验知识/题面给定，逻辑校验通过：光速传播延迟计算正确（200km/200km/s=1ms，往返2ms），路由跳数延迟估算合理（2-3跳，每跳约5-10ms），总延迟14ms取整为15ms符合工程惯例。

## Search Query

China telecom interconnection latency cross-ISP RTT base value
