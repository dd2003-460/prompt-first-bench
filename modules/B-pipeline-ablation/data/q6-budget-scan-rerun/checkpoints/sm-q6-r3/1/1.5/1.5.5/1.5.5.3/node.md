# N249: 静态分布偏差导致的P99延迟预测误差量化：ΔL_p99_bias = |L_p99_dynamic - L_p99_static|，在α_mobile=0.15

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

静态分布偏差导致的P99延迟预测误差量化：ΔL_p99_bias = |L_p99_dynamic - L_p99_static|，在α_mobile=0.15时，预计偏差为 +8ms 至 +12ms（因漫游用户通常位于高RTT区域或长尾节点，拉高尾部延迟）。

## Corrected Claim

静态分布偏差会导致P99延迟预测出现正向误差（即预测值低于实际动态值），具体偏差量级取决于网络动态特性，通常在毫秒级范围内。

## Evidence

[质询]具体数值区间（+8ms 至 +12ms）缺乏通用理论支撑，属于特定场景下的经验估计，不同网络拓扑和负载下偏差量级可能显著不同，存在将特定案例泛化为普遍规律的风险。 | 先验知识/题面给定，逻辑校验通过（静态分布无法捕捉动态长尾导致P99偏高符合直觉），但具体数值为经验事实且无外部来源支持，故降级。

## Search Query

CDN P99 latency prediction error due to static vs dynamic user distribution
