# N135: TLS握手延迟 T_tls 取决于会话复用率：完整握手（Full Handshake）约为 1-2 RTT（20-40ms），会话复用（Session Resu

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

TLS握手延迟 T_tls 取决于会话复用率：完整握手（Full Handshake）约为 1-2 RTT（20-40ms），会话复用（Session Resumption）约为 1 RTT（10-20ms），TLS 1.3 0-RTT 约为 0ms。

## Corrected Claim

TLS握手延迟 T_tls 取决于会话复用率：完整握手（Full Handshake）约为 1-2 RTT（20-40ms），会话复用（Session Resumption）约为 1 RTT（10-20ms），TLS 1.3 0-RTT 约为 0ms。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

TLS 1.3 handshake latency 0-RTT ms
