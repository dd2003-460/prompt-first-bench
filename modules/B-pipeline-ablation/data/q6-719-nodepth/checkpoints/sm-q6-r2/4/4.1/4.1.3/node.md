# N102: 网络中间件引入的额外延迟 T_overhead_edge，包括 TCP 握手、TLS 加密解密、HTTP 头处理及 CDN 内部路由查找，典型 P99 值在 5

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

网络中间件引入的额外延迟 T_overhead_edge，包括 TCP 握手、TLS 加密解密、HTTP 头处理及 CDN 内部路由查找，典型 P99 值在 5-15ms 之间，与用户地理距离无关但受并发负载影响。

## Corrected Claim

网络中间件引入的额外延迟 T_overhead_edge，包括 TCP 握手、TLS 加密解密、HTTP 头处理及 CDN 内部路由查找，典型 P99 值在 5-15ms 之间，与用户地理距离无关但受并发负载影响。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN edge node processing latency P99 overhead
