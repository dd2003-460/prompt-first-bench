# N119: 公有云CDN边缘节点的处理时间 T_proc_edge P99，主要包含 TLS 握手开销（若未复用连接）和 HTTP 响应头生成，典型值为 1-5ms，取决于

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

公有云CDN边缘节点的处理时间 T_proc_edge P99，主要包含 TLS 握手开销（若未复用连接）和 HTTP 响应头生成，典型值为 1-5ms，取决于节点 CPU 负载和并发连接数。

## Corrected Claim

公有云CDN边缘节点的处理时间 T_proc_edge P99，主要包含 TLS 握手开销（若未复用连接）和 HTTP 响应头生成，典型值为 1-5ms，取决于节点 CPU 负载和并发连接数。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN edge node processing time P99 latency benchmark
