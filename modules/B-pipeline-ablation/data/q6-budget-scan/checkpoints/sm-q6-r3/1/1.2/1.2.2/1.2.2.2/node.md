# N88: 自建节点单台服务器的并发处理能力上限（CPS）约为 10,000-50,000 连接，若峰值并发超过此值，排队延迟 T_queue 将显著增加，导致 P99 延

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

自建节点单台服务器的并发处理能力上限（CPS）约为 10,000-50,000 连接，若峰值并发超过此值，排队延迟 T_queue 将显著增加，导致 P99 延迟从 15ms 上升至 50-100ms，需通过压测确定具体拐点。

## Corrected Claim

自建节点单台服务器的并发处理能力上限（CPS）约为 10,000-50,000 连接，若峰值并发超过此值，排队延迟 T_queue 将显著增加，导致 P99 延迟从 15ms 上升至 50-100ms，需通过压测确定具体拐点。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Nginx/CDN node concurrent connections limit P99 latency degradation
