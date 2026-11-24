# N570: TCP Fast Open (TFO) 允许客户端在 SYN 包中携带 TLS ClientHello 数据（需服务器支持且客户端拥有有效的 TFO cooki

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N195

## Claim

TCP Fast Open (TFO) 允许客户端在 SYN 包中携带 TLS ClientHello 数据（需服务器支持且客户端拥有有效的 TFO cookie），从而将 TCP 握手与 TLS 握手合并为 1 RTT，节省 1 RTT 延迟；若无 TFO cookie，则仍为 2 RTT。

## Corrected Claim

TCP Fast Open (TFO) 允许客户端在 SYN 包中携带 TLS ClientHello 数据（需服务器支持且客户端拥有有效的 TFO cookie），从而将 TCP 握手与 TLS 握手合并为 1 RTT，节省 1 RTT 延迟；若无 TFO cookie，则仍为 2 RTT。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

TCP Fast Open TFO TLS ClientHello SYN packet 1 RTT
