# N328: CDN 内部路由查找与调度延迟 T_sched 受 DNS 解析缓存命中率 H_dns 和负载均衡算法复杂度影响，典型 T_sched = 1-5ms，若 H_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102

## Claim

CDN 内部路由查找与调度延迟 T_sched 受 DNS 解析缓存命中率 H_dns 和负载均衡算法复杂度影响，典型 T_sched = 1-5ms，若 H_dns < 0.9 则增加 DNS 查询 RTT。

## Corrected Claim

CDN 内部路由查找与调度延迟 T_sched 受 DNS 解析缓存命中率 H_dns 和负载均衡算法复杂度影响，典型 T_sched = 1-5ms，若 H_dns < 0.9 则增加 DNS 查询 RTT。

## Evidence

先验知识/题面给定，逻辑校验通过
