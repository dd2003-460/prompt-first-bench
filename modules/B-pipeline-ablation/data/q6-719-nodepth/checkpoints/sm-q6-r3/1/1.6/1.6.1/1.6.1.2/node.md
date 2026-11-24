# N195: TCP Handshake 占用 1 RTT，TLS 1.3 Full Handshake 占用 1 RTT，因此首次连接总延迟为 2 RTT；若结合 TCP 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

TCP Handshake 占用 1 RTT，TLS 1.3 Full Handshake 占用 1 RTT，因此首次连接总延迟为 2 RTT；若结合 TCP Fast Open (TFO)，TCP 握手可与 TLS ClientHello 合并，理论上可降至 1 RTT 完成连接和加密协商。

## Corrected Claim

TCP Handshake 占用 1 RTT，TLS 1.3 Full Handshake 占用 1 RTT，因此首次连接总延迟为 2 RTT；若结合 TCP Fast Open (TFO)，TCP 握手可与 TLS ClientHello 合并，理论上可降至 1 RTT 完成连接和加密协商。

## Evidence

先验知识/题面给定，逻辑校验通过
