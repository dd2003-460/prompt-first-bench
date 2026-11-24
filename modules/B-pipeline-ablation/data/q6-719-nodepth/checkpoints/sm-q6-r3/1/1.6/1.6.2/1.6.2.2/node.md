# N198: TLS 1.2 会话恢复（Session Resumption）使用 Session ID 或 Session Ticket 时，只需 1 RTT 完成 TLS

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

TLS 1.2 会话恢复（Session Resumption）使用 Session ID 或 Session Ticket 时，只需 1 RTT 完成 TLS 协商（Server 直接返回 ChangeCipherSpec 和 Finished），加上 TCP 1 RTT，总连接延迟为 2 RTT。

## Corrected Claim

TLS 1.2 会话恢复（Session Resumption）使用 Session ID 或 Session Ticket 时，只需 1 RTT 完成 TLS 协商（Server 直接返回 ChangeCipherSpec 和 Finished），加上 TCP 1 RTT，总连接延迟为 2 RTT。

## Evidence

先验知识/题面给定，逻辑校验通过：TLS 1.2 会话恢复机制（Session ID/Ticket）确实将握手过程简化为客户端发送 ClientHello（含会话标识），服务器直接响应 ChangeCipherSpec 和 Finished，无需密钥交换和证书验证，因此 TLS 层仅需 1 RTT；加上 TCP 三次握手的 1 RTT，总延迟为 2 RTT，符合网络协议基本原理。
