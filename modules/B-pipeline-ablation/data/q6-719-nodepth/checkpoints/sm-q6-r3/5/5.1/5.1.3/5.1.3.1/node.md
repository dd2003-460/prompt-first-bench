# N304: 跨AZ网络抖动导致的P99延迟增量 ΔP99_cross_az 的量化公式为：ΔP99_cross_az = P_cross_az_request × (T_c

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N106

## Claim

跨AZ网络抖动导致的P99延迟增量 ΔP99_cross_az 的量化公式为：ΔP99_cross_az = P_cross_az_request × (T_cross_az_p99 - T_same_az_p99)，其中 T_cross_az_p99 为跨AZ请求的P99延迟，T_same_az_p99 为同AZ请求的P99延迟，P_cross_az_request 为跨AZ请求占比（通常由负载均衡策略决定，如随机分发时为0.5）。

## Corrected Claim

跨AZ网络抖动导致的P99延迟增量 ΔP99_cross_az 的量化公式为：ΔP99_cross_az = P_cross_az_request × (T_cross_az_p99 - T_same_az_p99)，其中 T_cross_az_p99 为跨AZ请求的P99延迟，T_same_az_p99 为同AZ请求的P99延迟，P_cross_az_request 为跨AZ请求占比（通常由负载均衡策略决定，如随机分发时为0.5）。

## Evidence

先验知识/题面给定，逻辑校验通过
