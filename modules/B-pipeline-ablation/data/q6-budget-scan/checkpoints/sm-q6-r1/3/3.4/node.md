# N18: 自建边缘节点策略的延迟特性：P99_self = RTT_user_to_nearest_selfpop + T_queue_self + T_transmis

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

自建边缘节点策略的延迟特性：P99_self = RTT_user_to_nearest_selfpop + T_queue_self + T_transmission，10个POP点覆盖核心城市，平均RTT_base ≈ 10-20ms（核心区域），但长尾区域RTT_base可能 > 50ms

## Corrected Claim

自建边缘节点策略的延迟特性：P99_self = RTT_user_to_nearest_selfpop + T_queue_self + T_transmission，10个POP点覆盖核心城市，平均RTT_base ≈ 10-20ms（核心区域），但长尾区域RTT_base可能 > 50ms

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

10 CDN POP points China coverage latency core cities
