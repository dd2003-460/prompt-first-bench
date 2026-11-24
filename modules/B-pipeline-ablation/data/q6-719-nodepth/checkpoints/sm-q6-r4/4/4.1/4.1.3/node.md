# N102: 网络中间件引入的额外延迟 T_overhead_edge，包括 TCP 握手、TLS 加密解密、HTTP 头处理及 CDN 内部路由查找，典型 P99 值在 5

- **status**: pending
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

父节点级核验未通过：不完备（子节点之间逻辑正交，分别覆盖了传输层、安全层、路由层和排队层。但完备性不足，父节点明确提到的“HTTP 头处理”延迟在子节点中缺失。此外，TCP 握手和 TLS 握手通常发生在连接建立阶段，而 CDN 路由和排队发生在请求处理阶段，虽然分类合理，但缺少应用层协议处理环节导致无法完全覆盖父节点定义的总延迟。）

## Search Query

CDN edge node processing latency P99 overhead
