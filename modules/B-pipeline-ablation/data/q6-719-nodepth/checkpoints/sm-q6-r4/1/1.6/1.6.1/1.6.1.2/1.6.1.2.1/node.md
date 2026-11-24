# N569: TCP 三次握手（SYN-SYN/ACK-ACK）固定占用 1 RTT，该延迟是物理链路限制，无法通过应用层协议优化消除，除非使用 TCP Fast Open 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N195

## Claim

TCP 三次握手（SYN-SYN/ACK-ACK）固定占用 1 RTT，该延迟是物理链路限制，无法通过应用层协议优化消除，除非使用 TCP Fast Open 或 QUIC 等机制。

## Corrected Claim

TCP 三次握手（SYN-SYN/ACK-ACK）固定占用 1 RTT，该延迟是物理链路限制，无法通过应用层协议优化消除，除非使用 TCP Fast Open 或 QUIC 等机制。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

TCP three-way handshake 1 RTT latency baseline
