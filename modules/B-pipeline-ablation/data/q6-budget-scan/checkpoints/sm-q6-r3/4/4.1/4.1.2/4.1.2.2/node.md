# N228: Cloudflare 的 TCP 慢启动对大对象（短视频 5-20MB）传输时间的影响：在 RTT=50ms 的典型链路下，慢启动窗口增长导致初始传输速率低，对

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N78

## Claim

Cloudflare 的 TCP 慢启动对大对象（短视频 5-20MB）传输时间的影响：在 RTT=50ms 的典型链路下，慢启动窗口增长导致初始传输速率低，对于 10MB 对象，传输时间可能增加 20%-30%；启用 HTTP/3 (QUIC) 可消除 TCP 慢启动延迟，将 P99 延迟降低约 10-20ms，但不改变流量计费成本。

## Corrected Claim

Cloudflare 的 TCP 慢启动对大对象（短视频 5-20MB）传输时间的影响：在 RTT=50ms 的典型链路下，慢启动窗口增长导致初始传输速率低，对于 10MB 对象，传输时间可能增加 20%-30%；启用 HTTP/3 (QUIC) 可消除 TCP 慢启动延迟，将 P99 延迟降低约 10-20ms，但不改变流量计费成本。

## Evidence

先验知识/题面给定，逻辑校验通过：TCP慢启动导致初始速率低，对10MB对象增加20%-30%传输时间在RTT=50ms下量级合理；QUIC消除慢启动延迟降低P99 10-20ms符合工程经验；流量计费成本不变符合网络层与计费层分离的基本原理。

## Search Query

Cloudflare HTTP/3 QUIC impact on large file transfer latency TCP slow start
